#  Sum of First N Numbers

#  Parameterised Recursion
def sum_n(n, total = 0):
    if n == 0:
        return total
    
    return sum_n(n - 1, total = total + n)

print(sum_n(3))
    

# Functional Recursion
def sum_f(n):
    if n == 0:
        return 0
    return n + sum_f(n - 1)

print(sum_f(n = 3))