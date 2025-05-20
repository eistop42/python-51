numbers_1 = [40,2,3,1,5]
numbers_2 = []

for i in range(len(numbers_1)):
    if numbers_1[i] % 2 == 0:
        print(numbers_1[i])
        numbers_2.append(numbers_1[i])
        
print(numbers_2)