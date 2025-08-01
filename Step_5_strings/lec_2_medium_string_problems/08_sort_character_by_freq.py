from collections import defaultdict, Counter

"""
Problem: Sort Characters By Frequency
Given a string `s`, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple possible answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once. So 'e' must appear before both 'r' and 't'. Therefore "eert" is a valid answer. Other valid answers include "eetr".

Example 2:
Input: s = "cccaaa"
Output: "cccaaa"
Explanation: Both 'c' and 'a' appear three times. Any arrangement of "aaaccc" or "cccaaa" is also valid. Note that "aaaccc" is a valid answer, but "cacaca" is not because the same characters must be grouped together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: 'b' appears twice, 'A' and 'a' appear once. "bbaA" is also a valid answer, but "Aabb" is not. Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.
"""
# Platform: LeetCode
# Difficulty: Medium
# Topics: String, Hash Table, Sorting, Heap (Priority Queue), Bucket Sort
# LINK: https://leetcode.com/problems/sort-characters-by-frequency/

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s`.
- Output: A string where characters are sorted in decreasing order of their frequency.
          Characters with the same frequency can be in any order relative to each other,
          but characters themselves must be grouped (e.g., "aaaccc" is valid, "cacaca" is not).
- Constraints: Length between 1 and 5 * 10^5. Contains uppercase/lowercase English letters and digits.
- Edge Cases:
    - Empty string.
    - String with all unique characters.
    - String with all identical characters.
    - String with characters having the same frequency.
    - Case sensitivity (e.g., 'A' and 'a' are different).

APPROACH:
We will explore three approaches, ranging from a truly brute-force method to more optimized ones:
1. Truly Brute Force: Repeatedly find the max frequency character and build the string.
2. Optimized (Bucket Sort): Count frequencies, then use buckets to group characters by frequency.
3. Optimal (Counter + Sorted): Use `collections.Counter` for frequency, then sort the items.

TIME COMPLEXITY: Varies by approach.
SPACE COMPLEXITY: Varies by approach.
"""

# ==============================================================================
# SOLUTION 1: TRULY BRUTE FORCE APPROACH
# ==============================================================================

def sortCharFreqTrulyBrute(s: str) -> str:
    """
    TRULY BRUTE FORCE APPROACH - Repeatedly find the character with the maximum frequency.
    
    Intuition:
    - The most straightforward way to sort by frequency is to find the most frequent character,
      append it to the result, and repeat until no characters are left.
    - This involves repeatedly scanning the frequency map to find the maximum.
    
    Approach:
    1. Count the frequency of each character in the input string `s`. A `Counter` is used for convenience.
    2. Initialize an empty list `result` to store the sorted characters.
    3. Enter a `while` loop that continues as long as there are characters with positive counts in `char_counts`.
    4. Inside the loop:
       a. Initialize `max_freq = -1` and `max_char = ''`.
       b. Iterate through the `char_counts` dictionary to find the character (`char`) with the current `max_freq`.
          If frequencies are equal, prioritize alphabetically smaller characters for stable output.
       c. If a character with `max_freq > 0` is found:
          - Append `max_char` repeated `max_freq` times to the `result` list.
          - Remove `max_char` from `char_counts` (using `del`) so it's not considered again.
       d. If no character with `max_freq > 0` is found, break the loop.
    5. Join the characters in the `result` list to form the final string.
    
    Args:
        s: The input string.
    
    Returns:
        The string sorted by character frequency in decreasing order.
    
    Time Complexity: O(N + K^2)
                     - O(N) for initial frequency counting.
                     - The `while` loop runs K times (where K is the number of unique characters).
                     - Inside the loop, finding the max frequency character takes O(K) time.
                     - Thus, K * O(K) = O(K^2).
                     - Overall: O(N + K^2). This is inefficient if K is large.
    Space Complexity: O(N + K)
                      - O(K) for `char_counts` dictionary.
                      - O(N) for `result` list in the worst case (e.g., all unique characters).
                      - Overall: O(N) as N is typically much larger than K.
    """
    # 1. Count frequencies
    char_counts = Counter(s) # Using Counter for convenience, but could be manual dict

    result = []
    while char_counts: # While there are still characters with counts > 0
        max_freq = -1
        max_char = ''

        # Find the character with the maximum frequency
        for char, count in char_counts.items():
            if count > max_freq:
                max_freq = count
                max_char = char
            elif count == max_freq: # For stable output, pick alphabetically smaller if frequencies are same
                if char < max_char:
                    max_char = char

        if max_freq > 0: # If a character was found
            result.append(max_char * max_freq)
            del char_counts[max_char] # Remove this character from consideration
        else:
            break # No more characters with positive frequency
            
    return "".join(result)

# ==============================================================================
# SOLUTION 2: OPTIMIZED APPROACH (Bucket Sort)
# ==============================================================================

def sortCharFreqBrute(s: str) -> str: # Renamed from sortCharFreqOp to reflect its nature as a bucket sort
    """
    OPTIMIZED APPROACH (Bucket Sort) - Group characters by their frequency.
    
    Intuition:
    - Instead of repeatedly finding the max, we can group all characters by their frequency.
    - Then, iterate from the highest possible frequency down to 1, appending characters from each group.
    
    Approach:
    1. Count the frequency of each character in the input string `s` and store it in a dictionary `count`.
    2. Create a `buckets` dictionary (using `defaultdict(list)`) where keys are frequencies and values are lists of characters that have that frequency.
    3. Iterate through the `count` dictionary. For each character and its frequency, append the character to the corresponding frequency list in `buckets`.
    4. Initialize an empty list `res` to build the final string.
    5. Iterate from `len(s)` (maximum possible frequency) down to 1.
    6. For each frequency `i`:
       a. Check if `i` exists as a key in `buckets` (i.e., if there are characters with this frequency).
       b. If yes, iterate through the characters in `buckets[i]`. Sort these characters alphabetically to ensure stable output if multiple characters have the same frequency.
       c. Append each character `char` repeated `i` times (`char * i`) to the `res` list.
    7. Join the characters in `res` to form the final string.
    
    Args:
        s: The input string.
    
    Returns:
        The string sorted by character frequency in decreasing order.
    
    Time Complexity: O(N + K log K)
                     - O(N) for initial frequency counting.
                     - O(K) for populating buckets.
                     - O(K log K) in the worst case for sorting characters within buckets (if many characters have the same frequency).
                     - O(N) for building the result string.
                     - Overall: O(N + K log K). If K is considered a small constant (e.g., 26), this simplifies to O(N).
    Space Complexity: O(N + K)
                      - O(K) for `count` dictionary.
                      - O(K) for `buckets` dictionary.
                      - O(N) for `res` list.
                      - Overall: O(N) as N is typically much larger than K.
    """
    n = len(s)
    count = {}

    for ch in s:
        count[ch] = 1 + count.get(ch,0)
    
    buckets = defaultdict(list)
    
    for char, cnt in count.items():
        buckets[cnt].append(char)

    res = []
    # Iterate from max possible frequency (length of string) down to 1
    for i in range(len(s), 0, -1):
        if i in buckets: # Check if there are characters with this frequency
            # Sort characters alphabetically for stable output if frequencies are same
            for char in sorted(buckets[i]): 
                res.append(char * i)
    
    return "".join(res)

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (Counter + Sorted)
# ==============================================================================

def sortCharFreqOptimized(s: str) -> str: # Renamed from sortCharFreqOp to be more descriptive
    """
    OPTIMAL APPROACH (Counter + Sorted) - Concise and Pythonic.
    
    Intuition:
    - Python's `collections.Counter` is highly optimized for frequency counting.
    - Python's `sorted()` function can sort items based on a custom key, allowing
      direct sorting of character-frequency pairs.
    
    Approach:
    1. Use `collections.Counter(s)` to get a dictionary-like object where keys are characters
       and values are their frequencies.
    2. Sort the items (character, frequency pairs) from the `Counter`. The `key` for sorting
       is a lambda function `lambda item: (-item[1], item[0])`.
       - `-item[1]` sorts by frequency in *descending* order (negative of frequency).
       - `item[0]` sorts by character in *ascending* (alphabetical) order as a tie-breaker
         when frequencies are the same, ensuring stable output.
    3. Initialize an empty list `result`.
    4. Iterate through the `sorted_chars` list (which contains `(char, count)` tuples).
    5. For each `char` and `count`, append `char` repeated `count` times (`char * count`)
       to the `result` list.
    6. Join the elements in the `result` list to form the final string.
    
    Args:
        s: The input string.
    
    Returns:
        The string sorted by character frequency in decreasing order.
    
    Time Complexity: O(N + K log K)
                     - O(N) for `Counter(s)`.
                     - O(K log K) for sorting K unique character-frequency pairs.
                     - O(N) for building the result string.
                     - Overall: O(N + K log K). If K is considered a small constant, this simplifies to O(N).
                     - In practice, this is often the fastest due to highly optimized C implementations of `Counter` and `sorted`.
    Space Complexity: O(N + K)
                      - O(K) for `char_counts` (Counter object).
                      - O(K) for `sorted_chars` list.
                      - O(N) for `result` list.
                      - Overall: O(N) as N is typically much larger than K.
    """
    # 1. Count character frequencies
    char_counts = Counter(s)

    # 2. Sort characters by frequency in descending order.
    # If frequencies are the same, sort alphabetically (ascending) for stable output.
    sorted_chars = sorted(char_counts.items(), key=lambda item: (-item[1], item[0]))

    # 3. Build the result string
    result = []
    for char, count in sorted_chars:
        result.append(char * count)
    
    return "".join(result)

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

Let N be the length of the input string `s`.
Let K be the number of unique characters in `s`. K is at most 256 for ASCII, or 65536 for Unicode.

TIME COMPLEXITY:
- Truly Brute Force (`sortCharFreqTrulyBrute`): O(N + K^2)
  - Explanation: Initial frequency counting is O(N). The main loop runs K times. In each iteration, it scans the remaining K characters to find the max, taking O(K) time. Thus, K * O(K) = O(K^2).
  - This approach is generally the least efficient for larger K.

- Optimized (Bucket Sort) (`sortCharFreqBrute`): O(N + K log K)
  - Explanation: O(N) for frequency counting. O(K) for populating buckets. The dominant factor comes from sorting characters within buckets, which in the worst case could be O(K log K) if all unique characters have the same frequency. Building the result is O(N).
  - This is a very efficient approach, especially when K is small.

- Optimal (Counter + Sorted) (`sortCharFreqOptimized`): O(N + K log K)
  - Explanation: `Counter(s)` is O(N). Sorting K items is O(K log K). Building the result is O(N).
  - Asymptotically, this has the same complexity as the bucket sort. However, due to highly optimized C implementations of `Counter` and `sorted` in Python, this approach often performs best in practice.

SPACE COMPLEXITY:
- Truly Brute Force (`sortCharFreqTrulyBrute`): O(N + K)
  - Explanation: O(K) for the `char_counts` dictionary and O(N) for the `result` list.

- Optimized (Bucket Sort) (`sortCharFreqBrute`): O(N + K)
  - Explanation: O(K) for the `count` and `buckets` dictionaries, and O(N) for the `res` list.

- Optimal (Counter + Sorted) (`sortCharFreqOptimized`): O(N + K)
  - Explanation: O(K) for the `char_counts` (Counter object) and `sorted_chars` list, and O(N) for the `result` list.

TRADE-OFFS:
- The **Truly Brute Force** is conceptually simple but highly inefficient for larger alphabets (larger K) due to its O(K^2) component. It's mainly for demonstrating a less optimized approach.

- The **Optimized (Bucket Sort)** approach is very efficient. It leverages the fact that frequencies are bounded (by N) to distribute characters into "buckets." It's a strong contender for the best solution.

- The **Optimal (Counter + Sorted)** approach is often the most preferred in Python due to its conciseness, readability, and excellent practical performance. While its asymptotic complexity is the same as bucket sort, the underlying C implementations make it very fast. It's a great example of leveraging built-in tools effectively.

When to use which:
- **Truly Brute Force:** Avoid for practical applications; useful for understanding fundamental inefficiencies.
- **Optimized (Bucket Sort):** Excellent performance, especially if you want to implement the logic manually or if `K` is very large and `N` is relatively small.
- **Optimal (Counter + Sorted):** Highly recommended for its balance of readability, conciseness, and practical efficiency in Python.
"""
