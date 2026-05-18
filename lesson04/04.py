numbers = [4, 10, 15]
sum = 0

for num in numbers:
    if num%2 == 0:
        v = 1
    elif num%3 == 0:
        v = 2
    elif num%5 == 0:
        v = 3
    else:
        v = 0

    sum = sum + v

print(sum)