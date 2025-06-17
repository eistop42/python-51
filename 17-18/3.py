a = [1,2,3,4]
string = '1111'
count = 0
for number in a:
    if str(number) in string:
        count += 1
print(count)