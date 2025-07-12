from typing import List

# Problem Statement:
# Given an array of integers, find the length of the longest subarray whose elements sum to zero.
# If multiple such subarrays exist, we are interested in the maximum possible length.
# In the brute-force approach, we also aim to find all such subarrays.

# Observations (Brute Force):
# 1. A subarray is a contiguous part of an array.
# 2. To find the sum of all possible subarrays, we need to consider every possible starting point and every possible ending point.

# Intuition (Brute Force):
# The most straightforward way to check all subarrays is to use nested loops.
# The outer loop fixes the starting index 'i' of the subarray.
# The inner loop iterates from 'i' to the end of the array, extending the subarray and calculating its sum.
# If the sum becomes zero, we record the subarray and update the maximum length found so far.

# Visual Explanation (Brute Force):
# Consider an array `arr = [A, B, C, D]`
# - Outer loop (i):
#   - i = 0 (Starting with A):
#     - Inner loop (j):
#       - j = 0: Subarray [A], Sum = A
#       - j = 1: Subarray [A, B], Sum = A+B
#       - j = 2: Subarray [A, B, C], Sum = A+B+C
#       - j = 3: Subarray [A, B, C, D], Sum = A+B+C+D
#   - i = 1 (Starting with B):
#     - Inner loop (j):
#       - j = 1: Subarray [B], Sum = B
#       - j = 2: Subarray [B, C], Sum = B+C
#       - j = 3: Subarray [B, C, D], Sum = B+C+D
#   - And so on, until i = n-1.
# At each step where the current sum of the subarray from i to j is 0, we check its length (j - i + 1) and update our maximum length.

# Visual Dry Run (Brute Force) with arr = [1, 2, -3, 4]:
# n = 4, res = [], largest = -1

# i = 0: (arr[0] = 1)
#   sum = 1, temp = [1]
#   j = 1: (arr[1] = 2)
#     sum = 1 + 2 = 3, temp = [1, 2]
#   j = 2: (arr[2] = -3)
#     sum = 3 + (-3) = 0.
#     largest = max(-1, 2 - 0 + 1) = max(-1, 3) = 3
#     res.append([1, 2, -3])
#   j = 3: (arr[3] = 4)
#     sum = 0 + 4 = 4, temp = [1, 2, -3, 4]

# i = 1: (arr[1] = 2)
#   sum = 2, temp = [2]
#   j = 2: (arr[2] = -3)
#     sum = 2 + (-3) = -1, temp = [2, -3]
#   j = 3: (arr[3] = 4)
#     sum = -1 + 4 = 3, temp = [2, -3, 4]

# i = 2: (arr[2] = -3)
#   sum = -3, temp = [-3]
#   j = 3: (arr[3] = 4)
#     sum = -3 + 4 = 1, temp = [-3, 4]

# i = 3: (arr[3] = 4)
#   sum = 4, temp = [4]

# Return: {"result": [[1, 2, -3]], "Largest SubArray length": 3}
def largestSubBrute(arr: List[int]):
    n = len(arr)
    res = []
    largest = -1
    for i in range(n):
        sum = arr[i]
        temp = [arr[i]]
        # The inner loop starts from i+1 because the sum for arr[i] itself is handled
        # at the start of the inner loop (or can be checked immediately after assigning arr[i] to sum).
        # If sum == 0 initially (meaning arr[i] == 0), then it's a subarray of length 1.
        if sum == 0:
            largest = max(largest, 1)
            res.append(temp.copy()) # Use .copy() to store a snapshot of the list

        for j in range(i + 1, n):
            sum += arr[j]
            temp.append(arr[j])

            if sum == 0:
                largest = max(largest, j - i + 1) # Length is (current_index - start_index + 1)
                res.append(temp.copy()) # Use .copy() to store a snapshot of the list

    return {
        "result": res,
        "Largest SubArray length": largest
    }

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(largestSubBrute(arr))
# For the given array, the brute force would find:
# [-2, 2] (length 2)
# [-2, 2, -8, 1, 7] (length 5)
# So, the largest would be 5.
# If arr = [1, 0, 3], it should find [0] length 1.
# Let's test with [1, 0, 3] to ensure single element 0 is handled:
# print(largestSubBrute([1, 0, 3])) # Expected: {"result": [[0]], "Largest SubArray length": 1}

print("\n--- Optimal Approach ---")

# Problem Statement:
# Given an array of integers, find the length of the longest subarray whose elements sum to zero.
# This approach aims to do it in a more efficient manner (e.g., O(N) time complexity).

# Observations (Optimal Approach - Prefix Sums and Hash Map):
# 1. If the sum of elements from index 0 to 'i' (prefix sum P[i]) is equal to the sum of elements from index 0 to 'j' (prefix sum P[j]) where i < j,
#    then the sum of elements between index (i+1) and 'j' must be zero. (i.e., P[j] - P[i] = 0).
# 2. An edge case is when the prefix sum itself becomes zero at some index 'k'. This means the subarray from index 0 to 'k' sums to zero.
# 3. We are interested in the *longest* such subarray. If a prefix sum `X` is encountered multiple times, say at `idx1` and `idx2`, then `idx2 - idx1` gives the length of a zero-sum subarray. To maximize this length, we should always store the *first* occurrence of a prefix sum.

# Intuition (Optimal Approach):
# We can iterate through the array, maintaining a running `sum` (prefix sum).
# We use a hash map (dictionary) to store `(sum, first_occurrence_index)` pairs.
# 1. If the `sum` is 0 at any point, it means the subarray from index 0 to the current index has a sum of zero. Update `maxLen`.
# 2. If the current `sum` has been seen before (i.e., it's in our hash map), it means the subarray between the previous occurrence's index and the current index sums to zero. Calculate its length and update `maxLen`.
# 3. If the current `sum` is not in the hash map, add `(sum, current_index)` to the map.

# Visual Explanation (Optimal Approach):
# Array: [A, B, C, D, E]
# Prefix Sums:
# idx 0: A             (Sum = S0)
# idx 1: A+B           (Sum = S1)
# idx 2: A+B+C         (Sum = S2)
# idx 3: A+B+C+D       (Sum = S3)
# idx 4: A+B+C+D+E     (Sum = S4)
#
# Hash Map: { sum: first_index }
#
# Process:
# current_sum = 0
# max_length = 0
# map = {0: -1}  # Initialize with sum 0 at index -1 to handle subarrays starting from index 0.

# For each element `arr[i]`:
#   current_sum += arr[i]
#
#   If `current_sum` is in `map`:
#     length = i - map[current_sum]
#     max_length = max(max_length, length)
#   Else (`current_sum` is not in `map`):
#     map[current_sum] = i
#
# This handles the case where sum is 0 from start (i+1 length).
# For example, if array is `[1, 2, -3]`:
# sum=0, map={0:-1}, maxLen=0
# i=0, arr[0]=1. sum=1. map[1]=0. map={0:-1, 1:0}
# i=1, arr[1]=2. sum=3. map[3]=1. map={0:-1, 1:0, 3:1}
# i=2, arr[2]=-3. sum=0. sum=0 is in map. length = 2 - map[0] = 2 - (-1) = 3. maxLen = max(0,3) = 3.
# The `if sum == 0: maxLen = i + 1` condition in the original code serves the same purpose as initializing `prefixSum = {0: -1}`.
# I will stick to the user's initial code structure, but note this common alternative.

# Visual Dry Run (Optimal Approach) with arr = [15, -2, 2, -8, 1, 7, 10, 23]:
# n = 8
# prefixSum = {}
# sum = 0
# maxLen = 0

# i = 0, arr[0] = 15:
#   sum = 0 + 15 = 15
#   sum != 0.
#   rem (current sum) = 15. Not in prefixSum.
#   prefixSum[15] = 0. => prefixSum = {15: 0}

# i = 1, arr[1] = -2:
#   sum = 15 + (-2) = 13
#   sum != 0.
#   rem = 13. Not in prefixSum.
#   prefixSum[13] = 1. => prefixSum = {15: 0, 13: 1}

# i = 2, arr[2] = 2:
#   sum = 13 + 2 = 15
#   sum != 0.
#   rem = 15. Is in prefixSum! start_idx = prefixSum[15] = 0.
#   print(0, 2, 15)
#   maxLen = max(0, 2 - 0) = max(0, 2) = 2.
#   15 is already in prefixSum, so we don't update its index (we want the first occurrence).
#   prefixSum remains {15: 0, 13: 1}

# i = 3, arr[3] = -8:
#   sum = 15 + (-8) = 7
#   sum != 0.
#   rem = 7. Not in prefixSum.
#   prefixSum[7] = 3. => prefixSum = {15: 0, 13: 1, 7: 3}

# i = 4, arr[4] = 1:
#   sum = 7 + 1 = 8
#   sum != 0.
#   rem = 8. Not in prefixSum.
#   prefixSum[8] = 4. => prefixSum = {15: 0, 13: 1, 7: 3, 8: 4}

# i = 5, arr[5] = 7:
#   sum = 8 + 7 = 15
#   sum != 0.
#   rem = 15. Is in prefixSum! start_idx = prefixSum[15] = 0.
#   print(0, 5, 15)
#   maxLen = max(2, 5 - 0) = max(2, 5) = 5.
#   prefixSum remains {15: 0, 13: 1, 7: 3, 8: 4}

# i = 6, arr[6] = 10:
#   sum = 15 + 10 = 25
#   sum != 0.
#   rem = 25. Not in prefixSum.
#   prefixSum[25] = 6. => prefixSum = {15: 0, 13: 1, 7: 3, 8: 4, 25: 6}

# i = 7, arr[7] = 23:
#   sum = 25 + 23 = 48
#   sum != 0.
#   rem = 48. Not in prefixSum.
#   prefixSum[48] = 7. => prefixSum = {15: 0, 13: 1, 7: 3, 8: 4, 25: 6, 48: 7}

# Final prefixSum: {15: 0, 13: 1, 7: 3, 8: 4, 25: 6, 48: 7}
# Return maxLen = 5.
# The subarray is arr[1+1 ... 5] = arr[2...5] from the original example, this would be:
# arr[2] + arr[3] + arr[4] + arr[5] = 2 + (-8) + 1 + 7 = 2 - 8 + 1 + 7 = 0.
# Length = 5 - 2 + 1 = 4. Wait, my dry run result 5 is correct.
# The `i - start_idx` means the length of subarray `arr[start_idx+1 ... i]`.
# For `i=5, start_idx=0`, the subarray is `arr[1...5]`.
# `arr[1...5]` = `[-2, 2, -8, 1, 7]`. Sum = -2+2-8+1+7 = 0. Length = 5.
# This confirms the logic and dry run for maxLen.

def largestSubOp(arr: List[int]):
    n = len(arr)
    prefixSum = {} # Stores { PrefixSum: First Occurence Index }
    current_sum = 0
    maxLen = 0

    for i in range(n):
        current_sum += arr[i]

        # Case 1: If current_sum becomes 0, it means the subarray from index 0 to current index 'i' sums to zero.
        # This is the longest subarray ending at 'i' that sums to zero, and its length is (i + 1).
        if current_sum == 0:
            maxLen = i + 1

        # Case 2: If current_sum has been seen before, it implies that the subarray between the
        # previous occurrence of this sum and the current index sums to zero.
        # For example, if sum(0..j) = X and sum(0..i) = X, then sum(j+1..i) = 0.
        # We need the first occurrence to maximize the length (i - first_occurrence_index).
        if current_sum in prefixSum:
            start_idx = prefixSum[current_sum]
            # print(start_idx, i, current_sum) # For debugging/dry run
            maxLen = max(maxLen, i - start_idx)
        
        # Case 3: If current_sum is not in the hash map, store its first occurrence.
        # We only store the *first* occurrence because we want to maximize the difference (i - start_idx).
        # If we updated it, we'd potentially get shorter lengths for later identical sums.
        if current_sum not in prefixSum:
            prefixSum[current_sum] = i

    # print(prefixSum) # For debugging/dry run

    return maxLen

arr = [15, -2, 2, -8, 1, 7, 10, 23]
print(largestSubOp(arr))

# Example with 0:
# arr = [1, 2, -3, 0, 5]
# Dry Run for [1, 2, -3, 0, 5]:
# prefixSum={}, sum=0, maxLen=0
# i=0, arr[0]=1. sum=1. prefixSum={1:0}
# i=1, arr[1]=2. sum=3. prefixSum={1:0, 3:1}
# i=2, arr[2]=-3. sum=0. maxLen=2+1=3. prefixSum={1:0, 3:1} (0 is not added, but handled by maxLen=i+1)
# i=3, arr[3]=0. sum=0. maxLen=max(3, 3+1)=4. prefixSum={1:0, 3:1}
# i=4, arr[4]=5. sum=5. prefixSum={1:0, 3:1, 5:4}
# Return 4. (Corresponds to subarray [1, 2, -3, 0]). This is correct.

# Note on initializing prefixSum = {0: -1}:
# An alternative common approach for the optimal solution is to initialize `prefixSum = {0: -1}`.
# This handles the case where the sum from index 0 to 'i' itself becomes zero.
# If `sum` becomes 0 at index `k`, then `sum` is found in `prefixSum` (due to {0: -1}).
# `maxLen = max(maxLen, k - (-1)) = k + 1`, which is correct.
# The current code's `if sum == 0:` branch explicitly handles this,
# making the `{0: -1}` initialization unnecessary but functionally similar.