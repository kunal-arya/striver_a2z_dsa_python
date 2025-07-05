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

# Visual Explanation 📊
#
# Problem: Make max number of elements equal using at most `k` increments
# Approach: For each arr[i], try to make previous elements equal to it
#
# Sorted Array ➝ [a0, a1, ..., ai-1, ai, ..., an]
#                           ↑ target
#        <---- Looping Backwards ----
#
# For each j in [i-1 ... 0]:
#     How much to add to arr[j] to make it == arr[i]?
#         operation_needed = arr[i] - arr[j]
#
#     Keep track of total_operations:
#         If total_operations + operation_needed <= k:
#             ✅ Make arr[j] == arr[i]
#             count += 1
#             total_operations += operation_needed
#         Else:
#             ❌ Stop (not enough k left)
#
# Goal: Find max `count` and corresponding number (arr[i])
#
# Example:
#   arr = [1, 2, 4]
#   k = 5
#
#   Sorted: [1, 2, 4]
#
#   Try to make all == 4:
#     4 - 2 = 2
#     4 - 1 = 3
#     Total = 5 (✅)
#     → count = 3 → best so far
#
# Time Complexity: O(N^2)
# Why Brute Force? Trying every possibility greedily with early stop

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

# Visual Dry Run 🧠
#
# Input: arr = [1, 2, 4], k = 5
# After sort ➝ [1, 2, 4]
#
# Iteration 1:
#   i = 0 → target = 1
#   [1, 2, 4]
#    ↑
#   No elements before → count = 1
#
# Iteration 2:
#   i = 1 → target = 2
#   [1, 2, 4]
#    ↑   ↑
#    j   i
#   2 - 1 = 1 → ✅ total = 1 ≤ k → count = 2
#
# Iteration 3:
#   i = 2 → target = 4
#   [1, 2, 4]
#    ↑   ↑   ↑
#    j   j   i
#   4 - 2 = 2 → ✅ total = 2
#   4 - 1 = 3 → ✅ total = 5 (within k) → count = 3
#
# Final Result:
# ➝ max_freq = 3, number = 4

# Example Usage (Brute Force)
arr = [1, 2, 4]
k = 5
print("Brute Force Result:", high_low_freq(arr, k))
# Output should be (3, 4)


# ========================
# 🏎 Optimized Approach (Sliding Window)
# ========================

# LINK FOR VIDEO: https://www.youtube.com/watch?v=vgBrQ0NM5vE

# Intuition Behind Optimization:
# - Instead of checking every element individually (O(n^2)),
# - Use a sliding window to include as many elements as possible while total operations <= k.

# Time Complexity: O(n log n) because of sorting + O(n) pass.

# Visual Explanation 📊
#
# Problem: Make max number of elements equal using at most `k` increments
# Optimized Approach: Sliding Window + Prefix Sum Logic
#
# Idea: Instead of checking each arr[i] by looping back,
#       Use a window [l ... r] and check:
#
#   Can we make all elements in window equal to arr[r] using ≤ k ops?
#
# Condition:
#   arr[r] * window_size ≤ total_sum + k
#
# Why? 
#   To make all elements equal to arr[r], total operations needed:
#       (arr[r] - arr[l]) + (arr[r] - arr[l+1]) + ... + (arr[r] - arr[r])
#     = arr[r] * window_size - sum(window elements)
#
# If this ≤ k, we can make all elements equal to arr[r]
#
# If not → shrink window from the left
#
# Sliding Window:
#   - r expands window to include more elements
#   - l shrinks window when total operations > k
#
# Track max window size (r - l + 1) → gives max frequency possible
#
# Example:
#   arr = [1, 2, 4], k = 5
#   Sorted: [1, 2, 4]
#
#   Try making elements equal to 4:
#     total = 1 + 2 + 4 = 7
#     4 * 3 = 12 → 12 > 7 + 5 → ❌ too costly → shrink left
#     Now: [2, 4] → total = 6 → 4 * 2 = 8 ≤ 6 + 5 → ✅
#
# Final Answer ➝ max_freq = 2
#
# Time Complexity: O(N log N) for sorting + O(N) for window
# Much faster than brute-force O(N^2)

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

# Visual Dry Run 🔍 (Sliding Window Approach)
#
# Input: arr = [1, 2, 4], k = 5
# After sort ➝ [1, 2, 4]
#
# Initialize:
#   l = 0, r = 0, total = 0, max_freq = 0
#
# Step-by-step Sliding Window:
#
# r = 0 → total = 1
# [1, 2, 4]
#  ↑
#  l,r
#   Check: 1 * 1 = 1 ≤ total + k (1 + 5) ✅
#   → max_freq = 1
#
# r = 1 → total = 1 + 2 = 3
# [1, 2, 4]
#  ↑  ↑
#  l  r
#   Check: 2 * 2 = 4 ≤ 3 + 5 ✅
#   → max_freq = 2
#
# r = 2 → total = 3 + 4 = 7
# [1, 2, 4]
#  ↑     ↑
#  l     r
#   Check: 4 * 3 = 12 > 7 + 5 → ❌ shrink window
#     ➝ total -= arr[l] → total = 6, l = 1
#
# [1, 2, 4]
#     ↑  ↑
#     l  r
#   Check: 4 * 2 = 8 ≤ 6 + 5 ✅
#   → max_freq = 2 (unchanged)
#
# r = 3 → end
#
# Final Answer:
# ➝ max_freq = 2

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
