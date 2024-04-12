from config_data.config import load_config, Bot, Dispatcher

config = load_config(".env")

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()
