import random

comp = random.randint(1, 10)
count = 0

while count < 4:
    count += 1
    user = int(input('Введи число: '))
    if comp == user:
        print('Угадал')
        break
    else:
        print(f'Не угадал, ответ {comp}')

print('Конец игры')
