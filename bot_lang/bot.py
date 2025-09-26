import telebot
from telebot import types

from db import TelegramDB
from translate import YandexGPT
from speech import synthesize
from recognotion import recognize

from creds import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
db = TelegramDB('tg.json')
yandex = YandexGPT()

class Keyboards:

    def get_language_menu(self):
        markup_inline = types.InlineKeyboardMarkup()
        markup_inline.add(types.InlineKeyboardButton('английский', callback_data='lang=en'))
        markup_inline.add(types.InlineKeyboardButton('французский', callback_data='lang=fr'))
        return markup_inline

keyboards = Keyboards()

@bot.message_handler(commands=['start'])
def send_hello(message):
    chat_id = message.chat.id

    # создать кнопки в интерфейсе
    markup_inline = keyboards.get_language_menu()

    bot.send_message(chat_id, 'Привет! Выбириай язык ддя перевода', reply_markup=markup_inline)

@bot.callback_query_handler(func=lambda call: 'lang' in call.data)
def set_language(update):
    from pprint import pprint
    chat_id = update.message.chat.id
    lang = update.data.split('=')[1]
    db.set_value(chat_id, 'lang', lang)
    bot.send_message(chat_id, f'пиши сообщения для перевода')

@bot.callback_query_handler(func=lambda call: call.data == 'start_dialog')
def start_dialog(update):
    chat_id = update.message.chat.id
    bot.send_message(chat_id, f'Начали диалог. Пиши сообщения - буду переводить')


@bot.message_handler(commands=['language'])
def change_language(message):
    # отправить клавиатуру я зыками
    markup_inline = keyboards.get_language_menu()
    bot.send_message(message.chat.id, 'выбирай', reply_markup=markup_inline)

@bot.message_handler(func=lambda message: True)
def get_text(message):
    # 1. Получить текущий язык для перевода
    chat_id = message.chat.id
    lang = db.get_value(chat_id, 'lang')
    print(lang)
    if not lang:
        return bot.send_message(chat_id, 'Сначала выбери язык: /start')
    pormpt = f'переведи на {lang} текст: {message.text}'
    result = yandex.get_answer(pormpt)
    bot.send_message(message.chat.id, result)

    # отправить голосовое сообщение
    voice = synthesize(result)
    bot.send_voice(chat_id, voice)

@bot.message_handler(content_types=['voice'])
def get_voice(message):
    voice = message.voice
    file_info = bot.get_file(voice.file_id)

    file = bot.download_file(file_info.file_path)
    text = recognize(file)
    print(text)

bot.infinity_polling()