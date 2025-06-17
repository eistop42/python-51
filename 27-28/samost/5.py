s = 'a1s2d3f4g5h6j7k8l9oo'
count = 0
for i in range(len(s)):
    if s[i].isdigit()!=True:
        count +=1
print(count)

