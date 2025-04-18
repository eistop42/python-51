import random

comp = random.randint(1,10)
count = 0
user = int(input('Введи число:'))
while user != comp:
    print('Не угадал')
    user = int(input('Введи число:'))
    count += 1
print('Угадал!')
