def is_prime(num: int) -> bool:
    div: int = 2

    if num < div:
        return False
    else:
        while num > div:
            if num%div == 0:
                return False
            else:
                div = div + 1

        return True

for n in range(2, 100):
    if is_prime(n):
        print(n, end=" ")