'''
# **Part 1: Main Header Documentation**

# **1. Problem Statement:**
# Given a sorted array of distinct integers that has been rotated at some unknown pivot,
# and a target integer `x`, find the index of `x` in the array. If `x` is not present,
# return -1.

# **2. Brute-force Approach (as in `searchInRotatedSortedArrBrute`):**
# The simplest solution is to ignore the array's special properties and perform a linear search.
# - Iterate through the array from the first element to the last.
# - At each element, check if it is equal to the target `x`.
# - If a match is found, return the current index.
# - If the loop completes without finding the target, return -1.
# - Time Complexity: O(n), as we may need to scan the entire array.
# - Space Complexity: O(1).

# **3. Optimal Approach Intuition (as in `searchOp`):**
# A linear scan is inefficient. The fact that the array is composed of sorted segments
# suggests that a modification of Binary Search is possible.
# The core insight is that when we calculate `mid`, at least one of the two halves
# (from `low` to `mid` or from `mid` to `high`) must be sorted.
# We can identify the sorted half and then check if our target lies within the range of
# that sorted half.
# - If the target is in the range of the sorted half, we search within it.
# - If the target is *not* in the range of the sorted half, it must be in the other,
#   unsorted (but still partially ordered) half. So, we search there.
# This process allows us to eliminate half of the search space in each step, preserving
# the O(log n) efficiency of binary search.

# **4. Key Observations & Pattern:**
# - The main pattern is "Modified Binary Search".
# - At any `mid`, the condition `arr[low] <= arr[mid]` tells us if the left half is sorted.
#   If it's false, the right half (`arr[mid]` to `arr[high]`) must be sorted.
# - Once the sorted half is identified, a simple range check (`min <= target <= max`)
#   is enough to decide where to continue the search.

# **5. Step-by-step Approach:**
#   1.  Initialize `low = 0` and `high = n - 1`.
#   2.  Start a `while low <= high` loop.
#   3.  Calculate `mid`. If `arr[mid] == x`, we found the target, return `mid`.
#   4.  **Identify the sorted half:** Check if `arr[low] <= arr[mid]`.
#   5.  **Case 1: Left half is sorted (`arr[low] <= arr[mid]`)**
#       a. Check if the target lies within the range of the sorted left half
#          (i.e., `arr[low] <= x and x <= arr[mid]`).
#       b. If yes, the target is in the left half. Eliminate the right half: `high = mid - 1`.
#       c. If no, the target must be in the right half. Eliminate the left half: `low = mid + 1`.
#   6.  **Case 2: Right half is sorted (`arr[low] > arr[mid]`)**
#       a. Check if the target lies within the range of the sorted right half
#          (i.e., `arr[mid] <= x and x <= arr[high]`).
#       b. If yes, the target is in the right half. Eliminate the left half: `low = mid + 1`.
#       c. If no, the target must be in the left half. Eliminate the right half: `high = mid - 1`.
#   7.  If the loop finishes, the target was not found, so return -1.

# **6. Dry Run (Visual Explanation):**
# `arr = [7, 8, 9, 1, 2, 4, 6]`, `x = 1`

# - **Initial:** `low=0`, `high=6`
# - **Step 1:** `mid=3`. `arr[3]` is 1. `arr[mid] == x`. **Return `mid` which is 3.**

# Let's try another example: `x = 8`
# - **Initial:** `low=0`, `high=6`
# - **Step 1:** `mid=3`. `arr[3]` is 1. `arr[mid] != x`.
#   - Is left half sorted? `arr[0](7) <= arr[3](1)` is false.
#   - So, right half (`arr[3]` to `arr[6]`) is sorted: `[1, 2, 4, 6]`.
#   - Does `x=8` lie in the right half? `1 <= 8 <= 6` is false.
#   - Target must be in the other (left) half. Eliminate right: `high = mid - 1 = 2`.
# - **Step 2:** `low=0`, `high=2`. `mid=1`. `arr[1]` is 8. `arr[mid] == x`. **Return `mid` which is 1.**

# **7. Time Complexity:**
# O(log n). In each step, we discard half of the search space, which is the hallmark of a
# binary search algorithm.

# **8. Space Complexity:**
# O(1). We only use a few variables to keep track of indices.
'''
from typing import List

# Brute Force
def searchInRotatedSortedArrBrute(arr: List[int], x: int) -> int:
    n = len(arr)

    # Perform a simple linear scan
    for i in range(n):
        if arr[i] == x:
            return i
        
    # Return -1 if the target is not found
    return -1

arr = [7, 8, 9, 1, 2, 4, 6]
x = 1
print(f"Brute Force Result: {searchInRotatedSortedArrBrute(arr, x)}")


# Optimal Approach (Binary Search)
def searchOp(arr: List[int], x: int) -> int:
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        # If we found the target, return its index
        if arr[mid] == x:
            return mid
        
        # Case 1: The left half (low to mid) is sorted
        if arr[low] <= arr[mid]:
            # Check if the target lies within the sorted left half
            if arr[low] <= x and x <= arr[mid]:
                # Eliminate the right half
                high = mid - 1
            else:
                # Target must be in the unsorted right half
                low = mid + 1
        # Case 2: The right half (mid to high) is sorted
        else:
            # Check if the target lies within the sorted right half
            if arr[mid] <= x and x <= arr[high]:
                # Eliminate the left half
                low = mid + 1
            else:
                # Target must be in the unsorted left half
                high = mid - 1

    # If the loop completes, the target was not found
    return -1

arr = [7, 8, 9, 1, 2, 4, 6]
x = 1
print(f"Optimal Solution Result: {searchOp(arr, x)}")

x = 8
print(f"Optimal Solution Result for 8: {searchOp(arr, x)}")

x = 99
print(f"Optimal Solution Result for 99: {searchOp(arr, x)}")

'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **Array with 1 or 2 elements:** The logic holds. The `low <= high` and range checks
#   correctly handle these small arrays.
# - **Array is not rotated at all (fully sorted):** The condition `arr[low] <= arr[mid]`
#   will always be true. The algorithm then behaves exactly like a standard binary search.
# - **Target is the pivot element:** The `arr[mid] == x` check will eventually find it.
# - **Target does not exist:** The search space will correctly shrink until `low > high`,
#   and the function will return -1.

# **2. Common Follow-up Questions & Variations:**
# 1.  **What if the array contains duplicate elements?** This is a much harder variation.
#     The condition `arr[low] <= arr[mid]` is no longer sufficient to determine the sorted
#     half. If `arr[low] == arr[mid] == arr[high]`, you cannot determine which half is
#     sorted. In this specific case, you must shrink the search space by incrementing `low`
#     and decrementing `high`. This can degrade the worst-case time complexity to O(n).
# 2.  **Find the minimum element in the rotated sorted array:** This is a related problem.
#     You can use a similar modified binary search to find the "pivot" or minimum value
#     in O(log n) time. The minimum element is the only one that is smaller than its
#     predecessor.
'''