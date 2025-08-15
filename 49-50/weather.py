import requests

token = '8ae52edcb4fb242a16df41725340c407'

def get_weather(lat, lon):
    "Фукнция для получения данных о погоде в виде json"
    url = f'https://api.openweathermap.org/data/2.5/weather?appid={token}&units=metric&lang=ru'
    r = requests.get(url, params={'lat': lat, 'lon': lon})
    return r.json()

def format_weather(data):
    """Функуия для форматирования данных.
    Возвращает: "Екатеринбург: 15 (ощущается как 13)"
    """
    name = data['name']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    return f"{name}: {temp} (ощущается {feels_like})"

# ввод данных пользователем
user_lat = float(input('Введи широту: '))
user_lon = float(input('Введи долготу: '))

# вызов функций, вывод данных
weather_json = get_weather(user_lat, user_lon)
weather = format_weather(weather_json)
print(weather)
