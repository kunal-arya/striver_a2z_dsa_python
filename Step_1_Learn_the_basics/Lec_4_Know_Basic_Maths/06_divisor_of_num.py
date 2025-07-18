# You are given an integer n. You need to find all the divisors of n.
# Return all the divisors of n as an array or list in a sorted order.

# A number which completely divides another number is called it's divisor.

# Brute Force
# Time Complexity - O(n)

def all_divisor(n):
    temp = n
    divisor = []
    while temp > 0:
        if n % temp == 0:
            divisor.append(temp)
        temp -= 1
    return divisor[::-1]

print(all_divisor(12))

# Optimised - 1 ( Iterate till square root of the number )

def all_divisor_op(n):
    divisor = set()
    
    for i in range(1,int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.add(i)
            divisor.add(n // i)
    
    return sorted(divisor)

print(all_divisor_op(12))