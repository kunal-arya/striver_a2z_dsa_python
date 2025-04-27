# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit 
# integer range [-231, 231 - 1], then return 0.


def reverse_num(x: int) -> int:
    rev = 0
    if x >= 0:
        rev = int(str(x)[::-1])
    else:
        rev = int(str(x)[1:][::-1]) * -1

    if rev > 2**31 - 1 or rev < -2**31:
        return 0
    return rev


print(reverse_num(123))