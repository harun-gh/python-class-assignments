def eratosthenes(n: int) -> list[int]:
    array = [True] * (n + 1)

    array[0] = array[1] = False

    for i in range(2, n + 1):
        if array[i] == True:
            for k in range(i*2, n+1, i):
                array[k] = False
    
    for i, boolean in enumerate(array):
        if boolean:
            print(i, end=" ")

eratosthenes(100)