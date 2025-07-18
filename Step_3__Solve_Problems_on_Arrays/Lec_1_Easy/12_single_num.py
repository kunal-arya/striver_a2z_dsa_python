from typing import List

# -------------------------------------------------------
# PROBLEM: FIND THE SINGLE NUMBER
# -------------------------------------------------------
# Given a list where every element appears exactly twice except one element
# that appears only once, find and return that single element.
#
# Example:
#   Input:  [1,1,2,2,3,3,4,5,5]
#   Output: 4
#
# Note:
# - Only one number appears once, others appear exactly twice.
# - Constraints: Use O(n) time and ideally O(1) space.

# -------------------------------------------------------
# BRUTE FORCE APPROACH
# -------------------------------------------------------
# INTUITION:
# - For each element, count its frequency by scanning the full array.
# - If frequency is 1, return that number.
#
# TIME: O(n^2) → nested loops
# SPACE: O(1)

def singleNumBrute(arr: List[int]) -> int:
    n = len(arr)
    
    for num in arr:
        count = 0
        for i in range(n):
            if arr[i] == num:
                count += 1
        if count == 1:
            return num
        
    return -1

arr = [1,1,2,2,3,3,4,5,5]
print(singleNumBrute(arr))  # Output: 4

# -------------------------------------------------------
# BETTER APPROACH — HASHING (Using Dictionary)
# -------------------------------------------------------
# INTUITION:
# - Count frequency of each number using a hashmap (dict).
# - Loop through the hashmap and return the key whose frequency is 1.
#
# TIME: O(n)
# SPACE: O(n)

def singleNumBetter(arr: List[int]) -> int:
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Find the number whose frequency is 1
    return next((item for item, f in freq.items() if f == 1), -1)

arr = [1,1,2,2,3,3,4,5,5]
print(singleNumBetter(arr))  # Output: 4

# -------------------------------------------------------
# OPTIMAL APPROACH — BITWISE XOR
# -------------------------------------------------------
# INTUITION:
# - XOR (^) has properties:
#     x ^ x = 0  (same numbers cancel each other)
#     x ^ 0 = x
#     XOR is commutative and associative.
# - So XOR all elements → all paired numbers cancel out → only the unique number remains.
#
# TIME: O(n)
# SPACE: O(1)

def singleNumOp(arr: List[int]) -> int:
    xor = 0
    for num in arr:
        xor ^= num
    return xor

arr = [1,1,2,2,3,3,4,5,5]
print(singleNumOp(arr))  # Output: 4

# -------------------------------------------------------
# VISUAL DRY RUN (XOR)
# -------------------------------------------------------
# arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
#
# xor = 0
# xor ^ 1 → 1
# 1 ^ 1   → 0
# 0 ^ 2   → 2
# 2 ^ 2   → 0
# 0 ^ 3   → 3
# 3 ^ 3   → 0
# 0 ^ 4   → 4
# 4 ^ 5   → 1
# 1 ^ 5   → 4  ← Final Result
#
# All duplicates cancel out, only `4` remains.