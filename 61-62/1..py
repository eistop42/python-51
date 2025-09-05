import json
import os
import streamlit as st


class JsonDB:
    def __init__(self, filename):
        self.filename = filename

    def get_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            return json.dump(data, f)

json_db = JsonDB('C:\\Users\\TOP\\Documents\\Евдокимов\\python-51\\61-62\\notes.json')

if 'notes' not in st.session_state:
    st.session_state['notes'] = json_db.get_data()

notes = st.session_state['notes']

with st.form('notes_form', clear_on_submit=True):
    name = st.text_input('Название')
    text = st.text_area('Текст')

    submitted = st.form_submit_button('Сохранить')
    if submitted:
        notes.append({'name': name, 'text': text})
        json_db.save_data(notes)

note_names = [note['name'] for note in notes]

selected_names = st.selectbox('Выбери заметку', note_names)

for note in notes:
    if note['name'] == selected_names:
        st.header(note['name'])
        st.text(note['text'])
        break