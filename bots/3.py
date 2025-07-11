import requests
import json
import time

TOKEN = ''
get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'



def send_message(chat_id, text):
    """Функция для отправки сообщения пользователю"""
    send_m = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.get(send_m, params={'chat_id': chat_id, 'text': text})

with open('db.json') as f:
    db = json.load(f)

last_message_id = db['last_message_id']

while True:
    time.sleep(0.5)
    data = requests.get(get_updates).json()
    for message in data['result']:
        chat_id = message['message']['chat']['id']
        text = message['message']['text']
        message_id = message['message']['message_id']

        if int(message_id) > int(last_message_id) :
            if text == 'привет':
                send_message(chat_id, 'привет 😀😀')
            if text == 'пока':
                send_message(chat_id, 'пока 😐😐')
            print('что-то отправил')

            last_message_id = message['message']['message_id']
            print('последнее', last_message_id)

    db['last_message_id'] = last_message_id
    with open('db.json', 'w') as f:
       json.dump(db, f)