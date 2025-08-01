"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
"""

# Brute Force Approach
# Time Complexity: O(n^2) due to string slicing and concatenation in a loop
# Space Complexity: O(n) for the temporary string
def rotateStrBrute(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    
    temp_s = s
    for _ in range(len(s)):
        temp_s = temp_s[1:] + temp_s[0] # rotate
        if temp_s == goal:
            return True
    return False

# Optimal Approach
# Time Complexity: O(n) where n is the length of the string.
# Space Complexity: O(n) to store the concatenated string.
# This approach is efficient because if 'goal' is a rotation of 's', 
# then 'goal' must be a substring of 's' concatenated with itself.
def rotateStrOptimal(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
        
    return len(s) == len(goal) and goal in s + s

s = "abcde"
goal = "cdeab"

print(f"Is '{goal}' a rotation of '{s}'? (Brute Force): {rotateStrBrute(s, goal)}")
print(f"Is '{goal}' a rotation of '{s}'? (Optimal): {rotateStrOptimal(s, goal)}")

s = "abcde"
goal = "abced"

print(f"Is '{goal}' a rotation of '{s}'? (Brute Force): {rotateStrBrute(s, goal)}")
print(f"Is '{goal}' a rotation of '{s}'? (Optimal): {rotateStrOptimal(s, goal)}")

s = "defdefdefabcabc"
goal = "defdefabcabcdef"

print(f"Is '{goal}' a rotation of '{s}'? (Brute Force): {rotateStrBrute(s, goal)}")
print(f"Is '{goal}' a rotation of '{s}'? (Optimal): {rotateStrOptimal(s, goal)}")
