'''
# **Part 1: Main Header Documentation**

# ### Problem 1: How Many Times a Sorted Array is Rotated (Distinct Elements)

# **1. Problem Statement:**
# Given a sorted array of unique integers that has been rotated `k` times, find the
# value of `k`.

# **2. Core Insight:**
# The number of times a sorted array has been rotated is equal to the **index of its
# minimum element**. For example, if `[1, 2, 3, 4, 5]` is rotated twice, it becomes
# `[4, 5, 1, 2, 3]`. The minimum element `1` is now at index 2.
# Therefore, this problem is identical to "Find the Minimum in a Rotated Sorted Array",
# except we must return the index, not the value.

# **3. Brute-force Approach (as in `timesArrayRotatedBrute`):**
# A linear scan can find the minimum element and its index.
# - Time Complexity: O(n).
# - Space Complexity: O(1).

# **4. Optimal Approach (as in `timesArrayRotatedOp`):**
# We adapt the binary search solution for finding the minimum element to also track its index.
# - **Logic:** At each step, identify the sorted half. The minimum of that half is its
#   first element. Compare this to our current global minimum. If it's smaller, update
#   our answer (both value and index). Then, discard the sorted half and search in the
#   other half for a potentially even smaller value.
# - **Time Complexity:** O(log n).
# - **Space Complexity:** O(1).

# ---

# ### Problem 2: Handling Duplicates (as in `timesArrayRotatedDuplicates`)

# **1. The Challenge with Duplicates:**
# The logic is nearly identical, but duplicates introduce the ambiguous case where
# `arr[low] == arr[mid] == arr[high]`. In this situation, we cannot determine which half
# is sorted. For example, in `[3, 3, 1, 3, 3]`, the right half is sorted, but in
# `[3, 1, 3, 3, 3]`, the left half contains the inflection point.
#
# **2. The Solution:**
# When the ambiguous case `arr[low] == arr[mid] == arr[high]` occurs, we cannot safely
# eliminate half the search space. Instead, we simply shrink the window by one element
# from each side (`low += 1`, `high -= 1`) and continue the search.
#
# **3. Complexity with Duplicates:**
# - **Average Case:** O(log n).
# - **Worst Case:** O(n). This occurs when many elements are the same, forcing the
#   algorithm to shrink the window linearly (e.g., `[3, 3, 3, 3, 1, 3, 3]`).

'''
# Problem => How Many Times has the Array been rotated?
# ex => arr = [3,4,5,1,2]. The number of rotations is the index of the minimum element.

# --- Problem 1: Distinct Elements ---

# Brute Force (linear search)
def timesArrayRotatedBrute(arr):
    n = len(arr)
    ans = float("inf")
    min_idx = -1

    # Linearly scan to find the minimum element and its index
    for i in range(n):
        if arr[i] < ans:
            ans = arr[i]
            min_idx = i

    return min_idx

arr = [3, 4, 5, 1, 2]
print(f"Brute Force Result: {timesArrayRotatedBrute(arr)}")

# Optimal Approach (Binary Search)
def timesArrayRotatedOp(arr):
    n = len(arr)
    low = 0
    high = n - 1
    minE = float("inf")
    minIdx = -1

    while low <= high:
        mid = low + (high - low) // 2

        # Optimization: If the search space is already sorted
        if arr[low] <= arr[high]:
            if arr[low] < minE:
                minE = arr[low]
                minIdx = low
            break
        
        # Case 1: Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] < minE:
                minE = arr[low]
                minIdx = low
            low = mid + 1
        # Case 2: Right half is sorted
        else:
            if arr[mid] < minE:
                minE = arr[mid]
                minIdx = mid
            high = mid - 1

    return minIdx

arr = [3, 4, 5, 1, 2]
print(f"Optimal Solution Result: {timesArrayRotatedOp(arr)}")


# --- Problem 2: Duplicates Allowed ---

def timesArrayRotatedDuplicates(arr):
    n = len(arr)
    low = 0
    high = n - 1
    ans = float("inf")
    minIdx = -1

    while low <= high:
        mid = low + (high - low) // 2

        # Ambiguous case: if low, mid, and high are the same
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            # We can't decide, so check if this is a new minimum
            if arr[low] < ans:
                ans = arr[low]
                minIdx = low
            # And shrink the window
            low += 1
            high -= 1
            continue

        # Case 1: Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] < ans:
                ans = arr[low]
                minIdx = low
            low = mid + 1
        # Case 2: Right half is sorted
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                minIdx = mid
            high = mid - 1
            
    return minIdx

arr_dup = [3, 4, 4, 5, 5, 1, 2, 2]
print(f"Optimal Solution (Duplicates): {timesArrayRotatedDuplicates(arr_dup)}")

# Note: Your original print statement for the duplicate case was calling the wrong function.
# I have corrected it to call `timesArrayRotatedDuplicates`.
'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **Array not rotated (k=0):** The `if arr[low] <= arr[high]` optimization handles this
#   correctly for the distinct case. For the duplicate case, it will still find the
#   minimum at index 0.
# - **Ambiguous duplicates:** The `arr[low] == arr[mid] == arr[high]` check is the most
#   critical part for the duplicates version.

# **2. Common Follow-up Questions & Variations:**
# 1.  **Why not just use the duplicates-aware function for all cases?** You could. It works
#     for distinct arrays too. However, the distinct-only version has a slightly cleaner
#     logic and a guaranteed O(log n) performance, whereas the duplicates version can
#     degrade to O(n) in the worst case. It's good to know both.
# 2.  **Is there a way to solve this without tracking both `minE` and `minIdx`?** Yes.
#     A more streamlined approach is to just track the index. The logic would be: if
#     `arr[mid]` is a better candidate for the minimum than the current best index, update
#     the index. This avoids tracking the minimum value itself. However, the current
#     approach is very clear and explicit.
'''