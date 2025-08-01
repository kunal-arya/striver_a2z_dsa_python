"""
Problem: 8. String to Integer (atoi)
Platform: LeetCode
Difficulty: Medium
Topics: String, Implementation
LINK: https://leetcode.com/problems/string-to-integer-atoi/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s`.
- Output: A 32-bit signed integer.
- Constraints:
    - The length of `s` is between 0 and 200.
    - `s` consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
- Edge Cases:
    - Empty string.
    - String with only whitespaces.
    - String with a sign but no digits.
    - String with digits followed by non-digits.
    - Integer overflow (greater than 2^31 - 1 or less than -2^31).

APPROACH:
1. Ignore leading whitespaces.
2. Check for a sign ('+' or '-') and store it.
3. Read consecutive digits and build the number.
4. Stop when a non-digit character is encountered.
5. Handle integer overflow by clamping the result to the 32-bit signed integer range.
"""

# ==============================================================================
# OPTIMAL APPROACH
# ==============================================================================

def strToInt(s: str) -> int:
    """
    OPTIMAL APPROACH - Most efficient solution possible.

    Intuition:
    - We can parse the string in a single pass, keeping track of the sign and the numeric value.
    - We need to be careful about the order of operations: whitespace, sign, then digits.
    - Overflow checks are crucial and must be done at each step of building the number.

    Approach:
    1. Initialize an index `i` to 0.
    2. Skip all leading whitespaces by incrementing `i`.
    3. Check for a sign at the current position. If found, store the sign and increment `i`.
    4. Iterate through the remaining characters as long as they are digits.
    5. In each iteration, update the number by `num = num * 10 + digit`.
    6. Before updating, check if the current number is about to overflow. If it is, return the max or min integer value.
    7. Return the final number multiplied by its sign.

    Args:
        s: The input string.

    Returns:
        The converted 32-bit signed integer.

    Time Complexity: O(n), where n is the length of the string, as we iterate through the string at most once.
    Space Complexity: O(1), as we only use a few variables to store the state.
    """
    i = 0
    n = len(s)
    sign = 1
    num = 0
    
    # Constants for 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    # 1. Ignore leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # 2. Check for sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # 3. Convert number and handle overflow
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # Check for overflow before updating the number
        if num > (INT_MAX - digit) / 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        num = num * 10 + digit
        i += 1

    return sign * num


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    test_cases = {
        "42": 42,
        "   -42": -42,
        "1337c0d3": 1337,
        "0-1": 0,
        "words and 987": 0,
        "+1": 1,
        "2147483648": 2147483647,
        "-2147483649": -2147483648,
        "": 0,
        " ": 0
    }

    for s, expected in test_cases.items():
        result = strToInt(s)
        print(f"Input: '{s}', Output: {result}, Expected: {expected}")
        assert result == expected, f"Test failed for input '{s}'"

    print("🎉 All test cases passed!")