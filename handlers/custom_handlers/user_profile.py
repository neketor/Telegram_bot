from loader import bot, dp
from config_data.config import F, Message, logging
from database.db_main import Games_data
from keyboards.inline.in_menu_keyboard import keyboard
@dp.callback_query(F.data=="profile_button")
async def process_stat_command(message: Message):
    """ По нажатию на инлайн-кнопку профиля в меню (и не только), выводится профиль пользователя. """

    existing_user = Games_data.get_or_none(Games_data.user_id == message.from_user.id)
    # Проверка на наличие пользователя в базе данных. Если нет - добавляем
    if existing_user is None:
        new_user = Games_data(user_id=message.from_user.id, user_name=message.from_user.full_name, user_wins=0,
                              user_attempts=0, user_total_games1=0, user_total_games2=0, secret_number=0,
                              random_game_2_obj=0)
        new_user.save()
        logging.debug(f"{message.from_user.id, message.from_user.full_name} added to games database!")

    user = Games_data.get(Games_data.user_id == message.from_user.id)
    await bot.send_message(message.from_user.id, f'Профиль пользователя: {message.from_user.full_name}\n\nИмя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\n\n"Ваша игровая статистика:\nВсего игр сыграно: {user.user_total_games1}\nИгр выиграно: {user.user_wins}\n\n', reply_markup=keyboard)