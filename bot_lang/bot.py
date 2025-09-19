import telebot
from telebot import types

from db import TelegramDB

TOKEN = ''
bot = telebot.TeleBot(TOKEN)
db = TelegramDB('tg.json')

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id

    # создать кнопки в интерфейсе
    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(types.InlineKeyboardButton('английский', callback_data='lang=en'))
    markup_inline.add(types.InlineKeyboardButton('французский', callback_data='lang=fr'))

    bot.send_message(chat_id, 'Привет! Выбириай язык ддя перевода', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: 'lang' in call.data)
def set_language(update):
    from pprint import pprint
    chat_id = update.message.chat.id
    lang = update.data.split('=')[1]
    db.set_value(chat_id, 'lang', lang)
    bot.send_message(chat_id, f'выбрал язык: {update.data}')

    markup_inline = types.InlineKeyboardMarkup()
    markup_inline.add(types.InlineKeyboardButton('начать диалог', callback_data='start_dialog'))
    bot.send_message(chat_id, 'кликай, если готов', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: call.data == 'start_dialog')
def start_dialog(update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id, f'Начали диалог. Пиши сообщения - буду переводить')

@bot.message_handler(func=lambda message: True)
def get_text(message):
    bot.send_message(message.chat.id, 'вот перевод')

bot.infinity_polling()