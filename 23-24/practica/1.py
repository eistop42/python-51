regions = {'Свердловская область': 66, 'Челябиснкая область': 74}

for region in regions:
    print(region)

for code in regions.values():
    print(code)

for region, code in regions.items():
    print(f'Код региона: {code}, {region}')