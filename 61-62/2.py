import streamlit as st

from yandex import YandexGPT

# иницилазация клиента Яндекса
token = ''
catalog = ''
yandexgpt = YandexGPT(token, catalog)

st.write('Сбор данных')

#если загружаем первый раз - создай пустой список пользователей
if 'users' not in st.session_state:
    st.session_state['users'] = []


question = st.text_input('Введи вопрос: ')
button = st.button('Задать')

if button and question:
    # сходить в АПИ яндекса
    answer = yandexgpt.get_answer(question)
    st.markdown(answer)

