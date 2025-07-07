from typing import List

# ------------------------------------------------------------
# 🧠 PROBLEM: LONGEST SUBARRAY WITH SUM = K
# ------------------------------------------------------------
# Given an array of integers and an integer k, find the length of the longest
# subarray whose sum is equal to k.
#
# 🔸 Input: arr = [1,2,3,1,1,1,1,4,2,3], k = 3
# 🔸 Output: 3  → subarray [1,1,1] or [3]

# ------------------------------------------------------------
# 🐌 1. BRUTE FORCE APPROACH — O(n^2)
# ------------------------------------------------------------
# 🔍 Intuition:
# - Check every possible subarray (i, j) and calculate its sum.
# - If sum equals k, update the max length.

# TIME: O(n^2)
# SPACE: O(1)

def longestSubArraySumKBrute(arr: List[int], k: int) -> int:
    n = len(arr)
    
    # Edge case: single element array
    if n == 1:
        return 1 if arr[0] == k else -1

    res = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == k:
                res = max(res, j - i + 1)
    
    return res

arr = [1,2,3,1,1,1,1,4,2,3]
k = 3
print(longestSubArraySumKBrute(arr, k))  # Output: 3

# ------------------------------------------------------------
# 🧠 2. BETTER APPROACH — PREFIX SUM + HASHMAP
# ------------------------------------------------------------
# 🔍 Intuition:
# - Keep a running sum `sum` while traversing the array.
# - If `sum == k`, update maxLen.
# - Store the first occurrence of each prefix sum in a hashmap.
# - If (sum - k) exists in map, then subarray [map[sum-k] + 1 to i] has sum k.
#
# ✅ Works with negative numbers too.

# TIME: O(n)
# SPACE: O(n)

def longestSubArraySumKBetter(arr: List[int], k: int) -> int:
    prefixSum = {}   # {prefix_sum: first_index}
    n = len(arr)
    maxLen = 0
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum == k:
            maxLen = i + 1

        rem = sum - k
        if rem in prefixSum:
            start_idx = prefixSum[rem]
            maxLen = max(maxLen, i - start_idx)
        
        if sum not in prefixSum:
            prefixSum[sum] = i  # store only the first occurrence

    return maxLen

arr = [1,2,3,1,1,1,1,4,2,3]
k = 3
print(longestSubArraySumKBetter(arr, k))  # Output: 3

# ------------------------------------------------------------
# ⚡ 3. OPTIMAL (TWO POINTER / SLIDING WINDOW)
# ------------------------------------------------------------
# 🔍 Intuition:
# - Works only for **non-negative** integers.
# - Maintain a window [j to i] and keep increasing `i`, shrinking `j` when sum > k.
#
# ➕ Fastest solution, but only when array has no negatives.

# TIME: O(n)
# SPACE: O(1)

def longestSubArraySumKOp(arr: List[int], k: int) -> int:
    n = len(arr)
    i, j = 0, 0
    sum = 0
    maxLen = 0

    while i < n:
        sum += arr[i]

        # Shrink window if sum > k
        while sum > k and j <= i:
            sum -= arr[j]
            j += 1

        # Check for valid window
        if sum == k:
            maxLen = max(maxLen, i - j + 1)

        i += 1

    return maxLen

arr = [1,2,3,1,1,1,1,4,2,3]
k = 3
print(longestSubArraySumKOp(arr, k))  # Output: 3

# ------------------------------------------------------------
# 🔍 DRY RUN EXAMPLE (Prefix Sum)
# ------------------------------------------------------------
# arr = [1, 2, 3], k = 3
#
# i=0, sum=1 → store {1:0}
# i=1, sum=3 → sum == k → maxLen = 2
# i=2, sum=6 → rem = 6-3=3 → 3 in map? yes → maxLen = max(2, 2-1) = 2
# Result = 2