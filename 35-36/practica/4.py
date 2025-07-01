def factorail(number):
    f = 1
    for i in range(1, number+1):
        f = f * i
    return f
print(factorail(4))
print(factorail(5))