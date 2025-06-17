regions = {'Свердловская область': 66, 'Челябиснкая область': 74}

score = 0
for region, code in regions:
    user = int(input(f'Ввести код региона для {region}'))

    if user == code:
        score += 1
        print('правильно')
    else:
        print('неправильно')
print(f'Ты набрал {score}')