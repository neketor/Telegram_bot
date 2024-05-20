from peewee import *

db = SqliteDatabase(".database.db")

class BaseModel(Model):
    class Meta:
        database=db
        db_table="User"

class User_data(BaseModel):
    user_id = IntegerField()
    user_name = CharField()
    is_admin = IntegerField()



class Games_data(BaseModel):
    user_id = IntegerField()
    user_name = CharField()
    user_wins = IntegerField()
    user_attempts = IntegerField()
    # Количество игр, сыгранных в игру "Угадай число"
    user_total_games1 = IntegerField()
    # Количество игр, сыгранных в игру "Камень-ножницы-бумага"
    user_total_games2 = IntegerField()
    secret_number = IntegerField()
    # Цифрами 1, 2 или 3 будут выбираться камень, ножницы или бумага (1 = stone 2 = scissors 3 = paper)
    random_game_2_obj = IntegerField()