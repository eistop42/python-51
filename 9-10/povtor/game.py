import random

comp = random.randint(1, 10)

for i in range(1,5):
    print(f'Раунд {i}')
    user = int(input('Введи число: '))
    if comp == user:
        print('Угадал')
        break
    else:
        print(f'Не угадал, ответ {comp}')

print('Конец игры')
