

def print_n(n):
    if n == 0:
        return
    
    print(n)
    print_n(n - 1)

print_n(5)


# with Backtracking

def print_nb(n,i=1):
    if i > n:
        return
    
    print_nb(n,i+1)
    print(i)

print_nb(5)