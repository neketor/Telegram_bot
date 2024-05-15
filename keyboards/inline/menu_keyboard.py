from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

"""Главное меню бота"""

games_button = InlineKeyboardButton(
    text='🎮 Игры',
    callback_data='in_games_menu'
)

open_wth_button = InlineKeyboardButton(
    text='🌦️ Погода',
    callback_data='open_wth_button'
)

profile_button = InlineKeyboardButton(
    text='Ваш профиль',
    callback_data='profile_button'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[games_button,
                     open_wth_button], [profile_button]]
)