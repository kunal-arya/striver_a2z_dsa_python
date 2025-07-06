from typing import List

# ------------------------------------------------------
# 🔍 PROBLEM STATEMENT
# ------------------------------------------------------
# Given an array, move all the zeroes to the end of the array
# while maintaining the relative order of non-zero elements.

# Example:
# Input  : [0, 1, 0, 3, 12]
# Output : [1, 3, 12, 0, 0]

# ------------------------------------------------------
# 💡 INTUITION
# ------------------------------------------------------
# - We want to preserve the relative order of non-zero elements.
# - All 0s must be shifted to the end, in-place if possible.
# - We can approach this in two ways:
#     1. Brute force: Use extra space to store non-zeroes, then fill remaining with 0s.
#     2. Optimized: Use two pointers to swap zeroes with non-zeroes in-place.

# ======================================================
# 🧪 BRUTE FORCE APPROACH
# ======================================================

def moveZeroesBrute(arr: List[int]) -> List[int]:
    n = len(arr)

    # Edge case
    if n == 1:
        return arr

    # Step 1: Collect all non-zero elements
    temp = []
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    d = len(temp)  # Count of non-zero elements

    # Step 2: Place non-zero elements at the start
    for i in range(d):
        arr[i] = temp[i]

    # Step 3: Fill the rest with 0s
    for i in range(d, n):
        arr[i] = 0

    return arr

# ------------------------------------------------------
# 🖼️ DRY RUN (Brute Force)
# ------------------------------------------------------
# Input:  [0, 1, 0, 3, 0, 0, 12, 3]
# temp = [1, 3, 12, 3]
# Fill first 4 positions → [1, 3, 12, 3, _, _, _, _]
# Fill rest with 0s      → [1, 3, 12, 3, 0, 0, 0, 0]

# ------------------------------------------------------
# ⏱️ TIME & SPACE COMPLEXITY (Brute)
# ------------------------------------------------------
# Time:  O(n)
# Space: O(n) — due to temp list

arr1 = [0, 1, 0, 3, 0, 0, 12, 3, 0, 5, 0, 0, 0, 3, 33]
print("Brute Output:", moveZeroesBrute(arr1.copy()))

# ======================================================
# ⚡ OPTIMIZED APPROACH — Two Pointers
# ======================================================

def moveZeroesOp(arr: List[int]) -> None:
    n = len(arr)
    j = -1  # Pointer to the first zero

    # Step 1: Find the first occurrence of 0
    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    # If there is no zero, no need to process
    if j == -1:
        return

    # Step 2: Traverse from j+1 to end
    # Swap non-zero elements with arr[j]
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

# ------------------------------------------------------
# 🖼️ DRY RUN (Optimized)
# ------------------------------------------------------
# Input : [0, 1, 0, 3, 0, 12]
# After finding j = 0
# i = 1: arr[1] = 1 → swap with arr[0] → [1, 0, 0, 3, 0, 12]
# j = 1
# i = 3: arr[3] = 3 → swap with arr[1] → [1, 3, 0, 0, 0, 12]
# j = 2
# i = 5: arr[5] = 12 → swap with arr[2] → [1, 3, 12, 0, 0, 0]

# Final Output: [1, 3, 12, 0, 0, 0]

# ------------------------------------------------------
# ⏱️ TIME & SPACE COMPLEXITY (Optimized)
# ------------------------------------------------------
# Time:  O(n)
# Space: O(1) — in-place swap

arr2 = [0, 1, 0, 3, 0, 0, 12, 3, 0, 5, 0, 0, 0, 3, 33]
moveZeroesOp(arr2)
print("Optimized Output:", arr2)