import requests
from pprint import pprint

TOKEN = ''

# проверка работы бота, все ли ок с токеном
url = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url)
print(response.json())

# получить все сообщения от пользователей
get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(get_updates)
pprint(response.json())

# отправить сообщение пользователю
user_id = '158448812'
send_m = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

requests.get(send_m, params={'chat_id': user_id, 'text': 'привет'})