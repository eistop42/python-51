age = input('Возраст: ')

days = int(age) * 365
hours = days * 24
sec = hours * 60 * 60

print(f'Кол-во дней {days}')
print(f'Кол-во часов {hours}')
print(f'Кол-во cекунд {sec}')