from typing import List

# ------------------------------------------------------------
# 🧠 PROBLEM: TWO SUM
# ------------------------------------------------------------
# ✅ Find two elements in the array such that their sum is equal to the target.
# ✅ Return the indices of those two elements.
#
# 🔸 Input: arr = [4,5,3,2,1], target = 5
# 🔸 Output: [2, 4]  → 3 + 2 = 5

# ------------------------------------------------------------
# 🐌 1. BRUTE FORCE APPROACH
# ------------------------------------------------------------
# 🔍 Intuition:
# - Check every pair of elements (i, j)
# - If arr[i] + arr[j] == k, return [i, j]

# ❓ WHY `j` starts from `i+1`?
# - To avoid duplicate pairs and ensure we don’t add the same element twice.
# - Also avoids checking (i, j) and (j, i) both, since they’re same in this context.

# TIME: O(n^2)
# SPACE: O(1)

def TwoSumProblem(arr: List[int], k: int) -> List[int]:
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):  # start from i + 1 to avoid repeating pairs and i == j
            if arr[i] + arr[j] == k:
                return [i, j]

    return []

arr = [4,5,3,2,1]
k = 5
print(TwoSumProblem(arr, k))  # Output: [2, 4] or similar valid pair

# ------------------------------------------------------------
# ⚡ 2. HASHING APPROACH (Optimal for Index-Based Return)
# ------------------------------------------------------------
# 🔍 Intuition:
# - Traverse the array and keep track of seen elements in a hashmap.
# - For each element `a`, check if (target - a) exists in the map.
# - If yes, we found our pair.

# ✅ Does not require array to be sorted.
# ✅ Best for returning **original indices**.

# TIME: O(n)
# SPACE: O(n)

def TwoSumProblemBetter(arr: List[int], target: int) -> List[int]:
    hash_table = {}  # {value: index}

    for i, a in enumerate(arr):
        rem = target - a
        if rem in hash_table:
            return [hash_table[rem], i]
        hash_table[a] = i

    return [-1, -1]

arr = [4,5,3,2,1]
k = 5
print(TwoSumProblemBetter(arr, k))  # Output: [2, 4]

# ------------------------------------------------------------
# 🚀 3. TWO POINTER APPROACH (Only Works on Sorted Arrays)
# ------------------------------------------------------------
# 🔍 Intuition:
# - First, store original index with each value → [(val, index)]
# - Sort the array by value
# - Use two pointers (i and j) to move inward until the sum equals the target.

# ⚠️ Only use this if:
#   - You’re allowed to sort the array
#   - Or if returning actual indices is not necessary
#   - Otherwise, use hashing approach

# TIME: O(n log n) (due to sort)
# SPACE: O(n)

def TwoSumProblemOp(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    arr = [(nums[i], i) for i in range(n)]  # Store value and original index
    arr.sort(key=lambda x: x[0])           # Sort by value

    i, j = 0, n - 1

    while i < j:
        sum = arr[i][0] + arr[j][0]

        if sum == target:
            idx1, idx2 = arr[i][1], arr[j][1]
            return [min(idx1, idx2), max(idx1, idx2)]
        elif sum < target:
            i += 1
        else:
            j -= 1

    return [-1, -1]

arr = [4,5,3,2,1]
k = 5
print(TwoSumProblemOp(arr, k))  # Output: [2, 4] or [3, 0] depending on sort