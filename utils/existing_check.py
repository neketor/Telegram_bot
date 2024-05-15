from database.db_main import *

# Функция проверяет, есть ли пользователь в базе данных Games_data
def existing_check(user_id):
    existing_user = Games_data.get_or_none(Games_data.user_id == user_id)
    print(existing_user)
    if existing_user:
        return True
    return None