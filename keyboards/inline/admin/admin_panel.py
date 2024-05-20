from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


in_menu_button = InlineKeyboardButton(
    text='Список всех пользователей',
    callback_data='users_list'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[in_menu_button]]
)