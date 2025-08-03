"""
Problem: 5. Longest Palindromic Substring
Platform: LeetCode
Difficulty: Medium
Topics: String, Dynamic Programming
LINK: https://leetcode.com/problems/longest-palindromic-substring/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s`.
- Output: The longest palindromic substring in `s`.
- Constraints:
    - 1 <= `len(s)` <= 1000
- Edge Cases:
    - Empty string (though constrained out).
    - String with one character.
    - String that is already a palindrome.

APPROACH:
1. **Brute Force:** Generate all substrings, check if each is a palindrome, and keep track of the longest one. This is O(n^3).
2. **Dynamic Programming:** Create a 2D DP table to store whether a substring `s[i:j+1]` is a palindrome. This is O(n^2) time and O(n^2) space.
3. **Expand Around Center:** Iterate through each character of the string and treat it as a potential center of a palindrome. Expand outwards to find the longest palindrome. This is O(n^2) time and O(1) space.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def isPal(s: str, i: int, j: int) -> bool:
    """Helper function to check if a substring is a palindrome."""
    left = i
    right = j
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def longestPalSubBrute(s: str) -> str:
    """
    BRUTE FORCE APPROACH

    Intuition:
    - Check every possible substring and see if it's a palindrome.
    - Keep track of the longest one found so far.

    Approach:
    1. Generate all substrings using two nested loops.
    2. For each substring, check if it's a palindrome using a helper function.
    3. If it is a palindrome and its length is greater than the max length found so far, update the result.

    Time Complexity: O(n^3) - Two loops to generate substrings (O(n^2)) and one loop to check for palindrome (O(n)).
    Space Complexity: O(1) (excluding the space for the result string).
    """
    n = len(s)
    if n == 0: return ""
    res = s[0]
    maxC = 1
    for i in range(n):
        for j in range(i, n):
            if isPal(s, i, j):
                currentLen = j - i + 1
                if maxC < currentLen:
                    res = s[i:j + 1]
                    maxC = currentLen
    return res

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH (EXPAND AROUND CENTER)
# ==============================================================================

def lonPalSubOp(s: str) -> str:
    """
    OPTIMAL APPROACH - Expand Around Center

    Intuition:
    - A palindrome is symmetric around its center. The center can be a single character (for odd length palindromes) or a pair of characters (for even length palindromes).
    - We can iterate through all possible centers and expand outwards to find the longest palindrome.

    Approach:
    1. Iterate through the string with index `i` from 0 to `n-1`.
    2. For each `i`, consider it as the center for an odd-length palindrome. Expand from `(i, i)`.
    3. For each `i`, consider `(i, i+1)` as the center for an even-length palindrome. Expand from `(i, i+1)`.
    4. A helper function can handle the expansion logic and update the longest palindrome found.

    Time Complexity: O(n^2) - We iterate through the string (O(n)), and for each character, we expand outwards which can take up to O(n) time.
    Space Complexity: O(1) (excluding the space for the result string).
    """
    n = len(s)
    if n == 0: return ""
    res = ""
    resLen = 0

    def expand(l, r):
        nonlocal res, resLen
        while l >= 0 and r < n and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1
            r += 1

    for i in range(n):
        # Odd length palindromes
        expand(i, i)
        # Even length palindromes
        expand(i, i + 1)
    
    return res

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    test_cases = {
        "babad": ["bab", "aba"], # LeetCode allows either
        "cbbd": ["bb"],
        "a": ["a"],
        "ac": ["a", "c"],
        "abbd": ["bb"]
    }

    print("--- Brute Force Approach ---")
    for s, expected_options in test_cases.items():
        result = longestPalSubBrute(s)
        print(f"Input: '{s}', Output: '{result}', Expected: one of {expected_options}")
        assert result in expected_options, f"Brute force test failed for input '{s}'"

    print("\n--- Optimal Approach ---")
    for s, expected_options in test_cases.items():
        result = lonPalSubOp(s)
        print(f"Input: '{s}', Output: '{result}', Expected: one of {expected_options}")
        assert result in expected_options, f"Optimal test failed for input '{s}'"

    print("\n🎉 All test cases passed!")