capitals = {"Франция": "Париж", 'Италия': 'Рим'}

# перебор всех ключей словаря
for country in capitals:
    print(country)

# перебор всех значений словаря
for capital in capitals.values():
    print(capital)

# перебор пар ключ-значения
for country, capital in capitals.items():
    print(country, capital)