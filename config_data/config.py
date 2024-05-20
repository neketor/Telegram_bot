import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, KICKED, MEMBER, and_f, or_f
from aiogram.types import Message, CallbackQuery
from aiogram.types import ChatMemberUpdated
import logging

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

weather_API = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")