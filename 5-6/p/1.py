word = 'колобок'
user = input('введи букву')

count = word.count(user)

if count > 0:
    print('Угадал')
else:
    print('не угадал')