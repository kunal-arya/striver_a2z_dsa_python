# ------------------------------------------------------
# 🔍 PROBLEM STATEMENT
# ------------------------------------------------------
# Rotate an array to the left by 'd' positions.
# This means shift every element to the left d times,
# and the first d elements move to the end in order.

# Example:
# Input  : arr = [1, 2, 3, 4, 5, 6, 7], d = 3
# Output :       [4, 5, 6, 7, 1, 2, 3]

# ------------------------------------------------------
# 💡 INTUITION
# ------------------------------------------------------
# - For rotating d times to the left:
#   - The first d elements should go to the end.
#   - The rest should be moved forward to start from index 0.

# - This brute force approach uses an extra array `temp`
#   to store the first d elements temporarily.

# - After that:
#   - Shift remaining elements `arr[d:]` to the front.
#   - Then put the saved `temp` values at the end.

# ------------------------------------------------------
# 🧠 IMPLEMENTATION
# ------------------------------------------------------

def leftRotateBrute(arr, d):
    n = len(arr)

    # Edge case: Single-element array
    if n == 1:
        return arr

    # Handle cases where d >= n
    d = d % n

    # Step 1: Copy first d elements to temp array
    temp = []
    for i in range(d):
        temp.append(arr[i])

    # Step 2: Shift the rest of the array to the left
    for i in range(d, n):
        arr[i - d] = arr[i]

    # Step 3: Add temp elements at the end
    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]

    return arr

# ------------------------------------------------------
# 🖼️ DRY RUN EXAMPLE
# ------------------------------------------------------

# Input: arr = [1, 2, 3, 4, 5, 6, 7], d = 3

# Step 1: Store first 3 elements:
# temp = [1, 2, 3]

# Step 2: Shift remaining elements left:
# arr = [4, 5, 6, 7, 5, 6, 7]

# Step 3: Place temp at the end:
# i = 4 → arr[4] = temp[0] = 1
# i = 5 → arr[5] = temp[1] = 2
# i = 6 → arr[6] = temp[2] = 3

# Final Output: [4, 5, 6, 7, 1, 2, 3]

# ------------------------------------------------------
# ⏱️ TIME & SPACE COMPLEXITY
# ------------------------------------------------------
# Time Complexity  : O(n)       → 1 pass for temp, 1 for shift, 1 for replace
# Space Complexity : O(d)       → Extra space for temp array

# ------------------------------------------------------
# 💡 INTUITION
# ------------------------------------------------------
# Reverse Trick: Rotate Left by d is same as:
# 1. Reverse first d elements.
# 2. Reverse the rest of the array.
# 3. Reverse the entire array.

# Why does this work?
# - Because reversing parts and then the whole reorders the segments
#   to the correct rotated positions without using extra space.

# Visualization:
# arr = [1, 2, 3, 4, 5, 6, 7], d = 3

# Step 1: reverse(0 to 2) → [3, 2, 1, 4, 5, 6, 7]
# Step 2: reverse(3 to 6) → [3, 2, 1, 7, 6, 5, 4]
# Step 3: reverse(0 to 6) → [4, 5, 6, 7, 1, 2, 3]

# ------------------------------------------------------
# 🧠 IMPLEMENTATION
# ------------------------------------------------------

from typing import List

def leftRotateOp(arr: List[int], d: int) -> List[int]:
    n = len(arr)
    d = d % n  # Handle if d > n

    reverseArr(arr, 0, d - 1)      # Step 1: Reverse first d elements
    reverseArr(arr, d, n - 1)      # Step 2: Reverse rest
    reverseArr(arr, 0, n - 1)      # Step 3: Reverse entire array

    return arr

def reverseArr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# ------------------------------------------------------
# 🖼️ DRY RUN EXAMPLE
# ------------------------------------------------------

# arr = [1, 2, 3, 4, 5, 6, 7], d = 3

# Step 1: Reverse first d = 3 elements:
# reverse(0, 2) → [3, 2, 1, 4, 5, 6, 7]

# Step 2: Reverse from d to end:
# reverse(3, 6) → [3, 2, 1, 7, 6, 5, 4]

# Step 3: Reverse entire array:
# reverse(0, 6) → [4, 5, 6, 7, 1, 2, 3]

# ✅ Final Result: [4, 5, 6, 7, 1, 2, 3]

# ------------------------------------------------------
# ⏱️ TIME & SPACE COMPLEXITY
# ------------------------------------------------------
# Time Complexity  : O(n)     → 3 reversals, each O(n)
# Space Complexity : O(1)     → No extra space used
