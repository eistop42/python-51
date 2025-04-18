numb1 = int(input('первое число'))
numb2 = int(input('второе число'))

for i in range(numb1, numb2+1):
    if i % 2 != 0:
        print(i)