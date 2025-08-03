"""
Problem: 1763. Sum of Beauty of All Substrings
Platform: LeetCode
Difficulty: Medium
Topics: String, Hash Table
LINK: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s`.
- Output: The sum of the beauty of all substrings of `s`.
- Beauty of a string: The difference between the frequency of the most frequent character and the least frequent character.
- Constraints:
    - 1 <= `len(s)` <= 500
- Edge Cases:
    - String with all same characters (beauty is 0).
    - String with all different characters (beauty is 0).

APPROACH:
1. **Brute Force:** Generate all substrings. For each substring, calculate its beauty and add it to a running total. This is O(n^3).
2. **Optimized Brute Force:** We can optimize the brute-force approach by calculating the frequency map on the fly. As we extend the substring, we update the frequency map. This reduces the complexity to O(n^2).
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def sumBeautySubStrBrute(s: str) -> int:
    """
    BRUTE FORCE APPROACH

    Intuition:
    - Iterate through all possible substrings.
    - For each substring, calculate its beauty.
    - Sum up the beauties of all substrings.

    Approach:
    1. Use three nested loops.
    2. The first two loops (`i` and `j`) define the start and end of the substring.
    3. The third loop (`k`) iterates through the substring to build a frequency map.
    4. After building the map, find the max and min frequencies.
    5. Add the difference (beauty) to the total result.

    Time Complexity: O(n^3) - Three nested loops.
    Space Complexity: O(1) - The frequency map will have at most 26 keys.
    """
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            count = {}
            for k in range(i, j + 1):
                count[s[k]] = count.get(s[k], 0) + 1
            
            if count:
                maxC = max(count.values())
                minC = min(count.values())
                res += (maxC - minC)

    return res

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH
# ==============================================================================

def sumBeautySubStrOp(s: str) -> int:
    """
    OPTIMAL APPROACH

    Intuition:
    - We can avoid the third loop of the brute-force approach.
    - As we extend the substring from `i` to `j`, we can maintain the frequency map of the current substring `s[i:j+1]` incrementally.

    Approach:
    1. Use two nested loops. The outer loop `i` fixes the starting point of the substring.
    2. The inner loop `j` extends the substring by one character at a time.
    3. Maintain a frequency map for the substring `s[i:j+1]`.
    4. In each step of the inner loop, update the frequency of the new character `s[j]`.
    5. Then, calculate the beauty of the current substring `s[i:j+1]` from the updated frequency map and add it to the result.

    Time Complexity: O(n^2) - Two nested loops. Finding max/min in the frequency map takes O(26) which is constant time.
    Space Complexity: O(1) - The frequency map will have at most 26 keys.
    """
    n = len(s)
    res = 0
    for i in range(n):
        count = {}
        for j in range(i, n):
            count[s[j]] = count.get(s[j], 0) + 1

            maxC = max(count.values())
            minC = min(count.values())
            res += maxC - minC
    
    return res

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    test_cases = {
        "aabcb": 5,
        "aabcbaa": 17,
        "zzza": 0
    }

    print("--- Brute Force Approach ---")
    for s, expected in test_cases.items():
        result = sumBeautySubStrBrute(s)
        print(f"Input: '{s}', Output: {result}, Expected: {expected}")
        assert result == expected, f"Brute force test failed for input '{s}'"

    print("\n--- Optimal Approach ---")
    for s, expected in test_cases.items():
        result = sumBeautySubStrOp(s)
        print(f"Input: '{s}', Output: {result}, Expected: {expected}")
        assert result == expected, f"Optimal test failed for input '{s}'"

    print("\n🎉 All test cases passed!")