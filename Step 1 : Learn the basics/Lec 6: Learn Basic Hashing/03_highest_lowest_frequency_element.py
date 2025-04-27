# ========================
# 📚 Highest Frequency Element after at most K Increments
# ========================

# 🚀 Problem Understanding:
# - You can increment any element by 1 in one operation.
# - Goal: Maximize the frequency of any number after at most k operations.

# ⚡ When to think about this technique:
# - When you need to make elements equal.
# - When maximizing frequency after limited operations.
# - Sorting helps when relative difference matters.
# - Sliding window helps when dealing with contiguous or incremental ranges.


# ========================
# 🛠 Brute Force Approach
# ========================

def high_low_freq(arr, k):
    # Step 1: Sort the Array (smallest to largest)
    arr.sort()

    # Initialize maximum frequency and corresponding number
    max_freq = 1
    max_freq_num = arr[0]

    n = len(arr)

    # For each element, try to make previous elements equal to it
    for i in range(n):
        target = arr[i]
        count = 1
        total_operations = 0

        # Look back and see how many elements can be made equal to arr[i]
        for j in range(i - 1, -1, -1):
            operation_needed = target - arr[j]

            if total_operations + operation_needed <= k:
                total_operations += operation_needed
                count += 1
            else:
                break

        # Update the maximum frequency if a better one is found
        if count > max_freq:
            max_freq = count
            max_freq_num = target

    return max_freq, max_freq_num

# Example Usage (Brute Force)
arr = [1, 2, 4]
k = 5
print("Brute Force Result:", high_low_freq(arr, k))
# Output should be (3, 4)


# ========================
# 🏎 Optimized Approach (Sliding Window)
# ========================

# Intuition Behind Optimization:
# - Instead of checking every element individually (O(n^2)),
# - Use a sliding window to include as many elements as possible while total operations <= k.

# Time Complexity: O(n log n) because of sorting + O(n) pass.

def high_freq_op(arr, k):
    # Step 1: Sort the Array
    arr.sort()

    # Initialize pointers for sliding window
    l, r = 0, 0
    max_freq, total = 0, 0
    n = len(arr)

    # Slide the window
    while r < n:
        # Add current element to the total sum
        total += arr[r]

        # Condition Check:
        # - arr[r] * window_size > total + k means we need to shrink the window
        while arr[r] * (r - l + 1) > total + k:
            total -= arr[l]
            l += 1

        # Update maximum frequency
        max_freq = max(max_freq, r - l + 1)
        r += 1

    return max_freq

# Example Usage (Optimized)
arr = [1, 2, 4]
k = 5
print("Optimized Result:", high_freq_op(arr, k))
# Output should be 3


# ========================
# 🔥 Quick Summary
# ========================
#
# | Brute Force | Optimized |
# |:------------|:----------|
# | Sort array | Sort array |
# | For each element, check backwards using k | Two pointers sliding window |
# | O(N^2) | O(N log N) |
#
# 👉 When given k operations to make elements equal, SORT first!
# 👉 If optimization needed for frequencies/subarrays, think Sliding Window.
# 👉 Hashing is helpful if directly counting elements; not needed here.
