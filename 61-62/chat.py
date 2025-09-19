import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh


class DB:

    def __init__(self, BIN_ID=None, API_KEY=None):
        self.BIN_ID = BIN_ID
        self.API_KEY = API_KEY
        self.base_url = f'https://api.jsonbin.io/v3/b/{BIN_ID}'
        self.get_url = f'{self.base_url}/latest'
        self.headers = {
            'X-Access-Key': API_KEY
        }

    def get_all_data(self):
        return requests.get(self.get_url, json=None, headers=self.headers).json()

    def get_messages(self):
        return self.get_all_data()['record']['messages']

    def add_mesage(self, message):
        messages = self.get_messages()
        messages.append(message)
        print(messages)
        return requests.put(self.base_url, json={"messages": messages}, headers=self.headers).json()


db = DB(BIN_ID='68baacd8d0ea881f407281d1', API_KEY='$2a$10$xGYYSIf17KOuCJ8e3k3cbO0vR.Rkw5r88094T2EqhVWmQT7s/lbWG')

import streamlit as st

st_autorefresh(interval=10000)
for message in db.get_messages():
    st.write(message)

name = st.chat_input("Введи сообщение")
# Кнопка "Сохранить"
if name:
    db.add_mesage(name)
    st.session_state.usermessage = ""
    st.rerun()