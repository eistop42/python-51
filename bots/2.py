import requests
import time

TOKEN = ''

# проверка работы бота, все ли ок с токеном
url = f'https://api.telegram.org/bot{TOKEN}/getMe'
get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

r = requests.get(get_updates).json()
print(r)


# while True:
#     r = requests.get(get_updates)
#     print(r.json())
#     time.sleep(5)
