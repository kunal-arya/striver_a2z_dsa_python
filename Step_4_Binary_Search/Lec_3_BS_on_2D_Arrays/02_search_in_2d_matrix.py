"""
Problem: Search for a target value in an m x n integer matrix `matrix` that has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Example:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Platform: LeetCode
Difficulty: Medium
Topics: Array, Binary Search, Matrix
LINK: https://leetcode.com/problems/search-a-2d-matrix/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: An m x n matrix of integers and a target integer.
- Output: A boolean value indicating if the target is in the matrix.
- Constraints:
    - The matrix is sorted row-wise.
    - The first element of a row is greater than the last element of the previous row.
- Edge Cases:
    - Empty matrix.
    - Matrix with one row or one column.
    - Target smaller than the first element or larger than the last element.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def searchIn2DBrute(mat, k):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - Traverse every element in the matrix and check if it equals the target.
    - This approach ignores the sorted nature of the matrix.
    
    Approach:
    1. Use nested loops to iterate through each row and column.
    2. In the inner loop, compare the current element with the target `k`.
    3. If a match is found, return True immediately.
    4. If the loops complete without finding the target, return False.
    
    Args:
        mat (list[list[int]]): The 2D matrix.
        k (int): The target value to search for.
    
    Returns:
        bool: True if the target is found, False otherwise.
    
    Time Complexity: O(n * m) - We visit every element in the n x m matrix.
    Space Complexity: O(1) - No extra space is used.
    """
    n = len(mat)
    if n == 0:
        return False
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            if mat[i][j] == k:
                return True
            
    return False

# ==============================================================================
# SOLUTION 2: BETTER APPROACH (Binary Search on each row)
# ==============================================================================

def searchIn2DBetter(mat, k):
    """
    BETTER APPROACH - Using Binary Search on the correct row.
    
    Intuition:
    - Since each row is sorted, we can apply binary search to find the target.
    - First, we need to identify which row could possibly contain the target.
    - A row `i` is a candidate if the target `k` is between its first and last elements (`mat[i][0] <= k <= mat[i][m-1]`).
    
    Approach:
    1. Iterate through each row of the matrix.
    2. For each row, check if the target `k` falls within the range of values in that row.
    3. If it does, perform a standard binary search on that specific row.
    4. If the binary search finds the target, return True.
    5. If the loop finishes and no row contains the target, return False.
    
    Args:
        mat (list[list[int]]): The 2D matrix.
        k (int): The target value to search for.
    
    Returns:
        bool: True if the target is found, False otherwise.
    
    Time Complexity: O(n * log m) - We iterate through n rows, and for each, we might perform a binary search which takes O(log m) time.
    Space Complexity: O(1) - No extra space is used.
    """
    n = len(mat)
    if n == 0:
        return False
    m = len(mat[0])

    for i in range(n):
        # Check if the target is within the range of the current row
        if mat[i][0] <= k <= mat[i][m - 1]:
            # Perform binary search on this row
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
# SOLUTION 3: OPTIMAL APPROACH (Binary Search on the whole matrix)
# ==============================================================================

def searchIn2DOp(mat, k):
    """
    OPTIMAL APPROACH - Treat the 2D matrix as a flattened 1D sorted array.
    
    Intuition:
    - The properties of the matrix (sorted rows, and each row's start is greater than the previous row's end) mean that if we "flatten" the matrix into a 1D array, it would be completely sorted.
    - We can perform a binary search on this "virtual" 1D array without actually creating it.
    
    Approach:
    1. Define the search space as a 1D array of size `n * m`.
    2. Initialize `low = 0` and `high = (n * m) - 1`.
    3. Perform a standard binary search loop while `low <= high`.
    4. In each iteration, calculate the middle index `mid`.
    5. Convert this 1D `mid` index back to 2D matrix coordinates:
       - `row = mid // m` (integer division gives the row index)
       - `col = mid % m` (modulo operation gives the column index)
    6. Compare `mat[row][col]` with the target `k` and adjust `low` and `high` accordingly.
    
    Args:
        mat (list[list[int]]): The 2D matrix.
        k (int): The target value to search for.
    
    Returns:
        bool: True if the target is found, False otherwise.
    
    Time Complexity: O(log(n * m)) - Standard binary search on `n * m` elements.
    Space Complexity: O(1) - No extra space is used.
    """
    n = len(mat)
    if n == 0:
        return False
    m = len(mat[0])

    low = 0
    high = (n * m) - 1

    while low <= high:
        mid = (high + low) // 2
        i = mid // m  # row index
        j = mid % m   # column index

        if mat[i][j] == k:
            return True
        elif mat[i][j] > k:
            high = mid - 1
        else:
            low = mid + 1

    return False

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    mat = [
        [3, 4, 7, 9],
        [12, 13, 16, 18],
        [20, 21, 23, 29],
    ]
    target = 13

    print("Matrix:")
    for row in mat:
        print(row)
    print(f"Target: {target}\n")

    print("Brute Force Approach:")
    print(f"Found: {searchIn2DBrute(mat, target)}\n")

    print("Better Approach (BS on row):")
    print(f"Found: {searchIn2DBetter(mat, target)}\n")

    print("Optimal Approach (BS on matrix):")
    print(f"Found: {searchIn2DOp(mat, target)}\n")

    # Test case 2
    target2 = 22
    print(f"Target: {target2}")
    print("Optimal Approach:")
    print(f"Found: {searchIn2DOp(mat, target2)}")