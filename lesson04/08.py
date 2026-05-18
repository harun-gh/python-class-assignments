def eratosthenes(n: int) -> list(int):
    array = bytearray(b"\x01") * (n + 1)
    array[0:2] = b"\x00\x00"

    i = 2

    while i * i <= n:
        if array[i]:
            array[i * i : n + 1 : i] = b"\x00" * (((n - i * i) // i) + 1)

        i += 1

    for i, boolean in enumerate(array):
        if boolean:
            print(i, end=" ")

eratosthenes(1_0000_0000)