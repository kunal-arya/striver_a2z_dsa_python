'''
# **Part 1: Main Header Documentation**

# ### Problem 1: Find Minimum in Rotated Sorted Array (Distinct Elements)

# **1. Problem Statement:**
# Given a sorted array of unique integers that has been rotated at some unknown pivot,
# find the minimum element in the array.

# **2. Brute-force Approach (as in `minSortedArrBrute`):**
# The simplest way is to perform a linear scan to find the minimum value.
# - Initialize a variable `ans` to positive infinity.
# - Iterate through every element in the array.
# - In each iteration, update `ans` with the minimum of the current element and the
#   current `ans`.
# - After the loop, `ans` will hold the minimum value in the array.
# - Time Complexity: O(n).
# - Space Complexity: O(1).

# **3. Optimal Approach Intuition (as in `minSortedArrOp`):**
# A linear scan is suboptimal. Since the array is formed from a sorted sequence, we can
# use binary search. The minimum element is the "pivot" or "inflection point" where the
# rotation occurred.
# The core idea is to identify the sorted half of the array at each step. The minimum
# element of a sorted half is always its first element. We can compare this minimum with
# our current answer and then discard that sorted half, because the true minimum must lie
# in the unsorted, "broken" half (which contains the inflection point).

# **4. Key Observations & Pattern:**
# - The minimum element is the only element that is smaller than its previous element (if we
#   consider the array cyclically).
# - At any `mid`, if `arr[low] <= arr[mid]`, the left part is sorted. The minimum of this
#   part is `arr[low]`. The overall minimum could be `arr[low]` or it could be in the
#   unsorted right part. So, we record `arr[low]` and search right.
# - If `arr[low] > arr[mid]`, the right part is sorted. The minimum of this part is `arr[mid]`.
#   The overall minimum could be `arr[mid]` or it could be in the unsorted left part. So,
#   we record `arr[mid]` and search left.
# - A special case: if the entire search space `arr[low] <= arr[high]` is sorted, then
#   `arr[low]` is the minimum of that space.

# **5. Step-by-step Approach (`minSortedArrOp`):**
#   1.  Initialize `low=0`, `high=n-1`, and `ans` to infinity.
#   2.  Loop while `low <= high`.
#   3.  Calculate `mid`.
#   4.  **Optimization:** If `arr[low] <= arr[high]`, the current search space is fully sorted.
#       The minimum is `arr[low]`. Update `ans` and break the loop.
#   5.  **Identify sorted half:** Check if `arr[low] <= arr[mid]`.
#   6.  **Case 1: Left half is sorted.**
#       a. The minimum of this sorted half is `arr[low]`. Update `ans = min(ans, arr[low])`.
#       b. The overall minimum must be in the other (right) half. Eliminate the left: `low = mid + 1`.
#   7.  **Case 2: Right half is sorted.**
#       a. The minimum of this sorted half is `arr[mid]`. Update `ans = min(ans, arr[mid])`.
#       b. The overall minimum must be in the other (left) half. Eliminate the right: `high = mid - 1`.
#   8.  Return `ans`.

# ---

# ### Problem 2: Find Minimum in Rotated Sorted Array (Duplicates Allowed)

# **Intuition for Duplicates (as in `minSortedArrOp2`):**
# The logic is nearly identical, but the presence of duplicates introduces the same
# ambiguous case as in "Search in Rotated Sorted Array II": `arr[low] == arr[mid] == arr[high]`.
# When this happens, we cannot determine which half is sorted. For example, in `[3, 1, 3, 3, 3]`,
# `low=0, mid=2, high=4`. `arr[low]=3, arr[mid]=3, arr[high]=3`. Is the left `[3,1,3]` sorted? No.
# Is the right `[3,3,3]` sorted? Yes. But in `[3,3,3,1,3]`, the left is sorted.
# We cannot be sure. So, we safely shrink the search space by doing `low += 1` and `high -= 1`.

# **Complexity with Duplicates:**
# - Average Case: O(log n).
# - Worst Case: O(n), due to the window shrinking step.
'''
from typing import List

# --- Problem 1: Distinct Elements ---

# Brute Force
def minSortedArrBrute(arr: List[int]):
    n = len(arr)
    ans = float("inf")

    # Simple linear scan to find the minimum
    for i in range(n):
        ans = min(ans, arr[i])

    return ans

arr = [4, 5, 6, 7, 0, 1, 2]
print(f"Brute Force (Distinct): {minSortedArrBrute(arr)}")


# Optimal Approach (Binary Search)
def minSortedArrOp(arr: List[int]):
    n = len(arr)
    ans = float("inf")
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Optimization: If the entire search space is sorted,
        # the minimum is the first element.
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break

        # Case 1: Left half is sorted
        if arr[low] <= arr[mid]:
            # The minimum of the left half is arr[low].
            ans = min(ans, arr[low])
            # Eliminate the sorted left half and search right.
            low = mid + 1
        # Case 2: Right half is sorted
        else:
            # The minimum of the right half is arr[mid].
            ans = min(ans, arr[mid])
            # Eliminate the sorted right half and search left.
            high = mid - 1
    
    return ans

arr = [4, 5, 6, 7, 0, 1, 2]
print(f"Optimal (Distinct): {minSortedArrOp(arr)}")


# --- Problem 2: Duplicates Allowed ---

def minSortedArrOp2(arr: List[int]):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")

    while low <= high:
        mid = low + (high - low) // 2

        # Ambiguous case: cannot determine the sorted half.
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            # Record arr[low] as a potential answer and shrink the window.
            ans = min(ans, arr[low])
            low = low + 1
            high = high - 1
            continue
        
        # Case 1: Left half is sorted
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        # Case 2: Right half is sorted
        else:
            ans = min(ans, arr[mid])
            high = mid - 1

    return ans

arr = [3, 1, 3]
print(f"Optimal (Duplicates): {minSortedArrOp2(arr)}")
'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **Array is not rotated:** The `if arr[low] <= arr[high]` optimization handles this
#   efficiently, breaking in the first step.
# - **Array with 1 or 2 elements:** The logic holds correctly.
# - **Duplicates (for Problem 2):** The `arr[low] == arr[mid] == arr[high]` check is
#   critical to prevent getting stuck and to ensure progress.

# **2. Common Follow-up Questions & Variations:**
# 1.  **Can you do this without the `ans` variable?** Yes. A slightly different implementation
#     can simply shrink the `low` and `high` pointers. The loop terminates when `low == high`,
#     and that element is the minimum. For example, if `arr[mid] > arr[high]`, you know the
#     minimum is in `mid+1..high`. If `arr[mid] < arr[high]`, the minimum is in `low..mid`.
#     This is another common way to frame the solution.
# 2.  **How does this relate to finding a target element?** Finding the minimum is often the
#     first step in a more complex problem. Once you find the index of the minimum element,
#     you know where the rotation pivot is. You can then perform a standard binary search
#     on two separate, sorted subarrays: one from the start to the pivot, and one from the
#     pivot to the end.
'''