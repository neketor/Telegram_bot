from loader import bot, dp
from config_data import config
from states.states import open_weather_state, FSMContext
import requests
from keyboards.inline.in_menu_keyboard import keyboard


@dp.callback_query(lambda x: x.data=="open_wth_button")
async def get_weather_start(message: config.Message, state: FSMContext):
    """ По нажатию на кнопку из клавиатуры меню - запускает хэндлер """

    await bot.send_message(message.from_user.id, "Напишите название города на английском (Пример: Moscow, Krasnodar, London): ")
    await state.set_state(open_weather_state.name)

@dp.message(open_weather_state.name)
async def get_weather_town_info(message: config.Message, state: FSMContext):
    """ Здесь уже происходит get запрос, и результат выводится пользователю. """

    await state.update_data(number=message.text)
    name = await state.get_data()
    print(name)
    req = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={name['number']}&appid={config.API_KEY}&units=metric"
    )
    if req.status_code == 200:
        await message.answer(f"Текущая погода в городе {message.text}:")
        print('Запрос был успешным (статус код 200)')
        data = req.json()
        print(data)
        await bot.send_message(message.from_user.id, f"Город = {data['name']}"
                             f"\nСредн. температура = {data['main']['temp']}°C"
                             f"\nМин. температура = {data['main']['temp_min']}°C"
                             f"\nМакс. температура = {data['main']['temp_max']}°C"
                             f"\nМакс. температура = {data['main']['temp_max']}°C"
                             f"\nСкор. ветра = ~{data['wind']['speed']} метров в сек."
                             , reply_markup=keyboard)
    else:
        await bot.send_message(message.from_user.id, "Запрос не прошел. Попробуйте снова.", reply_markup=keyboard)
        await state.clear()
        print(f'Запрос вернул статус код {req.status_code}')
