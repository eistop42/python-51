
for i in range(5):
    name = input('Название товара: ')

    with open('prod.txt', 'a', encoding='utf-8') as f:
        f.write(name+'\n')