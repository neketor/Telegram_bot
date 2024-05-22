import logging
from loader import bot, dp
from config_data.config import Command, Message, F
from database.models import User_data
from keyboards.inline.admin.admin_panel import keyboard

@dp.message(Command(commands=["admin_panel"]))
async def is_admin_func(message: Message):
    """ После проверки на то, является ли пользователь админом - выдаёт доступ к панели"""

    user = User_data.get(User_data.user_id == message.from_user.id)
    if user.is_admin == 1:
        logging.debug(f"{message.from_user.id, message.from_user.full_name} - entered to the admin mode.")
        await bot.send_message(message.from_user.id, f"{message.from_user.id} : {message.from_user.full_name}, вы вошли в админ-панель! \nВсего пользователей у бота: {User_data.select().count()}\nВсего админов: {User_data.select().where(User_data.is_admin == 1).count()}", reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, "У вас недостаточно прав, чтобы пользоваться этой командой.")

# По нажатию инлайн-кнопки из админ-панели, запускается хэндлер
@dp.callback_query(F.data == "users_list")
async def get_users(message: Message):
    """ Выводит список пользователей бота. """

    users = User_data.select()
    response = "Список пользователей:\n"
    count = 0
    # Если список пользователей слишком большой, то он заканчивается на 150 строках.
    for user in users:
        if count < 150:
            response += f"{user.user_id} : {user.user_name}"
            count += 1
        else:
            response += f"И т. д."
    await bot.send_message(message.from_user.id, response)