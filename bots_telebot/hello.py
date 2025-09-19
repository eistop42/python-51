import telebot
from telebot import types
from pprint import pprint

from yandex import YandexGPT

TOKEN = '7787720175:AAHD6MmKI0zSfOJDu3aRwtjrV1B1wMn0o30'

bot = telebot.TeleBot(TOKEN)
yandex = YandexGPT()


@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id

    # создание кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    markup.add(types.KeyboardButton('Расскажи анекдот'))
    markup.add(types.KeyboardButton('Предсказание на завтра'))

    # создать кнопки в интерфейсе
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(types.InlineKeyboardButton('Расскажи анекдот', callback_data='joke'))

    bot.send_message(chat_id, 'Привет!', reply_markup=markup_inline)

@bot.message_handler(commands=['help'])
def send_hello(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Конечно, давай помогу')

@bot.callback_query_handler(func=lambda call: call.data == 'joke')
def send_joke(update):
    chat_id = update.message.chat.id
    joke = yandex.get_answer('пришли смешной анекдот про Вовочку с неожиданная концовкой')
    bot.send_message(chat_id, 'Придумываю анекдот...')
    bot.send_message(chat_id, joke)

@bot.message_handler(regexp='Предсказание на завтра')
def send_joke(message):
    chat_id = message.chat.id
    joke = yandex.get_answer('пришли вымышленное предсказание на завтрашний день')
    bot.send_message(chat_id, joke)

bot.infinity_polling()