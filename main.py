from loader import bot, dp
import handlers  # noqa

if __name__ == '__main__':
    dp.run_polling(bot)
