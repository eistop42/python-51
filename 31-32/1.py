# чтение файла целиком
file = open('data.txt', encoding='utf-8')

data = file.read()
print(data)

file.close()

# чтение файла по строкам
file = open('data.txt', encoding='utf-8')
data = file.readlines()
print(data)
file.close()

# чтение файла c перебором строк
file = open('data.txt', encoding='utf-8')
data = file.readlines()

for i in range(len(data)):
    print(f'{i}.{data[i].strip()}')

file.close()


# создание и запись в файл
file = open('data1.txt', 'w', encoding='utf-8')
file.write('привет\n')
file.write('пока\n')
file.close()

# добавление в файл
file = open('data1.txt', 'a', encoding='utf-8')
file.write('привет\n')
file.write('пока\n')
file.close()

# запись списка в файл
file = open('data1.txt', 'a', encoding='utf-8')
city = ['Екб\n', 'Москва\n']
file.writelines(city)
file.close()

with open('data2.txt', 'w', encoding='utf-8') as file:
    file.write('новая строка\n')
    file.write('еще строка\n')

print('на этой строке файл уже закрыт')

# запись списка с отступами
with open('data3.txt', 'w', encoding='utf-8') as file:
    names = ['Alisa', 'Bob', 'John']
    for name in names:
        file.write(name)
        file.write('\n')


# запись в файл информации от пользователя
name = input('Введи имя: ')
print('Добавляю в файл...')
with open('users.txt', 'w', encoding='utf-8') as file:
    file.write(name)
print('Записал!')