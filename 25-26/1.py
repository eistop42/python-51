dictionary = {
 "mork": "кот",
 "brel": "бежит",
 "drun": "по",
 "plek": "дороге"
}
fake_sentence = "mork brel drun plek plek"
fake_list = fake_sentence.split()
a=[]
for word in fake_list:
    a.append(dictionary[word])
    
print(' '.join(a))