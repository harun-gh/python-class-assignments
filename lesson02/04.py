def generate(_range: int) -> list:
    array = []

    for num in range(1, _range + 1):
        if num % 3 == 0:
            array.append("aho")
        else:
            array.append(num)

    return array

result = generate(100)

print(result)