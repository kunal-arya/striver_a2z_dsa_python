"""
Problem: 1021. Remove Outermost Parentheses
Platform: LeetCode
Difficulty: Easy
Topics: String, Stack
LINK: https://leetcode.com/problems/remove-outermost-parentheses/description/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A valid parentheses string `s`. For example, "(()())(())".
- Output: The string `s` after removing the outermost parentheses of every primitive string in its primitive decomposition. For "(()())(())", the decomposition is "(()())" + "(())". After removing outer parentheses, we get "()()" + "()" = "()()()".
- Constraints: 1 <= s.length <= 10^5, s[i] is either '(' or ')'. `s` is a valid parentheses string.
- Edge Cases: 
    - A string with a single primitive component, e.g., "(())". Output: "()".
    - A string with multiple simple primitive components, e.g., "()()". Output: "".
"""

# ==============================================================================
# SOLUTION 1: BETTER APPROACH (Using Slicing)
# ==============================================================================

def removeOutermostParanthesis(s: str) -> str:
    """
    BETTER APPROACH - Identifies primitive components and slices them.
    
    Intuition:
    - A primitive valid parentheses string has a balance of 0 (where '(' is +1 and ')' is -1) only at its beginning and end.
    - We can iterate through the string, keeping track of the balance. When the balance returns to 0, we have identified a primitive component.
    - We can then slice this component to remove its first and last characters and add the result to our list.
    
    Approach:
    1. Initialize an empty list `res` to store the inner parts of primitive strings.
    2. Use a `start` variable to mark the beginning of the current primitive component.
    3. Use a `balance` variable to track the count of open vs. closed parentheses.
    4. Iterate through the string with an index `i`.
    5. Increment `balance` for '(' and decrement for ')'.
    6. If `balance` becomes 0, it signifies the end of a primitive component.
    7. Slice the string from `start + 1` to `i` to get the content inside the outermost parentheses.
    8. Append this slice to the `res` list.
    9. Update `start` to `i + 1` to mark the beginning of the next component.
    10. Finally, join the elements of `res` to form the final string.
    
    Time Complexity: O(N), where N is the length of the string. We iterate through the string once. String slicing and joining operations also take a total of O(N) time.
    Space Complexity: O(N), as the `res` list can store intermediate substrings which, in the worst case, can have a total length proportional to N.
    """
    res = []
    start = 0
    balance = 0

    for i, ch in enumerate(s):
        if ch == "(":
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            res.append(s[start + 1:i])
            start = i + 1
    
    return "".join(res)

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH (Constant Space)
# ==============================================================================

def removeOutermostParanthesis_optimal(s: str) -> str:
    """
    OPTIMAL APPROACH - Builds the result string directly without intermediate slicing.
    
    Intuition:
    - Instead of identifying and slicing substrings, we can build the result character by character.
    - We should include a parenthesis in our result only if it is NOT part of the "outermost" layer of a primitive component.
    - An opening parenthesis `(` is "outer" if it's the very first one in a primitive part. We can identify this by checking our open parenthesis counter *before* processing the character.
    - A closing parenthesis `)` is "outer" if it's the very last one. We can identify this by checking the counter *after* processing the character.

    Why this is more optimal than the slicing approach:
    - While both approaches have the same asymptotic space complexity (O(K) for the output string), this method is more efficient in practice.
    - The slicing method (`res.append(s[start + 1:i])`) creates a new string object in memory for every primitive component it finds. This involves repeated memory allocation and copying of character data, which can be slow.
    - This optimal method avoids creating intermediate substrings. It appends single characters (`res.append(char)`) to a list, which is a much more lightweight and faster operation. It only builds the final string once at the very end with `.join()`. This reduces memory allocation overhead and avoids unnecessary data copying.
    
    Approach:
    1. Initialize an empty list `res` to build the result and a counter `open_parentheses` to 0.
    2. Iterate through each character of the string.
    3. If the character is '(':
        - If `open_parentheses` is greater than 0, it means we are already inside a primitive component, so this '(' is not an outermost one. Append it to `res`.
        - Increment `open_parentheses`.
    4. If the character is ')':
        - Decrement `open_parentheses`.
        - If `open_parentheses` is still greater than 0, it means this ')' is not the final closing parenthesis of the primitive component. Append it to `res`.
    5. Join the characters in `res` to get the final string.
    
    Time Complexity: O(N), as we perform a single pass through the string.
    Space Complexity: O(K), where K is the length of the result string. This is optimal because we need to construct the result string anyway. The auxiliary space used besides the result itself is O(1).
    """
    res = []
    open_parentheses = 0
    for char in s:
        if char == '(':
            if open_parentheses > 0:
                res.append(char)
            open_parentheses += 1
        else:
            open_parentheses -= 1
            if open_parentheses > 0:
                res.append(char)
    return "".join(res)

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

s = "(()())(())"
print(f"Input string: {s}")
print(f"Result (Better Approach): {removeOutermostParanthesis(s)}")
print(f"Result (Optimal Approach): {removeOutermostParanthesis_optimal(s)}")

s = "(()())(())(()(()))"
print(f"\nInput string: {s}")
print(f"Result (Better Approach): {removeOutermostParanthesis(s)}")
print(f"Result (Optimal Approach): {removeOutermostParanthesis_optimal(s)}")

s = "()()"
print(f"\nInput string: {s}")
print(f"Result (Better Approach): {removeOutermostParanthesis(s)}")
print(f"Result (Optimal Approach): {removeOutermostParanthesis_optimal(s)}")