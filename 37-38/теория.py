
number_1 = 4
number_2 = 6

def add(a,b):
    res = a + b
    return res

c = add(number_1, number_2)
print(c)


# пример с глобальным списком
users = []

def add_user(name):
    users.append(name)

def show_users():
    res = '\n'.join(users)
    return res

add_user('alisa')
add_user('bob')
print(show_users())