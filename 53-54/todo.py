import json
import os

class DB:
    def __init__(self, filename):
        self.filename = filename

    def write(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)

    def read(self):
        """Чтение данных из базы"""
        # если файла нет
        if not os.path.exists(self.filename):
            return []
        # читаем файл и возвращаем json из него
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)



class ToDo:
    def __init__(self, db):
        self.db = db

    def add_task(self):
        """Добавление задачи"""
        name = input('☺ Введи задачу: ')
        # получаем задачи из базы и добавляем новую задачу
        tasks = self.db.read()
        tasks.append(name)

        self.db.write(tasks)
        print('Задача добавлена 😎')

    def show_tasks(self):
        tasks = self.db.read()
        print('⚫⚫⚫===Список задач===⚫⚫⚫')
        for number, task in enumerate(tasks, start=1):
            print(f'🟦{number}. {task}')

# экземпляр классы базы
db = DB('tasks.json')

todo = ToDo(db)

while True:
    print('Выбери действие:')
    print('1 - добавить дело')
    print('2 - посмотреть дела')
    action = input('вводи: ')
    if action == '1':
        # вызвать метод добавления дела
        todo.add_task()
    elif action == '2':
        # вызвать метод просмотра дел
        todo.show_tasks()