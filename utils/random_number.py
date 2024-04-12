import random, requests

def random_number(first, sec):
    return random.randint(first, sec) if sec > first else print(BaseException("Второе число превышает первое."))

def get_weather_town_info():
    req = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=6288204852993431d8b726f7b06a8229&units=metric"
    )
    if req.status_code == 200:
        print('Запрос был успешным (статус код 200)')
        data = req.json()
        print(data)
    else:
        print(f'Запрос вернул статус код {req.status_code}')
