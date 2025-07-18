


# Backtracking
def print_n(n):
    if n == 0:
        return
    
    print_n(n - 1)
    print(n)


print_n(4)   

# Without Backtracking
def print_nb(n,i=1):
    if i > n:
        return
    
    print(i)
    print_nb(n, i + 1)


# print_nb(4)