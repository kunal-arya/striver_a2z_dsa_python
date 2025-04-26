# Understand recursion by print something N times

def print_n_times(n):
    if n == 0:
        return
    print_n_times(n - 1)
    print(n)


print_n_times(6)