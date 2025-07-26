"""
Problem: Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.
Example: 
Input: [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
Output: 2
Explanation: Row 2 contains the maximum number of 1s.
Platform: GeeksforGeeks
Difficulty: Easy
Topics: Array, Binary Search, Matrix
LINK: https://www.geeksforgeeks.org/find-the-row-with-maximum-number-of-1s/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A 2D list (matrix) of 0s and 1s.
- Output: The index of the row with the maximum number of 1s.
- Constraints: The matrix can have n rows and m columns. Each row is sorted in non-decreasing order.
- Edge Cases: 
    - Matrix with a single row or column.
    - Matrix with all 0s or all 1s.
    - Multiple rows with the same maximum number of 1s (return the first one).

APPROACH:
1. Brute Force: Iterate through each row, count the 1s, and keep track of the row with the maximum count.
2. Optimal: Since each row is sorted, we can use binary search to find the first occurrence of 1 in each row. This gives us the count of 1s in that row. We can then find the row with the maximum count.

TIME COMPLEXITY:
- Brute Force: O(n*m)
- Optimal: O(n*log(m))

SPACE COMPLEXITY:
- Brute Force: O(1)
- Optimal: O(1)
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

from typing import List

def rowWithMaxOneBrute(mat: List[List[int]]):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - Iterate through each element of the matrix and count the number of 1s in each row.
    - Keep track of the maximum count and the corresponding row index.
    
    Approach:
    1. Initialize `maxCount` to -1 and `maxIdx` to -1.
    2. Iterate through each row of the matrix.
    3. For each row, iterate through its columns and count the number of 1s.
    4. If the current row's count is greater than `maxCount`, update `maxCount` and `maxIdx`.
    5. Return `maxIdx`.
    
    Args:
        mat: The input 2D list of 0s and 1s.
    
    Returns:
        The index of the row with the maximum number of 1s.
    
    Time Complexity: O(n*m) - We traverse the entire matrix.
    Space Complexity: O(1) - No extra space is used.
    """
    n = len(mat)
    m = len(mat[0])
    maxCount = -1
    maxIdx = -1

    for i in range(n):
        countNow = 0
        for j in range(m):
            countNow += mat[i][j]
        if countNow > maxCount:
            maxCount = countNow
            maxIdx = i

    return maxIdx

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH
# ==============================================================================

def rowWithMaxOneOp(mat: List[List[int]]):
    """
    OPTIMAL APPROACH - Using binary search.
    
    Intuition:
    - Since each row is sorted, we can efficiently find the number of 1s by finding the index of the first 1.
    - The number of 1s will be `m - first_one_index`.
    - We can use binary search to find the first 1 in each row.
    
    Approach:
    1. Initialize `maxIdx` to -1 and `maxCount` to 0.
    2. Iterate through each row of the matrix.
    3. For each row, use binary search to find the index of the first occurrence of 1.
    4. The number of 1s in the current row is `m - low` (where `low` is the lower bound of the search).
    5. If this count is greater than `maxCount`, update `maxCount` and `maxIdx`.
    6. Return `maxIdx`.
    
    Args:
        mat: The input 2D list of 0s and 1s.
    
    Returns:
        The index of the row with the maximum number of 1s.
    
    Time Complexity: O(n*log(m)) - We perform a binary search for each of the n rows.
    Space Complexity: O(1) - No extra space is used.
    """
    n = len(mat)
    m = len(mat[0])

    maxIdx = -1
    maxCount = 0

    for i in range(n):
        low = 0
        high = m - 1

        while low <= high:
            mid = (high + low) // 2

            if mat[i][mid] == 1:
                high = mid - 1
            else:
                low = mid + 1

        total_ones = m - low

        if total_ones > maxCount:
            maxCount = total_ones
            maxIdx = i

    return maxIdx

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    mat = [
        [0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1]
    ]

    print("Brute Force Approach:", rowWithMaxOneBrute(mat))
    print("Optimal Approach:", rowWithMaxOneOp(mat))