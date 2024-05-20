from loader import bot, dp
from config_data.config import *
from utils.random_number import *
from states.states import guess_numb, FSMContext
from keyboards.inline.in_menu_keyboard import keyboard
from keyboards.inline.guess_numb_keyboard import keyboard as game_keyboard
from database.db_main import *
from utils.existing_check import existing_check

@dp.callback_query(F.data=="game_1_keyboard")
async def guess_the_number_start(message: Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Меню игры "Угадай число":', reply_markup=game_keyboard)

@dp.callback_query(F.data=="game_1")
async def guess_the_number_start(message: Message, state: FSMContext):
    # add to database
    if existing_check(message.from_user.id) is None:
        new_user = Games_data(user_id=message.from_user.id, user_name=message.from_user.full_name, user_wins=0, user_attempts=0, user_total_games1=0, user_total_games2=0, secret_number=0, random_game_2_obj=0)
        new_user.save()
        logging.debug(f"{message.from_user.id, message.from_user.full_name} added to games database!")

    global user

    user = Games_data.get(Games_data.user_id == message.from_user.id)
    user.secret_number = random_number(1, 20)
    user.user_attempts = 10
    user.save()

    await state.clear()
    await state.set_state(guess_numb.number)
    await bot.send_message(message.from_user.id, "Я загадал число!\n Командой /cancel вы можете остановить игру.\n Напишите число:")


@dp.message(Command(commands=['cancel']))
async def guess_the_number_cancel(message: Message, state: FSMContext):
    if existing_check(message.from_user.id):
        await message.answer(f"Игра окончена! Загаданное число: {user.secret_number}\nЧтобы получить справку о боте и его возможностях, введите команду /menu")
        await state.clear()

@dp.message(guess_numb.number)
async def guess_the_number_process(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    number = await state.get_data(); number = int(number["number"])
    if existing_check(message.from_user.id):
        if number == user.secret_number:
            user.user_wins += 1
            user.user_total_games1 += 1
            user.save()
            await bot.send_message(message.from_user.id, f"Вы победили! Загаданное число: {user.secret_number}", reply_markup=keyboard)
        elif number < user.secret_number:
            user.user_attempts -= 1
            user.save()
            await message.answer(f"Загаданное число больше. Оставшиеся попытки: {user.user_attempts}")
        elif number > user.secret_number:
            user.user_attempts -= 1
            user.save()
            await message.answer(f"Загаданное число меньше. Оставшиеся попытки: {user.user_attempts}")
        else:
            await message.reply('Бот принимает только цифры от 1 до 50 и команду /cancel для выхода из игры.')
        if user.user_attempts == 0:
            await bot.send_message(message.from_user.id, f"Игра окончена! Загаданное число: {user.secret_number}", reply_markup=keyboard)
            user.user_total_games1 += 1
            user.save()
            await state.clear()

