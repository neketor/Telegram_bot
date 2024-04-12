import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, KICKED, MEMBER
from aiogram.types import Message
from aiogram.types import ChatMemberUpdated
from dataclasses import dataclass
from environs import Env

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

weather_API = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

admin_ids: list[int] = [5091485602]

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку о боте"),
    ("echo", "Запустить эхо-функцию.")
)
GAMES_COMMANDS = (
    ("guess_numb", 'запустить игру "Угадай число"'),
    ("help", "Вывести справку о боте"),
    ("echo", "Запустить эхо-функцию.")
)
WEATHER_COMMANDS = (
    ("get_weather", "Получить статистику о погоде в определённом городе (по названию)"),
    ("help", "Вывести справку о боте")
)


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных

@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

def load_config(path: str):
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_LIST')))
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host='DB_HOST',
            db_user='DB_USER',
            db_password='DB_PASSWORD'
        )
    )