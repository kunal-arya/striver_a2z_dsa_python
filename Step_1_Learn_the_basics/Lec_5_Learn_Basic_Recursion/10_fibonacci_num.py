#  Fibonacci Number - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.......

def fibo(n):
    if n <= 1:
        return n

    return fibo(n - 1) + fibo(n - 2)

print(fibo(4))

