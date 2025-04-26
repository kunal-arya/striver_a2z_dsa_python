# Given an integer x, return true if x is a palindrome, and false otherwise.

def palindrome(x: int) -> bool:
    return int(str(x)[::-1]) == x


print(palindrome(121))