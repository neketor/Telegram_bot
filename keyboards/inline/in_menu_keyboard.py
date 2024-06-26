from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

""" Клавиатура с кнопкой "в меню" """

in_menu_button = InlineKeyboardButton(
    text='В меню',
    callback_data='in_menu'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[in_menu_button]]
)