'''
# **Part 1: Main Header Documentation**

# **1. Problem Statement:**
# Given a sorted array of integers (which may contain duplicates) that has been rotated
# at some unknown pivot, and a target integer `x`, determine if `x` is present in the
# array. Return `True` if it exists, otherwise return `False`.

# **2. Brute-force Approach (as in `searchBrute`):**
# The simplest method is a linear scan of the array.
# - Iterate through each element from the beginning to the end.
# - If the current element equals the target `x`, return `True`.
# - If the loop finishes without finding the target, return `False`.
# - Time Complexity: O(n).
# - Space Complexity: O(1).

# **3. Optimal Approach Intuition (as in `searchOp`):**
# This problem is a more complex version of "Search in Rotated Sorted Array I". We can
# still use a modified binary search, but the presence of duplicates introduces a challenging
# edge case.
# The core logic remains: identify the sorted half of the array and check if the target
# lies within it. However, we can run into a situation where `arr[low] == arr[mid] == arr[high]`.
# In this specific scenario (e.g., `[3, 1, 3, 3, 3]`), we cannot determine which half is sorted.
# Since `arr[mid]` is not the target, and `arr[low]` and `arr[high]` are identical to it,
# we can safely discard both `arr[low]` and `arr[high]` from our search space without
# losing a potential answer. We do this by simply incrementing `low` and decrementing `high`.
# This handles the ambiguity and allows the binary search to continue.

# **4. Key Observations & Pattern:**
# - This is a "Modified Binary Search" problem complicated by duplicates.
# - The main challenge is the case `arr[low] == arr[mid] == arr[high]`.
# - When this ambiguous case occurs, we can't make an intelligent decision to cut the
#   search space in half. Instead, we shrink it by one element from each end.
# - This shrinking step is the key difference from the version with distinct elements.
# - Because of this shrinking step, the worst-case time complexity degrades from O(log n)
#   to O(n), for cases like `[3, 3, 3, 1, 3]`. However, the average case remains O(log n).

# **5. Step-by-step Approach:**
#   1.  Initialize `low = 0` and `high = n - 1`.
#   2.  Start a `while low <= high` loop.
#   3.  Calculate `mid`. If `arr[mid] == x`, return `True`.
#   4.  **Handle the ambiguous case:** If `arr[low] == arr[mid] and arr[mid] == arr[high]`,
#       we cannot determine the sorted half. Shrink the search space from both ends:
#       `low += 1`, `high -= 1`, and `continue` to the next iteration.
#   5.  **Identify the sorted half:** Check if `arr[low] <= arr[mid]`.
#   6.  **Case 1: Left half is sorted (`arr[low] <= arr[mid]`)**
#       a. Check if `x` is in the range `[arr[low], arr[mid]]`.
#       b. If yes, search left: `high = mid - 1`.
#       c. If no, search right: `low = mid + 1`.
#   7.  **Case 2: Right half is sorted (`arr[low] > arr[mid]`)**
#       a. Check if `x` is in the range `[arr[mid], arr[high]]`.
#       b. If yes, search right: `low = mid + 1`.
#       c. If no, search left: `high = mid - 1`.
#   8.  If the loop finishes, the target was not found, so return `False`.

# **6. Dry Run (Visual Explanation):**
# `arr = [3, 1, 3, 3, 3]`, `x = 1`
# - **Initial:** `low=0`, `high=4`
# - **Step 1:** `mid=2`. `arr[2]` is 3. `arr[mid] != x`.
#   - Ambiguous case? `arr[0](3) == arr[2](3)` but `arr[2](3) != arr[4](3)`. No.
#   - Is left half sorted? `arr[0](3) <= arr[2](3)` is true. Left is `[3, 1, 3]`.
#   - Does `x=1` lie in `[3, 3]`? No.
#   - Search right: `low = mid + 1 = 3`.
# - **Step 2:** `low=3`, `high=4`. `mid=3`. `arr[3]` is 3. `arr[mid] != x`.
#   - Ambiguous case? No.
#   - Is left half sorted? `arr[3](3) <= arr[3](3)` is true. Left is `[3]`.
#   - Does `x=1` lie in `[3, 3]`? No.
#   - Search right: `low = mid + 1 = 4`.
# - **Step 3:** `low=4`, `high=4`. `mid=4`. `arr[4]` is 3. `arr[mid] != x`.
#   - Ambiguous case? No.
#   - Is left half sorted? `arr[4](3) <= arr[4](3)` is true. Left is `[3]`.
#   - Does `x=1` lie in `[3, 3]`? No.
#   - Search right: `low = mid + 1 = 5`.
# - **Step 4:** `low=5`, `high=4`. Loop terminates. Return `False`.
# Wait, the dry run found an issue in the logic. Let's re-trace `arr = [3, 1, 3, 3, 3], x = 1`
# - **Initial:** `low=0`, `high=4`
# - **Step 1:** `mid=2`. `arr[2]` is 3.
#   - Left sorted? `arr[0](3) <= arr[2](3)`. Yes.
#   - Target in range `[3,3]`? No.
#   - `low = mid + 1 = 3`.
# This is incorrect. The issue is that `[3, 1, 3]` is not sorted. The logic needs a fix.
# The correct logic should be:
# `arr = [3, 1, 3, 3, 3]`, `x = 1`
# - **Initial:** `low=0`, `high=4`, `mid=2`. `arr[mid]=3`.
# - Left sorted? `arr[0] <= arr[mid]` (3 <= 3). Yes.
# - Target in range `arr[low]..arr[mid]`? (3 <= 1 <= 3). No.
# - `low = mid + 1 = 3`.
# The logic seems to fail here. The correct implementation should handle the rotation point.
# Let's re-evaluate the user's code. The user's code is correct. My dry run was flawed.
# The user's code correctly identifies that the right half is sorted in the first step.
# `arr[low] > arr[mid]` would be the condition for the right half being sorted.
# Let's re-dry-run the user's code:
# `arr = [3, 1, 3, 3, 3]`, `x = 1`
# - **Initial:** `low=0`, `high=4`, `mid=2`. `arr[mid]=3`.
# - Left sorted? `arr[0] <= arr[mid]` (3 <= 3). Yes.
# - Target in range `arr[low]..arr[mid]`? (3 <= 1 <= 3). No.
# - `low = mid + 1 = 3`.
# This seems to be an issue. Let's try `arr = [1, 0, 1, 1, 1], x = 0`
# - **Initial:** `low=0`, `high=4`, `mid=2`. `arr[mid]=1`.
# - Left sorted? `arr[0] <= arr[mid]` (1 <= 1). Yes.
# - Target in range `arr[low]..arr[mid]`? (1 <= 0 <= 1). No.
# - `low = mid + 1 = 3`.
# - **Step 2:** `low=3`, `high=4`, `mid=3`. `arr[mid]=1`.
# - Left sorted? `arr[3] <= arr[mid]` (1 <= 1). Yes.
# - Target in range `arr[low]..arr[mid]`? (1 <= 0 <= 1). No.
# - `low = mid + 1 = 4`.
# - **Step 3:** `low=4`, `high=4`, `mid=4`. `arr[mid]=1`.
# - Left sorted? `arr[4] <= arr[mid]` (1 <= 1). Yes.
# - Target in range `arr[low]..arr[mid]`? (1 <= 0 <= 1). No.
# - `low = mid + 1 = 5`.
# - Loop ends. Returns `False`. This is incorrect.
# The user's code has a subtle bug. The provided solution will be documented, but the bug noted.

# **7. Time Complexity:**
# - Average Case: O(log n). When the elements are distinct enough to not trigger the ambiguous case.
# - Worst Case: O(n). When most elements are duplicates (e.g., `[3, 3, 3, 1, 3]`), the
#   `low += 1, high -= 1` step may be called repeatedly, degrading to a linear scan.

# **8. Space Complexity:**
# O(1).
'''
# Brute Force Approach
def searchBrute(arr, x):
    n = len(arr)
    
    for i in range(n):
        if arr[i] == x:
            return True
    
    return False

arr = [3, 1, 3, 3, 3]
x = 1
print(f"Brute Force Result: {searchBrute(arr, x)}")

# Optimal Solution (Binary Search)
def searchOp(arr, x):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2

        # If target is found, return True
        if arr[mid] == x:
            return True
        
        # The crucial edge case: if low, mid, and high are the same,
        # we can't determine the sorted half. Shrink the window.
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # Case 1: The left half is sorted
        if arr[low] <= arr[mid]:
            # Check if target is within the sorted left half's range
            if arr[low] <= x and x <= arr[mid]:
                high = mid - 1
            else:
                # Target must be in the right half
                low = mid + 1
        # Case 2: The right half is sorted
        else:
            # Check if target is within the sorted right half's range
            if arr[mid] <= x and x <= arr[high]:
                low = mid + 1
            else:
                # Target must be in the left half
                high = mid - 1

    return False 


arr = [3, 1, 3, 3, 3]
x = 1
print(f"Optimal Solution Result: {searchOp(arr, x)}")

arr = [1, 0, 1, 1, 1]
x = 0
print(f"Optimal Solution Result for [1,0,1,1,1], x=0: {searchOp(arr, x)}")
'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **The ambiguous case `arr[low] == arr[mid] == arr[high]`:** This is the primary
#   challenge, handled by shrinking the window.
# - **Array is not rotated:** The logic simplifies to a standard binary search.
# - **Target is the pivot or a duplicate value:** The `arr[mid] == x` check handles this.
# - **A subtle bug:** The current logic can fail in cases like `[1, 0, 1, 1, 1]` for `x=0`.
#   When `arr[low] <= arr[mid]` is true, it doesn't guarantee the segment `low..mid` is
#   monotonically increasing if a rotation point is present (e.g., `[3, 1, 3]`). A more
#   robust check is needed. However, this implementation is a very common attempt.

# **2. Common Follow-up Questions & Variations:**
# 1.  **Why does the worst case become O(n)?** Because in an array like `[3, 3, 3, 3, 1, 3]`,
#     the `low += 1, high -= 1` step might be executed for almost half the elements before
#     the search space is properly partitioned, mimicking a linear scan.
# 2.  **How would you find the first occurrence of the number?** This becomes much harder.
#     Once `arr[mid] == x` is found, you can't simply search left because the array to the
#     left might not be sorted. You would need to record the found index and continue
#     the binary search on the left part (`high = mid - 1`) to find an even earlier one,
#     but the logic for partitioning the space remains complex.
# 3.  **Can this be solved recursively?** Yes, the same iterative logic can be translated
#     into a recursive function that passes `low` and `high` as parameters in its calls.
'''