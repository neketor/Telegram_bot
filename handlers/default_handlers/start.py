from loader import bot, dp
from config_data.config import *


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Charles Swith!\n Чтобы узнать подробную информацию обо мне, напишите команду /help')