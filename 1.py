a = ['поспать', 'поесть']

# for i in range(len(a)):
#     print(f"{i+1} {a[i]}")



for number, task in enumerate(a, start=1):
    print(number, task)