from loader import bot, dp
from config_data.config import Message, logging, F
from random import randint
from keyboards.inline.games_inline.rock_scissors_paper_game.rock_paper_keyboard import keyboard as game_keyboard
from keyboards.inline.games_inline.rock_scissors_paper_game.rock_paper_choose_keyboard import keyboard as choose_keyboard
from keyboards.inline.in_menu_keyboard import keyboard as in_menu
from database.db_main import Games_data

""" Игра "Камень-ножницы-бумага" """

@dp.callback_query(F.data=="game_2_keyboard")
async def guess_the_number_start(message: Message):
    """ По нажатию на кнопку из клавиатуры игрового меню - открывает под-меню игры "камень-ножницы-бумага" """
    await bot.send_message(message.from_user.id, 'Меню игры "Камень-ножницы-бумага":', reply_markup=game_keyboard)

# При победе пользователя записывает победу в базу данных
def win():
    user.user_wins += 1
    user.user_total_games1 += 1
    user.save()

# При поражение пользователя записывает данные о проигрыше в базу данных
def defeat():
    user.user_total_games1 += 1
    user.save()


@dp.callback_query(F.data=="game_2")
async def guess_the_number_start(message: Message):
    """ В данной функции происходит инициализация пользователя, и ему в базе данных присваиваются значения. """

    # Проверка на наличие пользователя в базе данных. Если нет - добавляем
    existing_user = Games_data.get_or_none(Games_data.user_id == message.from_user.id)
    if existing_user is None:
        new_user = Games_data(user_id=message.from_user.id, user_name=message.from_user.full_name, user_wins=0,
                              user_attempts=0, user_total_games1=0, user_total_games2=0, secret_number=0,
                              random_game_2_obj=0)
        new_user.save()
        logging.debug(f"{message.from_user.id, message.from_user.full_name} added to games database!")

    global user

    user = Games_data.get(Games_data.user_id == message.from_user.id)
    user.random_game_2_obj = randint(1, 3)
    user.save()
    await bot.send_message(message.from_user.id, "Выбирай :)", reply_markup=choose_keyboard)


@dp.callback_query(F.data=="stone_button")
async def guess_the_number_start(message: Message):
    """ Проверка, если пользователь выбрал камень """

    if user.random_game_2_obj == 2:
        await bot.send_message(message.from_user.id, "Поздравляю! Вы победили. У меня были ножницы.", reply_markup=in_menu)
        win()
    elif user.random_game_2_obj == 3:
        await bot.send_message(message.from_user.id, "Вы проиграли! У меня была бумага.", reply_markup=in_menu)
        defeat()
    else:
        await bot.send_message(message.from_user.id, "Хм, ничья :) У обоих камень.", reply_markup=in_menu)
        defeat()


@dp.callback_query(F.data=="scissors_button")
async def guess_the_number_start(message: Message):
    """ Проверка, если пользователь выбрал ножницы """

    if user.random_game_2_obj == 3:
        await bot.send_message(message.from_user.id, "Поздравляю! Вы победили. У меня была бумага.", reply_markup=in_menu)
        win()
    elif user.random_game_2_obj == 1:
        await bot.send_message(message.from_user.id, "Вы проиграли! У меня был камень.", reply_markup=in_menu)
        defeat()
    else:
        await bot.send_message(message.from_user.id, "Хм, ничья :) У обоих ножницы.", reply_markup=in_menu)
        defeat()

@dp.callback_query(F.data=="paper_button")
async def guess_the_number_start(message: Message):
    """ Проверка, если пользователь выбрал бумагу """

    if user.random_game_2_obj == 1:
        await bot.send_message(message.from_user.id, "Поздравляю! Вы победили. У меня был камень.", reply_markup=in_menu)
        win()
    elif user.random_game_2_obj == 2:
        await bot.send_message(message.from_user.id, "Вы проиграли! У меня были ножницы.", reply_markup=in_menu)
        defeat()
    else:
        await bot.send_message(message.from_user.id, "Хм, ничья :) У обоих бумага.", reply_markup=in_menu)
        defeat()
