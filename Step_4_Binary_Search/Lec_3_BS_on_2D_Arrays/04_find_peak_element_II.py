"""
Problem: Find a Peak Element II
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.
Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].
You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Example 1:
Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:
Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

Platform: LeetCode
Difficulty: Medium
Topics: Array, Binary Search
LINK: https://leetcode.com/problems/find-a-peak-element-ii/
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A 0-indexed m x n matrix `mat`.
- Output: A length 2 array `[i, j]` corresponding to the position of any peak element.
- Constraints: 
  - `m == mat.length`
  - `n == mat[i].length`
  - `1 <= m, n <= 500`
  - `1 <= mat[i][j] <= 10^5`
  - No two adjacent cells are equal.
- Edge Cases:
  - Matrix with a single row or a single column.
  - Peak element is on the edge of the matrix.

APPROACH:
1. Use Binary Search on the column space of the matrix, from `low = 0` to `high = n-1`.
2. In each step, find the middle column `mid`.
3. Find the row index of the maximum element in this `mid` column. Let this be `max_row_index`.
4. This maximum element `mat[max_row_index][mid]` is a potential peak.
5. Check if this element is greater than its left and right neighbors.
   - The neighbors are `mat[max_row_index][mid-1]` and `mat[max_row_index][mid+1]`.
   - Handle boundary conditions for columns (if `mid` is 0 or `n-1`).
6. If `mat[max_row_index][mid]` is greater than both left and right neighbors, it's a peak. Return `[max_row_index, mid]`.
7. If the left neighbor is greater, it means a peak is likely to exist in the left half of the matrix. So, we shrink the search space to `high = mid - 1`.
8. If the right neighbor is greater, a peak is likely in the right half. Shrink the search space to `low = mid + 1`.
9. Repeat until `low <= high`.

TIME COMPLEXITY: O(m * log(n)) - Binary search on columns takes O(log n) iterations, and in each iteration, we find the max element in a column, which takes O(m).
SPACE COMPLEXITY: O(1) - We only use a few variables to keep track of `low`, `high`, and `mid`.
"""

from typing import List

# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def brute_force_solution(mat: List[List[int]]):
    """
    BRUTE FORCE APPROACH - Check every element.
    
    Intuition:
    - Iterate through every cell in the grid.
    - For each cell, check if it is a peak by comparing it with its four neighbors (top, bottom, left, right).
    - Since the problem guarantees a peak exists, this will eventually find one.
    
    Approach:
    1. Iterate through each row `i` from 0 to `m-1`.
    2. Iterate through each column `j` from 0 to `n-1`.
    3. For each element `mat[i][j]`, compare it with its four neighbors.
    4. Handle boundary conditions carefully (e.g., for elements on the edges or corners).
    5. If `mat[i][j]` is greater than all its existing neighbors, return `[i, j]`.
    
    Args:
        mat: The input 2D matrix.
    
    Returns:
        A list `[i, j]` of the peak element's coordinates.
    
    Time Complexity: O(m * n) - We may have to visit every cell in the worst case.
    Space Complexity: O(1) - No extra space is used.
    """
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            # Check top, bottom, left, right neighbors
            top = mat[i-1][j] if i > 0 else -1
            bottom = mat[i+1][j] if i < n-1 else -1
            left = mat[i][j-1] if j > 0 else -1
            right = mat[i][j+1] if j < m-1 else -1
            
            if mat[i][j] > top and mat[i][j] > bottom and mat[i][j] > left and mat[i][j] > right:
                return [i, j]
    return [-1, -1]

# =============================================================================
# SOLUTION 2: OPTIMAL APPROACH (BINARY SEARCH ON COLS)
# =============================================================================

def find_max_in_col(mat: List[List[int]], col: int):
    """Helper function to find the row index of the max element in a given column."""
    max_val = -1
    max_row = -1
    for i in range(len(mat)):
        if mat[i][col] > max_val:
            max_val = mat[i][col]
            max_row = i
    return max_row

def optimal_solution(mat: List[List[int]]):
    """
    OPTIMAL APPROACH - Using Binary Search on Columns.
    
    Intuition:
    - Reduce the search space by half in each step, which suggests binary search.
    - Instead of searching on values, we search on the 2D grid's columns.
    - In any column, find the maximum element. This element is already greater than its top and bottom neighbors.
    - We only need to check its left and right neighbors to see if it's a peak.
    - If it's not a peak, one of its horizontal neighbors must be larger. This gives us a direction to continue our search, effectively eliminating half of the remaining columns.
    
    Approach:
    1. Initialize `low = 0` and `high = n-1` (number of columns - 1).
    2. While `low <= high`, calculate `mid = (low + high) // 2`.
    3. Find the row index of the maximum element in the `mid` column (`max_row_index`).
    4. Get the values of the element itself, and its left and right neighbors. Use -1 for out-of-bounds neighbors.
    5. If `mat[max_row_index][mid]` is a peak (greater than left and right), return `[max_row_index, mid]`.
    6. If the left element is larger, it implies a peak must exist in the left half. So, set `high = mid - 1`.
    7. Otherwise, the right element is larger, so a peak must be in the right half. Set `low = mid + 1`.
    
    Args:
        mat: The input 2D matrix.
    
    Returns:
        A list `[i, j]` of the peak element's coordinates.
    
    Time Complexity: O(m * log(n)) - O(log n) for binary search on columns, O(m) for finding the max in a column.
    Space Complexity: O(1) - Constant extra space.
    """
    n = len(mat)
    m = len(mat[0])
    low, high = 0, m - 1

    while low <= high:
        mid = (low + high) // 2
        max_row = find_max_in_col(mat, mid)
        
        left = mat[max_row][mid - 1] if mid > 0 else -1
        right = mat[max_row][mid + 1] if mid < m - 1 else -1
        
        if mat[max_row][mid] > left and mat[max_row][mid] > right:
            return [max_row, mid]
        elif mat[max_row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
            
    return [-1, -1]

# =============================================================================
# MAIN SOLUTION FUNCTION
# =============================================================================

def find_peak_grid(mat: List[List[int]], approach="optimal"):
    """
    Main function to find a peak element in a 2D grid.
    
    Args:
        mat: The input 2D matrix.
        approach: "brute" or "optimal" (default).
    
    Returns:
        The coordinates `[i, j]` of a peak element.
    """
    if not mat or not mat[0]:
        return [-1, -1]
        
    if approach == "brute":
        return brute_force_solution(mat)
    else:
        return optimal_solution(mat)

mat = [
    [10,20,15],
    [21,30,14],
    [7,16,32]
]

print("Brute force solution:", find_peak_grid(mat, "brute"))
print("Optimal solution:", find_peak_grid(mat, "optimal"))