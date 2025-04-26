# You are given an integer n. 
# You need to check if the number is prime or not. 
# Return true if it is a prime number, otherwise return false.
# A prime number is a number which has no divisors except 1 and itself.

# Examples:
# Input: n = 5
# Output: true

# Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

# Input: n = 8
# Output: false

# Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number.

# Brute Force

def prime_num(n):
    for i in range(1,n + 1):
        if n % 1 == 0 and i != 1 and i != n:
            return False
    return True

print(prime_num(6))

# Optimised Code

def prime_num_op(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(prime_num_op(13))