# from loader import bot, dp
# from config_data import config
# import requests
#
# @dp.message(config.Command(commands='get_weather'))
# async def get_weather_start(message: config.Message):
#     config.User_state = "get_weather"
#     await message.answer("Напишите название города (Пример: Moscow, Krasnodar - англ.): ")
#
# @dp.message()
# async def get_weather_town_info(message: config.Message):
#     print(config.User_state)
#     req = requests.get(
#         f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={config.API_KEY}&units=metric"
#     )
#     if req.status_code == 200:
#         await message.answer(f"Погода на сегодня в городе {message.text}:")
#         print('Запрос был успешным (статус код 200)')
#         data = req.json()
#         print(data)
#         await message.answer(f"Город = {data['name']}"
#                              f"\nСредн. температура = {data['main']['temp']}°C"
#                              f"\nМин. температура = {data['main']['temp_min']}°C"
#                              f"\nМакс. температура = {data['main']['temp_max']}°C"
#                              f"\nМакс. температура = {data['main']['temp_max']}°C"
#                              f"\nСкор. ветра = ~{data['wind']['speed']} метров в сек."
#                              )
#
#     else:
#         print(f'Запрос вернул статус код {req.status_code}')
