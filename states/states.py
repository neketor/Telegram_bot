from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class default_states(StatesGroup):
    in_game: bool = False

class guess_numb(StatesGroup):
    number = State()

