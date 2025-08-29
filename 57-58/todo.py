import json
import os
from abc import ABC, abstractmethod

from rich.console import Console
from rich.style import Style
from rich.table import Table

class DB:
    def __init__(self, filename):
        self.filename = filename

    def add_task(self, task_name):
        """Метод для добавления задачи"""
        tasks = self.read()
        tasks.append(task_name)
        self.write(tasks)


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


class AbstractView(ABC):

    @abstractmethod
    def print(self, text):
        pass

    @abstractmethod
    def print_tasks(self, tasks):
        pass

class RichView(AbstractView):

    def print(self, text):
        console = Console()
        style = Style(color='blue', bgcolor='yellow')
        console.print(text, style=style)

    def print_tasks(self, tasks: list):
        console = Console()
        table = Table(title='Список дел')
        table.add_column('Номер')
        table.add_column('Название', style='yellow')

        for number, name in enumerate(tasks, start=1):
            table.add_row(str(number), name)
        console.print(table)

class BasicView(AbstractView):
    def print(self, text: str):
        print(text)

    def print_tasks(self, tasks: list):
        for task in tasks:
            print(task)

class ToDo:
    def __init__(self, db: DB, view: RichView):
        self.db = db
        self.view = view

    def add_task(self):
        """Добавление задачи"""
        name = input('☺ Введи задачу: ')
        self.db.add_task(name)
        self.view.print('Задача добавлена!')

    def show_tasks(self):
        tasks = self.db.read()
        self.view.print_tasks(tasks)


# экземпляр классы базы
db = DB('tasks.json')
rich_view = RichView()
basic_view = BasicView()

user = input('1 - базовая версия, 2 - платная версия')
if user == '1':
    todo = ToDo(db, basic_view)
elif user == '2':
    todo = ToDo(db, rich_view)

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