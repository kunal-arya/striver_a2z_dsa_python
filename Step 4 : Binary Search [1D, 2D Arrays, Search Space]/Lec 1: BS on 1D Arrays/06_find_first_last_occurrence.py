'''
# **Part 1: Main Header Documentation**

# **1. Problem Statement:**
# Given a sorted array of integers `nums` and an integer `target`, find the starting and
# ending position of the `target` value. If the `target` is not found in the array,
# return `[-1, -1]`.

# **2. Brute-force Approach (as in `findFirstLastBrute`):**
# The most straightforward approach is to linearly scan the entire array.
# - Initialize `first = -1` and `last = -1`.
# - Iterate through the array from the beginning. The first time we encounter the `target`,
#   we set `first` to the current index.
# - Continue iterating and keep updating `last` to the current index whenever we see the `target`.
# - Time Complexity: O(n) because we traverse the entire array in the worst case.
# - Space Complexity: O(1) as we only use a few variables.

# **3. Optimal Approach Intuition (as in `findFirstLastOp`):**
# Since the array is sorted, we can use Binary Search. The core idea is to find the
# "lower bound" and "upper bound" for the target element `x`.
# - **Lower Bound:** This is the index of the *first element* that is greater than or equal to `x`.
#   This naturally gives us the first occurrence of `x`.
# - **Upper Bound:** This is the index of the *first element* that is strictly greater than `x`.
#   The last occurrence of `x` will therefore be the index right before the upper bound.
# - By finding `lowerBound(x)` and `upperBound(x) - 1`, we can find the first and last positions.

# **4. Key Observations & Pattern:**
# - This problem is a classic application of Binary Search to find boundaries, not just a value.
# - The `lowerBound` function finds the first occurrence.
# - The `upperBound` function helps find the end of the sequence of the target value.
# - If the `lowerBound` index points to the end of the array or an element not equal to `x`,
#   it means `x` is not present in the array.

# **5. Step-by-step Approach:**
#   1.  Implement a `lowerBound` function that finds the first index `i` where `arr[i] >= x`.
#   2.  Implement an `upperBound` function that finds the first index `i` where `arr[i] > x`.
#   3.  In the main optimal function `findFirstLastOp`:
#   4.  Call `lowerBound` to get the starting position, `lb`.
#   5.  Check if `lb` is a valid index and if `arr[lb]` is actually `x`. If not, the element
#       is not in the array, so return `[-1, -1]`.
#   6.  Call `upperBound` to get the index of the first element strictly greater than `x`.
#   7.  The last occurrence is one index before the `upperBound`.
#   8.  Return `[lb, ub - 1]`.

# **6. Dry Run (Visual Explanation):**
# `arr = [2, 4, 6, 8, 8, 8, 11, 13]`, `x = 8`

# --- lowerBound(arr, 8) ---
# Returns `ans = 3`. This is the first occurrence. `lb = 3`.

# --- upperBound(arr, 8) ---
# Returns `ans = 6`. This is the index of `11`, the first element > 8. `ub = 6`.

# --- findFirstLastOp ---
# `lb` is 3. `arr[3]` is 8, so the element exists.
# The range is `[lb, ub - 1]`, which is `[3, 6 - 1] = [3, 5]`.
# Final Result: `[3, 5]`

# **7. Time Complexity:**
# O(log n). We perform two separate binary searches (`lowerBound` and `upperBound`), each
# taking O(log n) time. The total time is O(log n) + O(log n), which simplifies to O(log n).

# **8. Space Complexity:**
# O(1). We are not using any extra space that scales with the input size.
'''
from typing import List


# Brute Force Solution
def findFirstLastBrute(arr: List[int], x: int) -> List[int]:
    n = len(arr)

    first = -1
    last = -1

    # Iterate through the entire array
    for i in range(n):
        # If the element is found
        if arr[i] == x:
            # If this is the first time we see it, record the index
            if first == -1:
                first = i
            # Always update the last seen index
            last = i
            
    return [first, last]


arr = [2, 4, 6, 8, 8, 8, 11, 13]
x = 8
print(f"Brute Force Result: {findFirstLastBrute(arr, x)}")


# Optimal Solution

def lowerBound(arr: List[int], x: int) -> int:
    """
    Finds the first index such that arr[index] >= x.
    This gives the first occurrence of x.
    """
    n = len(arr)
    low = 0
    high = n - 1
    # ans is initialized to n for the case where x is greater than all elements
    ans = n

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= x:
            # This could be our answer, so store it
            ans = mid
            # Look for a smaller index on the left
            high = mid - 1
        else:
            # We need a larger value, so search on the right
            low = mid + 1

    return ans

def upperBound(arr: List[int], x: int) -> int:
    """
    Finds the first index such that arr[index] > x.
    This helps find the end of the range of x's.
    """
    n = len(arr)
    low = 0
    high = n - 1
    # ans is initialized to n for the case where x is greater than or equal to all elements
    ans = n

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x:
            # This could be our answer, so store it
            ans = mid
            # Look for a smaller index on the left
            high = mid - 1
        else:
            # We need a larger value, so search on the right
            low = mid + 1

    return ans

def findFirstLastOp(arr: List[int], x: int) -> List[int]:
    n = len(arr)

    # Find the lower bound, which is the first occurrence of x
    lb = lowerBound(arr, x)

    # If lower bound is n or the element at lower bound is not x, x is not in the array
    if lb == n or arr[lb] != x:
        return [-1, -1]

    # Find the upper bound and subtract 1 to get the last occurrence of x
    ub = upperBound(arr, x)

    return [lb, ub - 1]

arr = [2, 4, 6, 8, 8, 8, 11, 13]
x = 8
print(f"Optimal Solution Result: {findFirstLastOp(arr, x)}")

'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **Target not in array:** The check `if lb == n or arr[lb] != x:` correctly handles this.
# - **Empty array:** `len(arr)` will be 0, `lowerBound` will return `n` (which is 0), and the
#   check `lb == n` will correctly identify that the element was not found.
# - **Target is the first or last element:** The lower/upper bound logic handles this correctly.
# - **Array with all same elements:** The logic will correctly find the first index (0) and
#   the upper bound (n), resulting in the correct range `[0, n-1]`.

# **2. Common Follow-up Questions & Variations:**
# 1.  **Count occurrences of an element:** A direct application of this problem. The total
#     count is `upperBound(x) - lowerBound(x)`.
# 2.  **Is `upperBound(x) - 1` always the last occurrence?** Yes, because `upperBound` finds
#     the *first* element strictly greater than `x`. The element immediately before it must
#     be the last element that is less than or equal to `x`. Since we already confirmed `x`
#     exists, it must be the last `x`.
# 3.  **What if the array is rotated?** This becomes a much harder problem. You would
#     first need to find the pivot point in the rotated sorted array and then apply a
#     modified binary search on the correct subarray segment(s).
'''

# Optimal Approach 2 (Maybe Interviewer will tell u use Binary Search Only)
def firstOcc(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = low + (high - low) // 2

        # We find the element we were looking for , but to look for first occurence of this
        # number I will move left because this is where index will be less than current
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return first

def lastOcc(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = low + (high - low) // 2

        # Find the number, but I will look to the right b/c I want to find
        # greater index where x is
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return last

def findFirstLastOccOp2(arr,x):
    first = firstOcc(arr,x)
    if first == 1:
        return [-1,-1]
    last = lastOcc(arr,x)
    return [first,last]



arr = [2, 4, 6, 8, 8, 8, 11, 13]
x = 8
print(f"Optimal Solution Result 2: {findFirstLastOccOp2(arr, x)}")
