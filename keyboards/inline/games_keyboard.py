from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

"""Меню игр"""

game_1 = InlineKeyboardButton(
    text='🎮 Угадай число',
    callback_data='game_1_keyboard'
)

game_2 = InlineKeyboardButton(
    text='🎮 Камень ножницы бумага',
    callback_data='game_2_keyboard'
)

in_menu = InlineKeyboardButton(
    text='В главное меню',
    callback_data='in_menu'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[game_1],
                     [game_2],
                     [in_menu]]
)