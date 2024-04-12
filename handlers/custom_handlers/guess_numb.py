from loader import bot, dp
from config_data.config import *
from utils.random_number import *
from states.states import *

Users = {}
ATTEMPTS = 10

# Этот хэндлер будет срабатывать на команду "/stat"
@dp.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    await message.answer(
        f'Всего игр сыграно: '
        f'{Users[message.from_user.id]["total_games"]}\n'
        f'Игр выиграно: {Users[message.from_user.id]["wins"]}'
    )

@dp.message(Command(commands=['guess_numb']))
async def guess_the_number_start(message: Message, state: FSMContext):
    if message.from_user.id not in Users:
        Users[message.from_user.id] = {
            'in_game': True,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
        }
    Users[message.from_user.id]["in_game"] = True
    Users[message.from_user.id]["attempts"] = ATTEMPTS
    Users[message.from_user.id]["secret_number"] = random_number(1, 50)
    await state.set_state(guess_numb.number)
    await message.answer("Я загадал число!\n Командой /cancel вы можете остановить игру.\n Напишите число:")

@dp.message(Command(commands=['cancel']))
async def guess_the_number_cancel(message: Message, state: FSMContext):
    if message.from_user.id in Users:
        Users[message.from_user.id]["in_game"] = False
        await message.answer(f"Игра окончена! Загаданное число: {Users[message.from_user.id]['secret_number']}\nЧтобы получить справку о боте и его возможностях, введите команду /help")
        await state.clear()

@dp.message(guess_numb.number)
async def guess_the_number_process(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    number = await state.get_data()
    if message.from_user.id in Users:
        if int(message.text) == Users[message.from_user.id]['secret_number']:
            Users[message.from_user.id]["in_game"] = False
            Users[message.from_user.id]["wins"] += 1
            Users[message.from_user.id]["total_games"] += 1
            await message.answer(f"Поздравляю! Вы победили! Чтобы получить справку о боте и его возможностях, введите команду /help")
            User_state = ""
            print(User_state)
        elif int(message.text) < Users[message.from_user.id]['secret_number']:
            Users[message.from_user.id]["attempts"] -= 1
            await message.answer(f"Загаданное число больше. Оставшиеся попытки: {Users[message.from_user.id]['attempts']}")
        elif int(message.text) > Users[message.from_user.id]['secret_number']:
            Users[message.from_user.id]["attempts"] -= 1
            await message.answer(f"Загаданное число меньше. Оставшиеся попытки: {Users[message.from_user.id]['attempts']}")
        else:
            await message.reply('Бот принимает только цифры от 1 до 50 и команду cancel для выхода из игры.')
        if Users[message.from_user.id]['attempts'] == 0:
            await message.answer(f"Игра окончена! Загаданное число: {Users[message.from_user.id]['secret_number']}\nЧтобы получить справку о боте и его возможностях, введите команду /help")
            await state.clear()

