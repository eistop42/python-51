import random

while True:
    answer = random.randint(0,1)
    user = input('задай вопрос: ')

    if answer == 0:
        print('да')
    else:
        print('нет')