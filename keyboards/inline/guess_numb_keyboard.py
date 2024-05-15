from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

"""Клавиатура для игры 'Угадай число'"""

game_1 = InlineKeyboardButton(
    text='Статистика',
    callback_data='game_1_stat'
)

game_2 = InlineKeyboardButton(
    text='Начать игру',
    callback_data='game_1'
)

in_menu = InlineKeyboardButton(
    text='← Назад',
    callback_data='in_games_menu'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[game_1],
                     [game_2],
                     [in_menu]]
)