from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

""" Состояния пользователя """

#Угадай число
class guess_numb(StatesGroup):
    start_game = State()
    number = State()

class open_weather_state(StatesGroup):
    name: str = State()
