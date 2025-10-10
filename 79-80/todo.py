from db import DB

db = DB('db')

# спрашиваем имя и авторизуемся
name = input('Введи имя: ')
user = db.get_user(name)

# регистарция + авторизация
if not user:
    print('Нужна регстрация')
    action = input('Добавить тебя в базу? 1 - да, 2 - нет')
    if action == '1':
        db.add_user(name)
        user = db.get_user(name)
    else:
        print('пока 😉')

if user:
    user = dict(user)
    print(f'Привет {user['name']} Начинаем работу')
    while True:
        print('Выбери действие: ')
        print('1 - добавить задачу')
        print('2 - посмотреть задачи')
        action = input('выбирай: ')
        if action == '1':
            name = input('Название задачи')
            db.add_task(name, user['id'])
            print('Задача добавлена')
        if action == '2':
            tasks = db.get_tasks(user['id'])
            for task in tasks:
                task = dict(task)
                print(task['name'])