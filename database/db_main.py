from database.models import *

with db:
    db.create_tables([User_data, Games_data])