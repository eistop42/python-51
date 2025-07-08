import requests

TOKEN = ''
get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

data = requests.get(get_updates).json()

for message in data['result']:
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    print(chat_id, text)
