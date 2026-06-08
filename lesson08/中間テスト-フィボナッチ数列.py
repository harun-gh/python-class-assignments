def fibo(n: int)->int:
    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

# 実行テストコード
# for i in range(1, 100):
#     print(フィボナッチ(i), end=", ")