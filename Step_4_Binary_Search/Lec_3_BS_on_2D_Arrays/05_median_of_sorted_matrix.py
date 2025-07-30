"""
Problem: Median in a row-wise sorted Matrix
Given a row-wise sorted matrix mat[][] where the number of rows and columns is always odd. Return the median of the matrix.

Examples:
Input: mat[][] = [[1, 3, 5], 
                [2, 6, 9], 
                [3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements gives us [1, 2, 3, 3, 5, 6, 6, 9, 9]. Hence, 5 is median.

Platform: GeeksforGeeks
Difficulty: Hard
Topics: Array, Binary Search, Matrix
LINK: https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A row-wise sorted matrix `mat` with odd dimensions (r x c).
- Output: The median of all elements in the matrix.
- Constraints: 
  - 1 <= r, c <= 400
  - 1 <= mat[i][j] <= 2000
- Edge Cases:
  - A matrix with a single element.
  - A matrix with a single row or column.

APPROACH (Optimal):
1. The median of the matrix must lie within the range of the minimum and maximum values present in the matrix. The minimum can be found in the first column and the maximum in the last column.
2. We can binary search on this range of possible answers. Let the range be `[low, high]`.
3. For each `mid` value in our binary search, we need to find how many elements in the matrix are less than or equal to `mid`. Let this count be `smaller_equals_count`.
4. The median is the element `x` such that the number of elements less than or equal to `x` is `(r*c)/2 + 1`.
5. To find `smaller_equals_count` for a given `mid`, we can iterate through each row and use binary search (specifically, `upper_bound`) to find how many elements are `<= mid`. This is efficient because each row is sorted.
6. `upper_bound` on a row for `mid` gives the index of the first element strictly greater than `mid`. This index is also the count of elements `<= mid` in that row.
7. Summing these counts across all rows gives the total `smaller_equals_count`.
8. Now, we adjust our binary search range:
   - If `smaller_equals_count` is less than or equal to the required count `(r*c)/2`, it means our `mid` is too small to be the median, so we need to look for a larger value. We set `low = mid + 1`.
   - If `smaller_equals_count` is greater than the required count, `mid` could be our median, or there could be a smaller value that is also a median. So we store `mid` as a potential answer and try to find a smaller one by setting `high = mid - 1`.
9. The final `low` pointer will point to our median.

TIME COMPLEXITY: O(r * log(c) * log(max_val - min_val)). The outer binary search runs `log(range)` times. Inside it, we iterate through `r` rows, and for each row, we perform a binary search taking `log(c)` time.
SPACE COMPLEXITY: O(1).
"""

from typing import List

# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def medianBrute(arr: List[List[int]]):
    """
    BRUTE FORCE APPROACH - Flatten and sort.
    
    Intuition:
    - The most straightforward way to find the median is to have all elements in a single, sorted list.
    - We can create a new list, add all matrix elements to it, sort it, and then find the middle element.
    
    Approach:
    1. Create an empty list `temp`.
    2. Iterate through each row and each column of the matrix.
    3. Append each element to the `temp` list.
    4. Sort the `temp` list.
    5. The median is the element at the index `(r * c) // 2`.
    
    Args:
        arr: The input 2D matrix.
    
    Returns:
        The median of the matrix.
    
    Time Complexity: O(r * c * log(r * c)) - Dominated by sorting the flattened list of size r*c.
    Space Complexity: O(r * c) - To store all elements in the temporary list.
    """
    n = len(arr)
    m = len(arr[0])
    temp = []

    for i in range(n):
        for j in range(m):
            temp.append(arr[i][j])

    temp.sort()

    return temp[n * m // 2]


# =============================================================================
# SOLUTION 2: OPTIMAL APPROACH (BINARY SEARCH ON ANSWER)
# =============================================================================

def upperBound(arr: List[int], k: int) -> int:
    """
    Helper function to find the upper bound of k in a sorted array.
    Returns the count of elements less than or equal to k.
    """
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def count_smaller_equal(matrix: List[List[int]], k: int) -> int:
    """
    Counts the number of elements in the matrix less than or equal to k.
    """
    count = 0
    for i in range(len(matrix)):
        count += upperBound(matrix[i], k)
    return count

def medianOp(arr: List[List[int]]):
    """
    OPTIMAL APPROACH - Using Binary Search on the answer range.

    Intuition & Key Insight:
    The binary search is not performed on the matrix elements themselves, but on the *range of possible values* for the median, from the matrix's minimum to its maximum element.

    The `mid` value calculated in each step is just a "test value" or a "hypothesis". It might not even exist in the matrix. The crucial question we ask is: "How many elements in the matrix are less than or equal to this `mid` value?"

    Think of the count of elements `<= k` as a staircase function. The count stays flat and only jumps up when `k` crosses a value that actually exists in the matrix.
    
      Count ^
            |
          5 + - - - - - - - - - - - - - + (at value 9)
            |                           |
          4 + - - - - - - - + (at value 6)
            |                 |           |
          1 + - - + (at value 1,2,3)
            |       |           |           |
      ------+-------+-----------+-----------+------> k (value of mid)

    - If the count for `mid` is too small, we know the true median must be larger, so we do `low = mid + 1`. `low` is relentlessly pushed upwards past any value that is too small.
    - If the count is sufficient, `mid` *could* be our answer, but we must check if an even smaller value also works. We do `high = mid - 1` to tighten the search.

    The loop terminates when `low` becomes the *first value* that satisfies the median condition. Because the count "staircase" only steps up at numbers present in the matrix, this first value (`low`) is guaranteed to be an element from the matrix.
    
    Args:
        arr: The input 2D matrix.
    
    Returns:
        The median of the matrix.
    """
    n = len(arr)
    m = len(arr[0])
    # The median is the element at the (n*m)//2 -th index in the sorted array
    # so we need to find an element `x` such that there are (n*m)//2 elements smaller than or equal to it.
    required_count = (n * m) // 2

    # The answer must be between the minimum and maximum element in the matrix.
    low = float("inf")
    high = float("-inf")
    for i in range(n):
        low = min(low, arr[i][0])
        high = max(high, arr[i][m - 1])

    # Binary search for the median in the range [low, high]
    while low <= high:
        mid = low + (high - low) // 2
        smaller_equals = count_smaller_equal(arr, mid)

        if smaller_equals <= required_count:
            # `mid` is too small, need to search in the right half
            low = mid + 1
        else:
            # `mid` could be the answer, try to find a smaller one
            high = mid - 1
    
    return low


# =============================================================================
# MAIN EXECUTION
# =============================================================================

mat =  [[1, 3, 5], 
        [2, 6, 9], 
        [3, 6, 9]]
# Median of mat => 5

print("Brute Force Median:", medianBrute(mat)) 
print("Optimal Median:", medianOp(mat))