from loader import bot, dp
import handlers  # noqa
from config_data.config import Message, F, logging

""" Файл main - запуск бота """

if __name__ == '__main__':

    # логируем любые сообщения пользователей

    logging.basicConfig(
        level=logging.DEBUG,
        format = '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                '%(lineno)d - %(name)s - %(message)s'
    )
    @dp.message()
    async def process_start_command(message: Message):
        logging.debug(f"{message.from_user.id, message.from_user.full_name, message.text}")


    dp.run_polling(bot)
