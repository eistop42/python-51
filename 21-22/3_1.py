words = {'собака': 'dog', 'кошка': 'cat'}

count = 0
for word_rus, word_eng in words.items():
    user = input(f'Введи перевод слова {word_rus}')
    if user == word_eng:
        print('Правильно')
        count += 1
    else:
        print('Неправильно')
print(f'Ты набрал баллов: {count}')