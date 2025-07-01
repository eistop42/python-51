
# создание простой функции
# ничего не принимает не возвращает
def hello():
    print('Привет мир')

hello()
hello()

# создание простой функции
# принимает имя, выводит приветствие
def hello_user(name):
    print(f'Привет {name}!')

hello_user('Алиса')
hello_user('Боб')

# a = input('введи имя: ')
# hello_user(a)

# функция принимает и возвращает данные
def square(a, b):
    res = a * b
    return res

s = square(5, 12)
s2 = square(3, 9)
print(s)
print(s2)


# вызов функции с именованными аргументами
s = square(b=4, a=12)
print(s)