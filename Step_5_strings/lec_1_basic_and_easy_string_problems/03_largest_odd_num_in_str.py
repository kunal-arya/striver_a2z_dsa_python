"""
Problem: You are given a string `num` representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of `num`, or an empty string "" if no odd integer exists.
Platform: LeetCode
Difficulty: Easy
Topics: String, Greedy
LINK: https://leetcode.com/problems/largest-odd-number-in-string/
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `num` representing an integer.
- Output: The largest odd integer substring of `num`.
- Constraints: `1 <= num.length <= 10^5`, `num` consists of digits only and does not contain leading zeros.
- Edge Cases: No odd digits in the string.

APPROACH:
1. An integer is odd if its last digit is odd.
2. To get the largest odd number, we need the longest possible substring ending with an odd digit.
3. This means we should find the rightmost odd digit in the string.
4. The substring from the beginning of the string up to and including this rightmost odd digit will be the largest odd number.

TIME COMPLEXITY: O(n), where n is the length of the string.
SPACE COMPLEXITY: O(1) if slicing creates a view, O(n) if it creates a copy.
"""

# =============================================================================
# SOLUTION 1: OPTIMAL APPROACH
# =============================================================================

def LargestOddNum(s: str) -> str:
    """
    OPTIMAL APPROACH - Find the rightmost odd digit and take the prefix.
    
    Intuition:
    - The largest odd number must be a prefix of the original number ending in an odd digit.
    - By finding the last odd digit, we ensure the resulting number is the longest and therefore largest possible.
    
    Approach:
    1. Iterate from the end of the string towards the beginning.
    2. Check if the current digit is odd.
    3. If it is, the substring from the start up to this digit is the answer.
    4. If no odd digit is found, return an empty string.
    
    Args:
        s: The input string representing a number.
    
    Returns:
        The largest odd number substring.
    
    Time Complexity: O(n) in the worst case (scan the whole string).
    Space Complexity: O(1) as we are just returning a slice/substring.
    """
    
    # Iterate from the end of the string
    for i in range(len(s) - 1, -1, -1):
        # Check if the digit is odd
        if int(s[i]) % 2 != 0:
            # Return the substring from the beginning to this odd digit
            return s[:i+1]
    
    # If no odd digit is found, return empty string
    return ""

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Example usage
    test_string = "52"
    print(f"Input: '{test_string}'")
    print(f"Largest odd number: '{LargestOddNum(test_string)}'")
    
    test_string_2 = "4206"
    print(f"Input: '{test_string_2}'")
    print(f"Largest odd number: '{LargestOddNum(test_string_2)}'")