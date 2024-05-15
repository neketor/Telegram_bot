from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

#Угадай число
class guess_numb(StatesGroup):
    start_game = State()
    number = State()

# Камень-ножницы-бумага
class rock_paper(StatesGroup):
    start_game = State()
    number = State()

class open_weather_state(StatesGroup):
    name: str = State()
