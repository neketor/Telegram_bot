import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, KICKED, MEMBER, and_f, or_f
from aiogram.types import Message, CallbackQuery
from aiogram.types import ChatMemberUpdated
from dataclasses import dataclass
from environs import Env
import logging

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

weather_API = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

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