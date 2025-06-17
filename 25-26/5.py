user = input('Введи строку:')
words = user.split()
words_dict = {}
for word in words:
    if len(word) > 5:
        words_dict[word]=len(word)
print(words_dict)