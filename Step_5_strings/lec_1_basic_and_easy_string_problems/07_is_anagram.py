"""
Problem: Valid Anagram
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

# LINK: https://leetcode.com/problems/valid-anagram/

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: Two strings, `s` and `t`.
- Output: A boolean (`true` if `t` is an anagram of `s`, `false` otherwise).
- Constraints: Lengths between 1 and 5 * 10^4. Consist of lowercase English letters.
- Edge Cases:
    - Strings of different lengths (must return `false`).
    - Empty strings (if both empty, `true`; if one empty and other not, `false`).
    - Strings with duplicate characters.
    - Strings with all unique characters.

APPROACH:
We will explore three approaches:
1. Brute Force: Character-by-character checking and removal.
2. Better Approach: Using frequency maps (hashing).
3. Optimal Approach: Sorting both strings.

TIME COMPLEXITY: Varies by approach.
SPACE COMPLEXITY: Varies by approach.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def isAnagramBrute(s: str, t: str) -> bool:
    """
    BRUTE FORCE APPROACH - Character-by-character checking and removal.
    
    Intuition:
    - If `t` is an anagram of `s`, then every character in `s` must be present in `t`
      with the same frequency.
    - We can iterate through `s`, and for each character, try to find and "remove" it
      from `t`. If we can't find a character, or if `t` is not empty at the end,
      it's not an anagram.
    
    Approach:
    1. Check if lengths of `s` and `t` are different. If so, return `False` immediately.
    2. Convert `t` to a list of characters (`t_list`) to allow for efficient removal.
    3. Iterate through each character `char_s` in string `s`.
    4. For each `char_s`, iterate through `t_list` to find a matching character `char_t`.
    5. If a match is found, remove `char_t` from `t_list` and set a `found` flag to `True`, then `break` the inner loop.
    6. If `found` is `False` after checking all characters in `t_list` for `char_s`, then `char_s` is not in `t_list`, so return `False`.
    7. If the outer loop completes, it means all characters in `s` were found and removed from `t_list`. Return `True`.
    
    Args:
        s: The first string.
        t: The second string.
    
    Returns:
        True if `t` is an anagram of `s`, False otherwise.
    
    Time Complexity: O(N*M) in the worst case, where N is len(s) and M is len(t).
                     This is because for each character in `s` (N), we might iterate
                     through almost all characters in `t` (M), and `list.pop(i)`
                     takes O(M) time. So, it's closer to O(N*M) or O(N^2) if N=M.
    Space Complexity: O(M) to store `t_list`.
    """
    if len(s) != len(t):
        return False

    t_list = list(t)

    for char_s in s:
        found = False
        for i, char_t in enumerate(t_list):
            if char_s == char_t:
                t_list.pop(i)  # Remove the found character
                found = True
                break  # Move to the next character in s
        
        if not found:
            return False
            
    return True

# ==============================================================================
# SOLUTION 2: BETTER APPROACH (Hashing/Frequency Map)
# ==============================================================================

def isAnagramBetter(s: str, t: str) -> bool:
    """
    BETTER APPROACH - Improved efficiency using frequency maps (hash tables).
    
    Intuition:
    - If two strings are anagrams, they must have the exact same count of each character.
    - We can count the frequency of each character in both strings and then compare these counts.
    
    Approach:
    1. Check if lengths of `s` and `t` are different. If so, return `False`.
    2. Initialize two dictionaries, `countS` and `countT`, to store character frequencies for `s` and `t` respectively.
    3. Iterate through both strings simultaneously (since they have the same length). For each character, increment its count in the respective dictionary.
       `countS[s[i]] = countS.get(s[i], 0) + 1`
       `countT[t[i]] = countT.get(t[i], 0) + 1`
    4. Iterate through the keys (characters) in `countS`. For each character `c`:
       - Check if `countS[c]` is equal to `countT.get(c, 0)`. `get(c, 0)` handles cases where a character from `s` might not be in `t`.
       - If counts don't match, return `False`.
    5. If the loop completes, it means all characters in `s` have matching frequencies in `t`. Return `True`.
    
    Args:
        s: The first string.
        t: The second string.
    
    Returns:
        True if `t` is an anagram of `s`, False otherwise.
    
    Time Complexity: O(N) where N is the length of the strings.
                     We iterate through the strings once to build frequency maps (O(N)).
                     Then, we iterate through at most 26 (for lowercase English) or K unique characters (O(K)) to compare counts.
                     Since K is constant or much smaller than N, the dominant factor is O(N).
    Space Complexity: O(K) where K is the number of unique characters (at most 26 for lowercase English letters).
                      This is for storing the two frequency dictionaries.
    """
    n = len(s)
    m = len(t)

    if n != m:
        return False
    
    countS = {}
    countT = {}

    for i in range(n):
        countS[s[i]] = countS.get(s[i], 0) + 1
        countT[t[i]] = countT.get(t[i], 0) + 1

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    
    return True

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (Sorting)
# ==============================================================================

def isAnagramOp(s: str, t: str) -> bool:
    """
    OPTIMAL APPROACH - Sorting both strings.
    
    Intuition:
    - If two strings are anagrams of each other, then sorting both strings alphabetically
      will result in identical strings.
    
    Approach:
    1. Sort string `s`.
    2. Sort string `t`.
    3. Compare the sorted versions of `s` and `t`. If they are equal, return `True`; otherwise, return `False`.
    
    Args:
        s: The first string.
        t: The second string.
    
    Returns:
        True if `t` is an anagram of `s`, False otherwise.
    
    Time Complexity: O(N log N) where N is the length of the strings.
                     This is dominated by the sorting operation. Python's `sorted()`
                     uses Timsort, which is O(N log N).
    Space Complexity: O(N) for storing the sorted copies of the strings.
    """
    return sorted(s) == sorted(t) 

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

TIME COMPLEXITY:
- Brute Force (`isAnagramBrute`): O(N*M) or O(N^2) if N=M.
  - Explanation: Nested loops where the inner loop iterates through `t_list` (up to M elements) and `list.pop()` takes O(M) time. This is repeated N times.
- Better Approach (`isAnagramBetter`): O(N)
  - Explanation: Two passes over the strings to build frequency maps (O(N)). A third pass over the unique characters (O(K), where K is small constant like 26) to compare counts. Dominant factor is O(N).
- Optimal Approach (`isAnagramOp`): O(N log N)
  - Explanation: The time complexity is dominated by the sorting operation, which is typically O(N log N) for comparison-based sorts.

SPACE COMPLEXITY:
- Brute Force (`isAnagramBrute`): O(M)
  - Explanation: A list `t_list` is created from string `t`.
- Better Approach (`isAnagramBetter`): O(K)
  - Explanation: Two hash maps (`countS`, `countT`) are used to store character frequencies. The maximum number of entries in these maps is limited by the size of the alphabet (e.g., 26 for lowercase English letters).
- Optimal Approach (`isAnagramOp`): O(N)
  - Explanation: The `sorted()` function typically creates new lists/strings to store the sorted versions, which can take O(N) space.

TRADE-OFFS:
- The **Brute Force** is the simplest to conceptualize but the least efficient in terms of time complexity.
- The **Better Approach (Hashing)** offers optimal time complexity (O(N)) for this problem, making it very efficient, especially for large strings. Its space complexity is constant (O(K)) relative to the input size N, which is excellent.
- The **Optimal Approach (Sorting)** is very concise and easy to implement in Python. Its time complexity is O(N log N), which is generally slower than O(N) but still efficient enough for many practical purposes. Its space complexity is O(N).

When to use which:
- **Brute Force:** Rarely recommended for production code due to inefficiency, but good for initial understanding.
- **Better (Hashing):** Preferred for performance when N is large, as it achieves linear time complexity.
- **Optimal (Sorting):** A good balance of readability, conciseness, and reasonable performance. Often chosen in interviews for its simplicity if O(N log N) is acceptable.
"""

# Example Usage:
print(isAnagramBrute("anagram", "nagaram")) # True
print(isAnagramBrute("rat", "car"))       # False
print(isAnagramBetter("anagram", "nagaram")) # True
print(isAnagramBetter("rat", "car"))       # False
print(isAnagramOp("anagram", "nagaram")) # True
print(isAnagramOp("rat", "car"))       # False