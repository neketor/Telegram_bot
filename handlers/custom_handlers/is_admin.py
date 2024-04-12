from loader import dp
from handlers.filters.is_admin import *

# Этот хэндлер будет срабатывать, если апдейт от админа
@dp.message(IsAdmin(admin_ids), Command(commands=["admin_commands"]))
async def answer_if_admins_update(message: Message):
    await message.answer('Вы админ')