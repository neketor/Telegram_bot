from loader import bot, dp
from config_data.config import ChatMemberUpdated, ChatMemberUpdatedFilter, KICKED, MEMBER, logging

""" Хэндлеры срабатывают, если пользователь разблокировал или заблокировал бота """

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
      logging.debug(f"Пользователь: {event.from_user.id} заблокировал бота.")

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def process_user_unblocked_bot(event: ChatMemberUpdated):
      logging.debug(f"Пользователь: {event.from_user.id} разблокировал бота.")
      await bot.send_message(event.from_user.id, f'{event.from_user.first_name}, Добро пожаловать обратно!')