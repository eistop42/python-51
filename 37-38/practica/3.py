import json
def load_db():
    """читает данные из файла"""
    with open('users.json', encoding='utf-8') as f:
        return json.load(f)

def save_db():
    """сохраняет данные в файл"""
    with open('users.json', 'w', encoding='utf-8') as f:
        return json.dump(users, f, ensure_ascii=False)

def add_user(name):
    """добавление пользователя"""
    if name not in users:
        users.append(name)
        print('добавил пользователя')

def show_users():
    """просмотр списка пользователей"""
    res = ','.join(users)
    return res

# читать данные из базы
users = load_db()

while True:
    print('1 - добавить пользователя, 2- посмотреть список, 3- выход')
    action = input('выбери действие: ')
    print(users)
    if action == '1':
        user = input('Введи имя: ')
        add_user(user)
        save_db()

    elif action == '2':
        users_list = show_users()
        print(users_list)
