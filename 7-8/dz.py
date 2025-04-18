word = input('Введи слово: ')
symbol = input('Введи символ: ')

res = word.find(symbol)
if res >= 0:
    print(f'Индекс: {res}')
else:
    print('Символа нет')
