import requests
import random
import json
import time
from pprint import  pprint

TOKEN = ''
get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

keyboard = {"keyboard": [[{"text": "Добавить дело"}], [{"text": "Посмотреть дела"}]], 'resize_keyboard': True}

inline_keyboard = {"inline_keyboard": [
    [{"text": "Добавить дело", 'callback_data': 'add_task'}],
    [{"text": "Посмотреть дела", 'callback_data': 'show_tasks'}]
]}


def send_message_keyboad(chat_id, text):
    """Функция для отправки сообщения пользователю"""
    send_m = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(send_m, json={'chat_id': chat_id, 'text': text, 'reply_markup': inline_keyboard})

def send_message(chat_id, text):
    """Функция для отправки сообщения пользователю"""
    send_m = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(send_m, json={'chat_id': chat_id, 'text': text})


with open('db.json') as f:
    db = json.load(f)

last_message_id = db['last_message_id']
state = ''
tasks = []
while True:
    time.sleep(0.5)
    data = requests.get(get_updates).json()

    for message in data['result']:

        # получить id сообщения любого типа
        if message.get('message'):
            message_id = message['message']['message_id']

        elif message.get('callback_query'):
            message_id = message['callback_query']['message']['message_id']

        if int(message_id) > int(last_message_id):
            # обрабокта обычных сообщений

            if message.get('message'):
                text = message['message']['text']
                chat_id = message['message']['chat']['id']
                if text == '/start':
                    send_message_keyboad(chat_id, 'Привет, кликай по кнопкам!')
                else:
                    # добавляем дело поьлзователя
                    tasks.append(text)
                    print(tasks)
                    send_message_keyboad(chat_id, 'Дело добавлено!')
            # обрабокта кликов по инлайн кнопкам
            elif message.get('callback_query'):
                chat_id = message['callback_query']['message']['chat']['id']
                callback_data = message['callback_query']['data']

                if callback_data == 'add_task':
                    send_message(chat_id, 'Введите текст дела')


            last_message_id = message_id

    db['last_message_id'] = last_message_id

    with open('db.json', 'w') as f:
        json.dump(db, f)
