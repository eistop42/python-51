import requests

class OpenWeather:

    def __init__(self, token):
        """Параметры по умолчанию"""
        self.token = token
        self.url = f'https://api.openweathermap.org/data/2.5/weather?appid={token}&units=metric&lang=ru'

    def get_weather(self, lat, lon):
        "Метод для получения данных о погоде"
        r = requests.get(self.url, params={'lat': lat, 'lon': lon})
        weather = self.format_weather(r.json())
        return weather

    def format_weather(self, data):
        """Метод для форматирования данных.
        Возвращает: "Екатеринбург: 15 (ощущается как 13)"
        """
        name = data['name']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        return f"{name}: {temp} (ощущается {feels_like})"

open_w = OpenWeather(token='8ae52edcb4fb242a16df41725340c407')

user_lat = float(input('Введи широту: '))
user_lon = float(input('Введи долготу: '))

print(open_w.get_weather(user_lat, user_lon))