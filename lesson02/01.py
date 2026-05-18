# from random import random;

def factorial(n: int) -> int | factorial:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

j = 4
k = factorial(j)
print(f'{j}! = {k}')

# if __name__ == "__main__":
#     factorial(random() * 10)