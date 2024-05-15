from loader import bot, dp
from config_data.config import *
from database.db_main import *

# Функция проверяет, есть ли пользователь в базе данных Games_data
def existing_check(user_id):
    existing_user = Games_data.get_or_none(Games_data.user_id == user_id)
    print(existing_user)
    if existing_user:
        return True

@dp.message(F.data=="game_1_stat")
async def process_stat_command(message: Message):
    # Проверка на то, что пользователь есть в базе данных, иначе - добавляем его в неё
    if existing_check(message.from_user.id) is None:
        new_user = Games_data(user_id=message.from_user.id, user_name=message.from_user.full_name, user_wins=0, user_attempts=0, user_total_games1=0, user_total_games2=0, secret_number=0)
        new_user.save()
        logging.debug(f"{message.from_user.id, message.from_user.full_name} added to games database!")

    user = Games_data.get(Games_data.user_id == message.from_user.id)
    if existing_check(message.from_user.id):
        await message.answer(
            "Ваша игровая статистика:",
            f'Всего игр сыграно: {user.user_total_games1}\n'
            f'Игр выиграно: {user.user_wins}'
        )