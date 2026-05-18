def gcd(x: int, y: int) -> int:
    a = x % y

    if a == 0:
        return x
    else:
        return gcd(y, a)

if __name__ == "__main__":
    result = gcd(10, 2)
    print(result)