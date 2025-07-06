# ----------------------------------------
# 🔍 PROBLEM STATEMENT
# ----------------------------------------
# Given an array of integers, rotate the array to the LEFT by 1 position in-place.
# This means:
# Every element shifts to the left by one index,
# and the first element moves to the end of the array.

# Example:
# Input  : [10, 20, 30, 40, 50]
# Output : [20, 30, 40, 50, 10]

# ----------------------------------------
# 💡 INTUITION
# ----------------------------------------
# - Think of the array as a circular queue.
# - When we rotate left, each element moves to its previous index.
# - The first element gets kicked out from the front and comes back at the end.

# To do this in-place:
# 1. Store the first element in a temp variable.
# 2. Shift all remaining elements one step to the left.
# 3. Put the temp value at the last index.

# ----------------------------------------
# 🧠 IMPLEMENTATION
# ----------------------------------------

def leftRotateByOnePlace(arr):
    n = len(arr)

    # Step 1: Store the first element
    temp = arr[0]

    # Step 2: Shift elements to the left
    for i in range(1, n):
        arr[i - 1] = arr[i]

    # Step 3: Place the first element at the end
    arr[n - 1] = temp

# ----------------------------------------
# 🖼️ DRY RUN VISUALIZATION
# ----------------------------------------

# Let's dry run with:
# arr = [10, 20, 30, 40, 50]

# Initial state:
# temp = 10

# Iteration:
# i = 1 → arr[0] = arr[1] → [20, 20, 30, 40, 50]
# i = 2 → arr[1] = arr[2] → [20, 30, 30, 40, 50]
# i = 3 → arr[2] = arr[3] → [20, 30, 40, 40, 50]
# i = 4 → arr[3] = arr[4] → [20, 30, 40, 50, 50]

# After loop:
# arr[4] = temp → [20, 30, 40, 50, 10]

# ✅ Final Output:
# [20, 30, 40, 50, 10]

# ----------------------------------------
# ⏱️ TIME & SPACE COMPLEXITY
# ----------------------------------------
# Time Complexity  : O(n)    → We iterate through the array once
# Space Complexity : O(1)    → No extra space except one temp variable
