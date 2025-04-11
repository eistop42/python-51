import random

number = random.randint(1,10)
user = int(input('Введите число:'))

if user == number:
    print('Угадал')
else:
    print('Не угадал')
    print(f'Ответ: {number}')