from loader import bot, dp
from config_data.config import F, Message
from database.db_main import Games_data
from keyboards.inline.in_menu_keyboard import keyboard
@dp.callback_query(F.data=="profile_button")
async def process_stat_command(message: Message):
    """ По нажатию на инлайн-кнопку профиля в меню (и не только), выводится профиль пользователя. """

    user = Games_data.get(Games_data.user_id == message.from_user.id)
    await bot.send_message(message.from_user.id, f'Профиль пользователя: {message.from_user.full_name}\n\nИмя: {message.from_user.first_name}\nФамилия: {message.from_user.last_name}\n\n"Ваша игровая статистика:\nВсего игр сыграно: {user.user_total_games1}\nИгр выиграно: {user.user_wins}\n\n', reply_markup=keyboard)