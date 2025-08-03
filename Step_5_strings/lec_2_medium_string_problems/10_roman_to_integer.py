"""
Problem: Roman to Integer
Given a roman numeral, convert it to an integer.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
# Platform: LeetCode
# Difficulty: Easy
# Topics: String, Hash Table, Math
# LINK: https://leetcode.com/problems/roman-to-integer/

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s` representing a Roman numeral.
- Output: An integer equivalent of the Roman numeral.
- Constraints: Length between 1 and 15. Contains valid Roman numeral characters. Guaranteed to be valid and in range [1, 3999].
- Edge Cases:
    - Standard additive cases (e.g., "III", "LVIII").
    - Subtractive cases (e.g., "IV", "IX", "XL", "XC", "CD", "CM").
    - Combinations of additive and subtractive cases (e.g., "MCMXCIV").

APPROACH (Roman to Integer):
1. Map Roman symbols to their integer values.
2. Iterate through the Roman numeral string from left to right.
3. Apply the rule: if a symbol's value is less than the next symbol's value, subtract it; otherwise, add it.

"""

# ==============================================================================
# SOLUTION 1: ROMAN TO INTEGER (Optimal Approach)
# ==============================================================================

# Function to change from roman to int
def romanToInt(s: str) -> int:
    """
    OPTIMAL APPROACH - Iterating through the string and applying Roman numeral rules.
    
    Intuition:
    - Roman numerals are generally read from left to right, adding values.
    - The key exception is when a smaller value precedes a larger value (e.g., IV, IX),
      in which case the smaller value is subtracted from the larger one.
    - By iterating from left to right, we can check if the current symbol's value
      is less than the next symbol's value. If it is, we subtract the current value;
      otherwise, we add it.
    
    Approach:
    1. Create a dictionary `roman` to map each Roman symbol to its integer value.
    2. Initialize `res` (result) to 0.
    3. Iterate through the input string `s` from index `i = 0` to `n-1` (where `n` is the length of `s`).
    4. In each iteration, check if `i + 1` is within the bounds of the string AND if the value of `s[i]`
       is less than the value of `s[i + 1]`.
       - If true (subtractive case, e.g., "IV"): Subtract `roman[s[i]]` from `res`.
       - If false (additive case, e.g., "VI" or last character): Add `roman[s[i]]` to `res`.
    5. Return the final `res`.
    
    Args:
        s: The Roman numeral string.
    
    Returns:
        The integer equivalent of the Roman numeral.
    
    Time Complexity: O(N) where N is the length of the input string `s`.
                     We iterate through the string once. Dictionary lookups are O(1).
    Space Complexity: O(1)
                      The `roman` dictionary has a fixed size (7 entries).
    """
    roman = {
        "I" :1, "V" :5, "X" :10, "L" :50, "C" :100, "D" :500, "M" :1000
    }

    n = len(s)
    res = 0

    for i in range(n):
        if i + 1 < n and roman[s[i]] < roman[s[i + 1]]:
            res -= roman[s[i]]
        else:
            res += roman[s[i]]

    return res

# ==============================================================================
# PROBLEM ANALYSIS (Integer to Roman)
# ==============================================================================

"""
PROBLEM BREAKDOWN (Integer to Roman):
- Input: An integer `num`.
- Output: A string representing the Roman numeral equivalent.
- Constraints: `num` is guaranteed to be in the range [1, 3999].
- Edge Cases:
    - Numbers requiring subtractive notation (4, 9, 40, 90, 400, 900).
    - Numbers requiring combinations of symbols.

APPROACH (Integer to Roman - Greedy):
1. Create a list of Roman symbol-value pairs, sorted in descending order of value, including subtractive combinations.
2. Iterate through this list. For each pair, repeatedly append the Roman symbol to the result and subtract its value from the number until the number is smaller than the current value.
"""

# ==============================================================================
# SOLUTION 2: INTEGER TO ROMAN (Greedy Approach)
# ==============================================================================

# Function to change from int to roman
def intToRoman(num: int) -> str:
    """
    GREEDY APPROACH - Iterating through predefined Roman numeral values from largest to smallest.
    
    Intuition:
    - To convert an integer to a Roman numeral, we can greedily subtract the largest possible Roman numeral value
      from the number until it becomes zero.
    - This requires a predefined list of Roman numeral symbols and their corresponding integer values,
      including the special subtractive cases (e.g., 900 for "CM", 400 for "CD") to ensure correctness.
    
    Approach:
    1. Create a list of tuples `roman`, where each tuple is `(symbol, value)`, sorted in descending order of `value`.
       This list must include both standard symbols (M, D, C, L, X, V, I) and subtractive combinations (CM, CD, XC, XL, IX, IV).
    2. Initialize an empty string `res` to build the Roman numeral.
    3. Iterate through the `roman` list.
    4. For each `(sym, val)` pair:
       a. While the input `num` is greater than or equal to `val`:
          - Append `sym` to `res`.
          - Subtract `val` from `num`.
    5. Return the final `res`.
    
    Args:
        num: The integer to convert.
    
    Returns:
        The Roman numeral string.
    
    Time Complexity: O(1)
                     The number of Roman numeral symbols and combinations is fixed (13).
                     The `while` loop for each symbol runs a maximum of 3 times (e.g., "III", "XXX", "CCC", "MMM").
                     Therefore, the number of operations is constant, independent of the input `num` (within the given constraints).
    Space Complexity: O(1)
                      The `roman` list has a fixed size. The `res` string grows up to a fixed maximum length (e.g., 15 for 3999).
    """
    roman = [
        ["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10],
        ["XL", 40], ["L", 50], ["XC", 90], ["C", 100],
        ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]
    ]
    # Sort in descending order of value for the greedy approach
    roman.sort(key=lambda x: x[1], reverse=True)

    res = ""
    for sym, val in roman:
        if num == 0: # Optimization: if num becomes 0, no need to continue
            break
        while num >= val:
            res += sym
            num -= val
    
    return res

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

ROMAN TO INTEGER (`romanToInt`):
TIME COMPLEXITY: O(N)
- Explanation: The algorithm iterates through the input string `s` once. Each character lookup in the `roman` dictionary is an O(1) operation because the dictionary size is fixed and small. Therefore, the total time complexity is directly proportional to the length of the input string.

SPACE COMPLEXITY: O(1)
- Explanation: The `roman` dictionary stores a fixed number of key-value pairs (7 symbols). The space used does not grow with the input size.

INTEGER TO ROMAN (`intToRoman`):
TIME COMPLEXITY: O(1)
- Explanation: The number of Roman numeral symbols and their combinations is fixed (13). The algorithm iterates through this fixed list. For each symbol, it performs a `while` loop that subtracts the value. Since the maximum input number is 3999, the maximum number of subtractions is also constant (e.g., 3 'M's, 1 'CM', 1 'XC', 1 'IV' for 3994). Thus, the total number of operations is constant, independent of the input `num` within the given constraints.

SPACE COMPLEXITY: O(1)
- Explanation: The `roman` list has a fixed size (13 entries). The `res` string grows, but its maximum length is also fixed (e.g., 15 characters for 3999, "MMMCMXCIX"). Therefore, the space used does not grow with the input number.

TRADE-OFFS:
- Both functions are highly optimized for their respective tasks, achieving optimal time and space complexities given the nature of Roman numerals. There are no significant trade-offs to consider between different approaches for these specific problems, as the greedy/iterative approaches are standard and efficient.
"""