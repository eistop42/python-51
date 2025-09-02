import random

chat = {"привет": ['привет', 'добрый день'], 'как дела': ['хорошо', 'норм']}

print(chat['привет'])

while True:
    text = input('Введи текст: ')

    if text == '1':
        break

    if text in chat:
        h = random.choice(chat[text])
        print(h)
    else:
        print('не понимаю...')


# print('Привет', name)
# print(f'Привет, {name}')

for i in range(5):
    print('привет', end=' ')