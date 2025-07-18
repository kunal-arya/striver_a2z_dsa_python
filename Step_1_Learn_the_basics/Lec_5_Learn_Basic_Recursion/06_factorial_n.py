# Factorial N


def fac_n(n):
    if n == 1:
        return 1
    
    return n * fac_n(n - 1)


print(fac_n(5))