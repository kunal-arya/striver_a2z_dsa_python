"""
Problem: Search in a 2D Matrix II
Platform: LeetCode
Difficulty: Medium
Topics: Array, Binary Search, Divide and Conquer, Matrix
LINK: https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: An m x n integer matrix `mat` and an integer `k` (target).
- Output: `True` if `k` exists in `mat`, otherwise `False`.
- Constraints:
    - The matrix `mat` has the following properties:
        - Integers in each row are sorted in ascending order from left to right.
        - Integers in each column are sorted in ascending order from top to bottom.
- Edge Cases:
    - Empty matrix.
    - Matrix with one row or one column.
    - Target is smaller than the smallest element or larger than the largest element.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def searchIn2DBrute(mat, k):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - Traverse every element in the matrix and check if it equals the target value.
    - This approach ignores the sorted property of the matrix.
    
    Approach:
    1. Use nested loops to iterate through each row `i` and each column `j`.
    2. In each iteration, compare `mat[i][j]` with the target `k`.
    3. If a match is found, return `True` immediately.
    4. If the loops complete without finding the target, return `False`.
    
    Args:
        mat (list[list[int]]): The sorted 2D matrix.
        k (int): The target value to search for.
    
    Returns:
        bool: True if k is found, False otherwise.
    
    Time Complexity: O(n * m), where n is the number of rows and m is the number of columns. We visit every element.
    Space Complexity: O(1), as no extra space is used.
    """
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            if mat[i][j] == k:
                return True
    
    return False

# ==============================================================================
# SOLUTION 2: BETTER APPROACH
# ==============================================================================

def searchIn2DBetter(mat, k):
    """
    BETTER APPROACH - Using Binary Search on each row.
    
    Intuition:
    - Since each row is sorted, we can apply binary search on every single row to find the target.
    - This is better than brute force because we avoid a linear scan of each row.
    
    Approach:
    1. Iterate through each row of the matrix.
    2. For each row, perform a standard binary search for the target `k`.
    3. If binary search finds the target in any row, return `True`.
    4. If all rows are searched and the target is not found, return `False`.
    
    Args:
        mat (list[list[int]]): The sorted 2D matrix.
        k (int): The target value to search for.
    
    Returns:
        bool: True if k is found, False otherwise.
    
    Time Complexity: O(n * log m), where n is the number of rows and m is the number of columns. We perform a binary search (log m) for each of the n rows.
    Space Complexity: O(1), as no extra space is used.
    """
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        low = 0
        high = m - 1

        while low <= high:
            mid = (high + low) // 2

            if mat[i][mid] == k:
                return True
            elif mat[i][mid] > k:
                high = mid - 1
            else:
                low = mid + 1

    return False

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH
# ==============================================================================

def searchIn2DOp(mat, k):
    """
    OPTIMAL APPROACH - Staircase Search.
    
    Intuition:
    - Leverage both row and column sorted properties simultaneously.
    - Start at a corner that allows for eliminating a row or a column in each step. The top-right corner is a good choice (bottom-left also works).
    - From the top-right element `mat[row][col]`:
        - If `mat[row][col] == k`, we found it.
        - If `mat[row][col] < k`, the target cannot be in the current row because all elements to the left are smaller. So, we move down to the next row to find a larger value.
        - If `mat[row][col] > k`, the target cannot be in the current column because all elements below are larger. So, we move left to the previous column to find a smaller value.
    
    Approach:
    1. Initialize two pointers: `row = 0` and `col = m - 1` (top-right corner).
    2. Loop as long as the pointers are within the matrix bounds (`row < n` and `col >= 0`).
    3. Compare the element at `mat[row][col]` with the target `k`.
    4. If they are equal, return `True`.
    5. If the element is less than `k`, move down by incrementing `row`.
    6. If the element is greater than `k`, move left by decrementing `col`.
    7. If the loop finishes, the element was not found, so return `False`.
    
    Args:
        mat (list[list[int]]): The sorted 2D matrix.
        k (int): The target value to search for.
    
    Returns:
        bool: True if k is found, False otherwise.
    
    Time Complexity: O(n + m). In the worst case, the pointer moves from the top-right to the bottom-left, traversing at most n rows and m columns.
    Space Complexity: O(1), as no extra space is used.
    """
    n = len(mat)
    m = len(mat[0])

    row = 0
    col = m - 1

    while row < n and col >= 0:
        if mat[row][col] == k:
            return True
        elif mat[row][col] < k:
            row += 1
        else:
            col -= 1

    return False

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    mat = [
        [  1,  4,  7, 11, 15],
        [  2,  5,  8, 12, 19],
        [  3,  6,  9, 16, 22],
        [ 10, 13, 14, 17, 24],
        [ 18, 21, 23, 26, 30]
    ]
    target = 13
    
    print(f"Searching for {target} in the matrix.")
    
    print("\n--- Brute Force Approach ---")
    print(f"Found: {searchIn2DBrute(mat, target)}")
    
    print("\n--- Better Approach (Binary Search per Row) ---")
    print(f"Found: {searchIn2DBetter(mat, target)}")
    
    print("\n--- Optimal Approach (Staircase Search) ---")
    print(f"Found: {searchIn2DOp(mat, target)}")

    target_not_found = 20
    print(f"\nSearching for {target_not_found} in the matrix.")
    print(f"Found: {searchIn2DOp(mat, target_not_found)}")