"""
Problem: Count Substrings with Exactly K Distinct Characters
Platform: GeeksforGeeks
Difficulty: Medium
Topics: String, Sliding Window, Hashing
LINK: https://www.geeksforgeeks.org/problems/count-substrings-with-exactly-k-distinct-characters/1
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s` and an integer `k`.
- Output: The number of substrings of `s` with exactly `k` distinct characters.
- Constraints:
    - 1 <= `len(s)` <= 10^5
    - 1 <= `k` <= 26
- Edge Cases:
    - Empty string.
    - `k` is 0.
    - `k` is greater than the number of distinct characters in the string.

APPROACH:
1. A brute-force approach would be to generate all substrings, and for each substring, count the number of distinct characters. This would be O(n^3) or O(n^2) with optimization.
2. A better approach is to use a sliding window. The core idea is to find the number of substrings with at most `k` distinct characters and subtract the number of substrings with at most `k-1` distinct characters. This gives us the number of substrings with exactly `k` distinct characters.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def countNoOfSubstringsBrute(s: str, k: int) -> int:
    """
    BRUTE FORCE APPROACH - Most straightforward solution.

    Intuition:
    - Generate all possible substrings.
    - For each substring, count the number of unique characters.
    - If the count of unique characters is equal to k, increment a counter.

    Approach:
    1. Initialize a counter `count` to 0.
    2. Use two nested loops to generate all substrings.
    3. The outer loop `i` iterates from 0 to `n-1` (start of substring).
    4. The inner loop `j` iterates from `i` to `n-1` (end of substring).
    5. For each substring `s[i:j+1]`, use a hash map (or a set) to count the distinct characters.
    6. If the number of distinct characters is `k`, increment `count`.
    7. If the number of distinct characters exceeds `k`, we can break the inner loop and start the next substring, as any further extension of the current substring will also have more than `k` distinct characters.

    Args:
        s: The input string.
        k: The number of distinct characters.

    Returns:
        The number of substrings with exactly k distinct characters.

    Time Complexity: O(n^2) because of the nested loops. In the inner loop, we are also maintaining a frequency map, which takes at most O(26) which is constant time.
    Space Complexity: O(k) or O(26) for the frequency map, which is O(1).
    """
    n = len(s)
    count = 0

    for i in range(n):
        freq = {}
        for j in range(i, n):
            ch = s[j]
            freq[ch] = freq.get(ch, 0) + 1

            if len(freq) == k:
                count += 1
            elif len(freq) > k:
                break
    
    return count

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH
# ==============================================================================

def countAtMostK(s: str, k: int) -> int:
    """
    Helper function to count substrings with at most k distinct characters using a sliding window.

    Intuition:
    - Use a sliding window to efficiently count substrings with at most `k` distinct characters.
    - The window `[left, right]` will always contain at most `k` distinct characters.
    - For each valid window ending at `right`, all substrings ending at `right` within that window are valid. The number of such substrings is `right - left + 1`.

    Approach:
    1. Initialize `left = 0`, `right = 0`, `count = 0`, and a frequency map `freq`.
    2. Expand the window by moving `right`.
    3. Add the character `s[right]` to the frequency map.
    4. If the number of distinct characters in the window (`len(freq)`) exceeds `k`, shrink the window from the left by moving `left` forward.
    5. While shrinking, decrement the frequency of `s[left]` and remove it from the map if its frequency becomes 0.
    6. After ensuring the window is valid (has at most `k` distinct characters), add the size of the window (`right - left + 1`) to the total count.
    7. Repeat until `right` reaches the end of the string.

    Args:
        s: The input string.
        k: The maximum number of distinct characters allowed.

    Returns:
        The number of substrings with at most k distinct characters.
    """
    if k < 0: return 0
    n = len(s)
    count = 0
    left = 0
    freq = {}
    for right in range(n):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        count += (right - left + 1)
    
    return count

def countNoOfSubStringsOp(s: str, k: int) -> int:
    """
    OPTIMAL APPROACH - Using the principle of inclusion-exclusion.

    Intuition:
    - The number of substrings with exactly `k` distinct characters is equal to:
      (number of substrings with at most `k` distinct characters) -
      (number of substrings with at most `k-1` distinct characters).
    - This allows us to use the efficient sliding window approach twice.

    Approach:
    1. Call the `countAtMostK` helper function with `k`.
    2. Call the `countAtMostK` helper function with `k-1`.
    3. Return the difference between the two results.

    Args:
        s: The input string.
        k: The exact number of distinct characters required.

    Returns:
        The number of substrings with exactly k distinct characters.

    Time Complexity: O(n) because we are calling `countAtMostK` twice, and each call takes O(n) time.
    Space Complexity: O(k) or O(26) for the frequency map, which is O(1).
    """
    return countAtMostK(s, k) - countAtMostK(s, k - 1)

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    test_cases = {
        ("aabacbebebe", 3): 14, # From GFG
        ("aba", 2): 2,
        ("aa", 1): 3,
        ("abc", 2): 2,
        ("abcde", 5): 1,
        ("abac", 2): 4
    }

    print("--- Brute Force Approach ---")
    for (s, k), expected in test_cases.items():
        result = countNoOfSubstringsBrute(s, k)
        print(f"Input: s='{s}', k={k}, Output: {result}, Expected: {expected}")
        assert result == expected, f"Brute force test failed for s='{s}', k={k}"

    print("\n--- Optimal Approach ---")
    for (s, k), expected in test_cases.items():
        result = countNoOfSubStringsOp(s, k)
        print(f"Input: s='{s}', k={k}, Output: {result}, Expected: {expected}")
        assert result == expected, f"Optimal test failed for s='{s}', k={k}"

    print("\n🎉 All test cases passed!")