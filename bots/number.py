import requests
import random
import json
import time

TOKEN = ''
get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

keyboard = {"keyboard":[[{"text": "давай"}]], 'resize_keyboard': True}

def send_message(chat_id, text):
    """Функция для отправки сообщения пользователю"""
    send_m = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(send_m, json={'chat_id': chat_id, 'text': text, 'reply_markup': keyboard})

with open('db.json') as f:
    db = json.load(f)

last_message_id = db['last_message_id']
state = ''
while True:
    time.sleep(0.5)
    data = requests.get(get_updates).json()
    print(data)
    for message in data['result']:
        chat_id = message['message']['chat']['id']
        text = message['message']['text']
        message_id = message['message']['message_id']

        if int(message_id) > int(last_message_id) :
            if text == '/start':
                send_message(chat_id, 'Хочешь сыграть в игру?')
            elif text == 'давай':
                state = 'game'
                number = random.randint(1, 10)
                send_message(chat_id, f'Я загадал число от 1 до 10')
                send_message(chat_id, number)
            elif text.isdigit() == True and state == 'game':
                # проверить правильное ввел число или нет
                # используйте int(text)
                if int(text) == number:
                    state = ''
                    send_message(chat_id, 'угадал  🎉 🎉 ')
                    send_message(chat_id, f'Кликай по кнопке, чтобы начать')
                else:
                    send_message(chat_id, 'не угадал ')

            last_message_id = message['message']['message_id']


    db['last_message_id'] = last_message_id
    with open('db.json', 'w') as f:
       json.dump(db, f)