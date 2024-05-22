from config_data.config import *
from loader import bot, dp
from keyboards.inline.games_keyboard import keyboard

""" Игровое меню """

@dp.callback_query(F.data == "in_games_menu")
async def set_game_state(call: CallbackQuery):
    await bot.send_message(call.from_user.id, "Доступные игры:", reply_markup=keyboard)