from loader import bot, dp
from config_data.config import *

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
      print(f"Пользователь {event.from_user.id} заблокировал бота")

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_unblocked_bot(event: ChatMemberUpdated):
      print(f"Пользователь {event.from_user.id} разблокировал бота")
      await bot.send_message(chat_id = event.from_user.id,text = f'{event.from_user.first_name}, Добро пожаловать обратно!')