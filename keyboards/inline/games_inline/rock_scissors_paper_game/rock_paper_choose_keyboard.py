from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

""" Во время самой игры, у вас будет выбор между камнем/ножницами или бумагой """

stone_button = InlineKeyboardButton(
    text='Камень',
    callback_data='stone_button'
)

scissors_button = InlineKeyboardButton(
    text='Ножницы',
    callback_data='scissors_button'
)

paper_button = InlineKeyboardButton(
    text='Бумага',
    callback_data='paper_button'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[stone_button],
                     [scissors_button],
                     [paper_button]]
)