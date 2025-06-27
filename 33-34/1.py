import json

name = {
    'name': 'Ivan',
    'age': 30,
    'is_student': False,
    'skills': ['python', 'sql']
}
# запись в json
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(name, file, ensure_ascii=False, indent=4)

# чтение json
with open('users.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)

