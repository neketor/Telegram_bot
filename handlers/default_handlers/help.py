from loader import bot, dp
from config_data.config import Command, Message
from states.states import FSMContext
from keyboards.inline.in_menu_keyboard import keyboard

""" По коменде /help, хэндлер просто выводит небольшую информацию """

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["help"]))
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    await bot.send_message(message.from_user.id, f"Данный бот создан в развлекательных целях, и имеет в себе несколько миниигр, а также может показывать погоду в вашем городе через API сервис OpenWeather.\nИнтерфейс бота предельно прост, так что проблема в том, чтобы разобраться у вас не должна возникнуть :)", reply_markup=keyboard)