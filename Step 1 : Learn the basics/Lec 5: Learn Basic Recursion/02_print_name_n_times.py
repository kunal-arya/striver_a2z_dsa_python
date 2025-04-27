

def print_name_n_times(n):
    if n == 0:
        return
    print("name")
    print_name_n_times(n - 1)


print_name_n_times(3)