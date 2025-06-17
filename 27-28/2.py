a = {1,2,3}
b = {2,4}
c = {1, 2}

print(a|b) # объединение
print(a&b) # пересчение
print(a-b)
print(b-a)

users = {'alisa', 'anton'}
users2 = {'anton', 'alex'}

print(users|users2)
print(users&users2)

users = ['alisa', 'anton', 'alisa']
users = set(users)
print(users)