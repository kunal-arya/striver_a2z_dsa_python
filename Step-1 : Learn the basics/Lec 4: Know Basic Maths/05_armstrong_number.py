# You are given an integer n. You need to check 
# whether it is an armstrong number or not. 
# Return true if it is an armstrong number, otherwise return false.

# An armstrong number is a number which is 
# equal to the sum of the digits of the number, raised to the power of the number of digits.

# Examples:
# Input: n = 153
# Output: true

# Explanation: Number of digits : 3.
# 1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 1 + 125 + 27 = 153.
# Therefore, it is an Armstrong number.

# Input: n = 12
# Output: false

# Explanation: Number of digits : 2.
# 1 ^ 2 + 2 ^ 2 = 1 + 4 = 5.
# Therefore, it is not an Armstrong number.

# OPTIMIZED - 1

def armstrong_num_1(n: str) -> bool:
    str_n = str(n)
    len_n = len(str_n)
    result: int = sum(int(digit) ** len_n for digit in str_n)
    return result == n

print(armstrong_num_1(153))

# Syntax
# sum(iterable, start)

# Parameter Values
## Parameter Description ###################################
## iterable	( Required ) -> The sequence to sum
## start ( Optional ) -> A value that is added to the return value

# OPTIMIZED - 2 ( For really big number )

def armstrong_num_2(n):
    temp = n
    len_n = len(str(n))
    result = 0

    while temp > 0:
        digit = temp % 10
        result += digit ** len_n
        temp //= 10

    return result == n


print(armstrong_num_2(153))