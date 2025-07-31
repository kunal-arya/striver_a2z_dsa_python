"""
Problem: Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Platform: LeetCode
Difficulty: Medium
Topics: String, Two Pointers
LINK: https://leetcode.com/problems/reverse-words-in-a-string/
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A string `s` containing words separated by spaces.
- Output: A string with the words reversed.
- Constraints: `1 <= s.length <= 10^4`, `s` contains printable ASCII characters.
- Edge Cases: Leading/trailing spaces, multiple spaces between words.

APPROACH:
1. Reverse the entire string.
2. Iterate through the reversed string, identify each word.
3. Reverse each word back to its original form.
4. Append the corrected word to the result string with a single space.

TIME COMPLEXITY: O(n), where n is the length of the string.
SPACE COMPLEXITY: O(n) for the result string.
"""

# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def reverseWords(s: str) -> str:
    """
    BRUTE FORCE APPROACH - Reverses the entire string, then reverses each word.
    
    Intuition:
    - Reversing the whole string places words in the correct final order, but the letters of each word are backward.
    - A second pass to reverse each word individually corrects the letters.
    
    Approach:
    1. Reverse the input string `s`.
    2. Initialize an empty string `ans` to store the result.
    3. Iterate through the reversed string with a pointer `i`.
    4. For each word, build it by appending characters until a space is found.
    5. If a word has been formed, reverse it and append it to `ans` with a leading space.
    6. Skip over any spaces.
    7. Return `ans`, removing any leading space.
    
    Args:
        s: The input string.
    
    Returns:
        The string with words reversed.
    
    Time Complexity: O(n) because of the multiple passes.
    Space Complexity: O(n) for storing the reversed string and the answer.
    """
    
    # STEP 1: Reverse the entire string
    s = s[::-1]
    
    n = len(s)
    ans = ""
    i = 0
    
    # STEP 2: Iterate through the reversed string
    while i < n:
        word = ""
        # STEP 3: Build each word
        while i < n and s[i] != " ":
            word += s[i]
            i += 1
        
        # STEP 4: Reverse the word and append to result
        if len(word) > 0:
            word = word[::-1]
            ans += " " + word
        
        # STEP 5: Skip spaces
        i += 1
        
    return ans.strip()

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Example usage
    test_string = "  hello world  "
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{reverseWords(test_string)}'")
