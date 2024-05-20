from loader import bot, dp
from config_data.config import *
from database.models import *
from states.states import FSMContext

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    with db:
        existing_user = User_data.get_or_none(User_data.user_id == message.from_user.id)
        if existing_user is None:
            new_user = User_data(user_id=message.from_user.id, user_name=message.from_user.full_name, is_admin=0)
            new_user.save()
            logging.debug(f"{message.from_user.id, message.from_user.full_name} added to database!")

        await bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}! Я телеграм-Бот Charles Smith :)\n Главное меню бота: /menu")