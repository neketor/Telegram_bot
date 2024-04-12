from loader import bot, dp
from config_data.config import *

# Навешиваем декоратор с указанием в качестве фильтра типа контента
@dp.message(F.voice)
async def process_sent_voice(message: Message):
    # Выводим апдейт в терминал
    print(message.model_dump_json(indent=4))
    # Отправляем сообщение в чат, откуда пришло голосовое
    await message.answer(text='Вы прислали голосовое сообщение!')