'''
# **Part 1: Main Header Documentation**

# **1. Problem Statement:**
# Given a sorted array of integers `arr` and an integer `x`, find the total number of
# occurrences of `x` in the array.

# **2. Brute-force Approach (as in `countOccurenceBrute`):**
# The most straightforward solution is to iterate through the entire array and maintain a
# counter.
# - Initialize `count = 0`.
# - Loop through each element of the array from start to finish.
# - If the current element is equal to `x`, increment the `count`.
# - After the loop finishes, return the final `count`.
# - Time Complexity: O(n), as we must visit every element in the worst case.
# - Space Complexity: O(1), as we only use a single counter variable.

# **3. Optimal Approach Intuition (as in `countOccurenceOp`):**
# Since the array is sorted, we can use a more efficient approach than a linear scan.
# The key insight is that all occurrences of `x` will be in a contiguous block. If we can
# find the start and end of this block, we can calculate the count.
# The problem reduces to finding the index of the **first occurrence** of `x` and the
# index of the **last occurrence** of `x`.
# The total count is then `last_index - first_index + 1`.
# A very clever way to do this is to find the `firstOccurrence(x)` (also known as lower bound)
# and the `upperBound(x)`. The upper bound is the index of the first element *strictly greater*
# than `x`. The difference between these two bounds gives the number of elements equal to `x`.

# **4. Key Observations & Pattern:**
# - This problem is a direct application of the "Find First and Last Position" problem.
# - The number of occurrences of an element `x` in a sorted array is equal to:
#   `(index of first element > x) - (index of first element >= x)`.
# - This translates to `upperBound(x) - lowerBound(x)`.
# - If the first occurrence doesn't exist, the element is not in the array, and the count is 0.

# **5. Step-by-step Approach:**
#   1.  Implement a `firstOccurence` function (or `lowerBound`) that finds the first index `i`
#       where `arr[i] >= x`. It should return -1 if `x` is not found.
#   2.  Implement an `upperBound` function that finds the first index `i` where `arr[i] > x`.
#   3.  In the main optimal function `countOccurenceOp`:
#   4.  Call `firstOccurence` to get the starting position, `first`.
#   5.  If `first` is -1, it means `x` is not in the array, so return 0 immediately.
#   6.  Call `upperBound` to get the index of the first element strictly greater than `x`.
#   7.  The total count is the difference: `upperBound - first`.

# **6. Dry Run (Visual Explanation):**
# `arr = [2, 4, 6, 8, 8, 8, 11, 13]`, `x = 8`

# --- firstOccurence(arr, 8) ---
# This will find the lower bound of 8.
# Returns `ans = 3`. `first = 3`.

# --- upperBound(arr, 8) ---
# This will find the first element strictly greater than 8.
# Returns `ans = 6` (the index of 11). `upper_bound = 6`.

# --- countOccurenceOp ---
# `first` is 3, which is not -1.
# The count is `upper_bound - first` = `6 - 3` = `3`.
# Final Result: 3

# **7. Time Complexity:**
# O(log n). We perform two separate binary searches (`firstOccurence` and `upperBound`),
# each taking O(log n) time. The total time complexity is O(log n).

# **8. Space Complexity:**
# O(1). We only use a few variables for the indices and bounds, which is constant space.
'''
from typing import List

# Brute Approach
def countOccurenceBrute(arr: List[int], x: int):
    n = len(arr)
    count = 0

    # Linearly scan the array
    for i in range(n):
        # If element is found, increment counter
        if arr[i] == x:
            count += 1

    return count


# Optimal Approach
def firstOccurence(arr: List[int], x: int) -> int:
    """
    Finds the lower bound of x, which is the first index where arr[index] >= x.
    Returns -1 if x is not found.
    """
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= x:
            ans = mid
            # Search for an even earlier occurrence on the left
            high = mid - 1
        else:
            low = mid + 1
    
    # If ans is n or the element at ans is not x, then x is not in the array
    if ans == n or arr[ans] != x:
        return -1

    return ans

def upperBound(arr: List[int], x: int) -> int:
    """
    Finds the upper bound of x, which is the first index where arr[index] > x.
    """
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x:
            ans = mid
            # Search for an even earlier occurrence on the left
            high = mid - 1
        else:
            low = mid + 1

    return ans


def countOccurenceOp(arr: List[int], x: int) -> int:
    # Find the first occurrence of x
    first = firstOccurence(arr,x)

    # If the element doesn't exist, its count is 0
    if first == -1:
        return 0
    
    # Find the index of the first element greater than x
    upper_bound = upperBound(arr,x)

    # The difference is the number of occurrences
    return upper_bound - first


arr = [2, 4, 6, 8, 8, 8, 11, 13]
x = 8
print(f"Brute Solution Result: {countOccurenceBrute(arr, x)}")
print(f"Optimal Solution Result: {countOccurenceOp(arr, x)}")

x = 13
print(f"Brute Solution Result for 13: {countOccurenceBrute(arr, x)}")
print(f"Optimal Solution Result for 13: {countOccurenceOp(arr, x)}")

x = 99
print(f"Brute Solution Result for 99: {countOccurenceBrute(arr, x)}")
print(f"Optimal Solution Result for 99: {countOccurenceOp(arr, x)}")

'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **Target not in array:** `firstOccurence` correctly returns -1, and `countOccurenceOp`
#   returns 0 as expected.
# - **Empty array:** `firstOccurence` will get n=0 and return -1, leading to a final count of 0.
# - **Target is the only element:** `firstOccurence` will be 0, `upperBound` will be 1.
#   Count = 1 - 0 = 1. Correct.
# - **All elements are the target:** `firstOccurence` will be 0, `upperBound` will be n.
#   Count = n - 0 = n. Correct.

# **2. Common Follow-up Questions & Variations:**
# 1.  **What if you can only use one helper function?** You can solve this with just a
#     `lowerBound` function. The count would be `lowerBound(x + 1) - lowerBound(x)`.
#     This is a common and elegant variation.
# 2.  **How would this work for a very large dataset that doesn't fit in memory?**
#     This approach assumes the array is in memory. For larger datasets, you'd need to
#     rely on database indexing or other external storage search mechanisms.
# 3.  **Is this approach always better than brute-force?** For small arrays, the overhead
#     of two binary searches might make the brute-force method slightly faster due to
#     simpler logic and better CPU cache performance. However, for any reasonably sized
#     array, the O(log n) complexity is vastly superior.
'''