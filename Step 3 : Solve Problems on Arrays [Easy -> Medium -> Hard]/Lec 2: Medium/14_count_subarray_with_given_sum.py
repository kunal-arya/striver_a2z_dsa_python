from typing import List

# ------------------------------ #
# Brute Force Approach (O(n^3)) #
# ------------------------------ #

def countSubArraySumKBrute(arr: List[int], k: int):
    n = len(arr)
    count = 0

    # ✅ Intuition:
    # Try every possible subarray using 3 nested loops and check if its sum equals to k

    for i in range(n):  # Starting index of subarray
        for j in range(i, n):  # Ending index of subarray
            sum = 0
            for ki in range(i, j + 1):  # Add all elements between i and j
                sum += arr[ki]
            if sum == k:
                count += 1  # If subarray sum == k, count it

    return count

# 🔍 Visual Dry Run for arr = [1,1,1], k = 2:
# Subarrays checked: [1], [1,1], [1], [1,1], [1]
# Valid subarrays: [1,1] (at index 0–1) and [1,1] (at index 1–2)
# Total = 2

# 🧠 Visual Explanation:
# 1 1 1
# ↘↘   → sum = 2 ✅
#   ↘↘ → sum = 2 ✅

arr = [1, 1, 1]
k = 2
print(countSubArraySumKBrute(arr, k))  # Output: 2


# ------------------------------- #
# Better Approach (O(n^2))       #
# ------------------------------- #

def countSubArraySumKBetter(arr: List[int], k: int):
    n = len(arr)
    count = 0

    # ✅ Intuition:
    # Optimize by removing the 3rd loop.
    # Use only 2 loops and keep running sum in the inner loop.

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]  # Keep adding as we expand the subarray
            if sum == k:
                count += 1

    return count

# 🔍 Visual Dry Run for arr = [1,2,3], k = 3:
# i=0: sum=1 -> 3 ✅
# i=1: sum=2 -> 5
# i=2: sum=3 ✅
# Total = 2

arr = [1, 2, 3]
k = 3
print(countSubArraySumKBetter(arr, k))  # Output: 2


# ---------------------------------------------- #
# Optimal Approach (Prefix Sum + HashMap) O(n)   #
# ---------------------------------------------- #

def countSubArraySumKOp(arr: List[int], k: int) -> int:
    n = len(arr)
    prefix_count = {0: 1}  # Sum 0 is seen once initially
    total = 0
    count = 0

    # ✅ Intuition:
    # Use prefix sums and a hashmap to keep count of how many times a sum has occurred.
    # If (current_sum - k) has occurred before, then there exists a subarray ending at current index with sum k.

    for i in range(n):
        num = arr[i]
        total += num

        # Check if a subarray with sum 'k' ends at index i
        if total - k in prefix_count:
            count += prefix_count[total - k]

        # Update prefix_count for current total
        prefix_count[total] = prefix_count.get(total, 0) + 1

        # 🧠 Visual Explanation:
        # current total = sum(arr[0..i])
        # if there’s any prefix sum == total - k,
        # then arr[j+1..i] has sum == k

    return count

# 🔍 Visual Dry Run:
# arr = [1,2,3,-3,1,1,1,4,2,-3], k = 3
# Prefix Sums: 1,3,6,3,4,5,6,10,12,9
# Whenever (sum - k) exists in map, increment count

arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
k = 3
print(countSubArraySumKOp(arr, k))  # Output: 6
