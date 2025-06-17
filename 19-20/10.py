for i in range(25,61):
    if i%5 == 0:
        print(i, 'кратно 5')
    elif i%3 == 0:
        print(i, 'кратно 3')
    elif i == 42:
        print(i, 'секретное число')
    else:
        print(i)