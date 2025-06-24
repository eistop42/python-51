login = input('логин')
passw = input('пароль')

with open('users.txt', encoding='utf-8') as f:
    users = f.readlines()
    for user in users:
        user = user.split('-')
        if login == user[0] and passw == user[1].strip():
            print('разрешен')
            break
    else:
        print('не разрешен ')