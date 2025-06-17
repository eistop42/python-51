user = input('Введи слово: ')
letters = {}

for letter in user:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
print(letters)