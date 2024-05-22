from config_data.config import *
from loader import bot, dp
from keyboards.inline.menu_keyboard import keyboard

""" Главное меню бота """
@dp.callback_query(F.data=="in_menu")
@dp.message(Command(commands=['menu']))
async def process_help_command(message: Message):
    await bot.send_message(message.from_user.id, "Главное меню бота:", reply_markup=keyboard)