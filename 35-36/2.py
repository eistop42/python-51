
def find_sum(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count = count + number
    return count

print(find_sum([3, 4, 5, -4]))
print(sum([3, 4, 5, -4]))