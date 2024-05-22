from database.models import db, User_data, Games_data

""" Если вы удалили базу данных - через этот файл её можно создать по новой. """

with db:
    db.create_tables([User_data, Games_data])