from loader import bot, dp
from config_data.config import Message, F, Command
from random import randint
from states.states import guess_numb, FSMContext
from keyboards.inline.in_menu_keyboard import keyboard
from keyboards.inline.games_inline.guess_number.guess_numb_keyboard import keyboard as game_keyboard
from database.db_main import Games_data
""" Игра "Угадай число" """

@dp.callback_query(F.data=="game_1_keyboard")
async def guess_the_number_start(message: Message, state: FSMContext):
    """ По нажатию на кнопку из клавиатуры игрового меню - открывает под-меню игры "Угадай число" """
    await bot.send_message(message.from_user.id, 'Меню игры "Угадай число":', reply_markup=game_keyboard)

@dp.callback_query(F.data=="game_1")
async def guess_the_number_start(message: Message, state: FSMContext):
    """ В данном хэндлер происходит инициализация пользователя, и ему в базе данных присваиваются значения. """

    global user

    user = Games_data.get(Games_data.user_id == message.from_user.id)
    user.secret_number = randint(1, 20)
    user.user_attempts = 10
    user.save()

    await state.clear()
    await state.set_state(guess_numb.number)
    await bot.send_message(message.from_user.id, "Я загадал число!\n Командой /cancel вы можете остановить игру.\n Напишите число:")


@dp.message(Command(commands=['cancel']))
async def guess_the_number_cancel(message: Message, state: FSMContext):
    """ Остановка игры """

    await message.answer(f"Игра окончена! Загаданное число: {user.secret_number}\nЧтобы получить справку о боте и его возможностях, введите команду /menu")
    await state.clear()

@dp.message(guess_numb.number)
async def guess_the_number_process(message: Message, state: FSMContext):
    """ Функция, в которой введённое число пользователя проверяется, и определяется исход. """

    await state.update_data(number=message.text)
    number = await state.get_data(); number = int(number["number"])
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

