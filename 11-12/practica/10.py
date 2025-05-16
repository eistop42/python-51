
import random

questions = ['Самая высока гора?', 'Столица России?']
answers = ['Эверест', 'Москва']

q = random.choice(questions)
print(q)
ind = questions.index(q)
user = input('введи ответ: ')

if user == answers[ind]:
    print('верно')
else:
    print('не верно')