# =================================================================================================
# PROBLEM: 48. Rotate Image
# =================================================================================================
#
# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees
# clockwise.
#
# You have to rotate the image in-place, which means you have to modify the input 2D
# matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# For example:
# Input:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
#
# Output:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
#
# The problem will be solved in two ways:
# 1. Brute Force: A simple approach that uses an extra matrix (violates the "in-place" constraint but is good for understanding).
# 2. Optimal: An efficient, in-place solution that uses a two-step transformation.
#
# =================================================================================================

from typing import List

def printMatrix(arr):
    for row in arr:
        print(' '.join(str(x) for x in row))

# =================================================================================================
# Approach 1: Brute Force (Using an Auxiliary Matrix)
# =================================================================================================

# --- INTUITION ---
# The most straightforward way to approach this problem is to figure out where each element
# *should* go in the rotated image and place it there in a new, separate matrix.
#
# Let's observe the pattern of movement for an element at `arr[row][col]` in an `n x n` matrix:
# - The element at `[0][0]` moves to `[0][2]`.
# - The element at `[0][1]` moves to `[1][2]`.
# - The element at `[1][0]` moves to `[0][1]`.
#
# The general rule for a clockwise 90-degree rotation is:
# An element at `arr[row][col]` moves to `new_matrix[col][n - 1 - row]`.
#
# We can create a new blank matrix and use this formula to copy every element from the
# original matrix into its correct new position in the new matrix.

# --- ALGORITHM ---
# 1. Create a new `n x n` matrix, `new`, initialized with zeros.
# 2. Get the dimensions of the matrix, `n`.
# 3. Iterate through every cell of the original matrix `arr` using nested loops (for `row` from 0 to n-1, for `col` from 0 to n-1).
# 4. In each iteration, take the value `arr[row][col]` and place it into the `new` matrix at the calculated destination: `new[col][n - 1 - row]`.
# 5. After the loops complete, the `new` matrix will be the correctly rotated version.

def rotateBrute(arr: List[List[int]]) -> None:
    n = len(arr)

    # Create a new matrix of the same size, filled with a placeholder.
    new = [[0 for _ in range(n)] for _ in range(n)]

    # Iterate through each cell of the original matrix.
    for rowIdx in range(n):
        for colIdx in range(n):
            # Apply the rotation formula to place the element in the new matrix.
            new[colIdx][n - 1 - rowIdx] = arr[rowIdx][colIdx] 

    printMatrix(new)

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2)
# Why? We must iterate through every cell of the `n x n` matrix once to copy it.
# If N is the number of rows/columns, there are N*N cells.
#
# Space Complexity: O(N^2)
# Why? We allocate an entirely new `n x n` matrix to store the result. The space required
# is proportional to the number of cells in the matrix. This approach is not "in-place".
#
# --- HOW TO REMEMBER ---
# Brute Force = "New Matrix, Copy Formula". It's simple and directly uses the mathematical
# formula for rotation, but it requires extra memory.

arr = [ [1,2,3], [4,5,6], [7,8,9] ]
print("Brute Approach Result:")
rotateBrute(arr)
print("-" * 20)

# =================================================================================================
# Approach 2: Optimal (In-place Rotation)
# =================================================================================================

# --- INTUITION ---
# To solve this in-place (O(1) extra space), we can't use a new matrix. We need a clever trick.
# A 90-degree clockwise rotation can be achieved through two sequential, simpler transformations:
#
# 1.  **Transpose the matrix:** This means flipping the matrix over its main diagonal (from top-left
#     to bottom-right). An element at `arr[row][col]` is swapped with the element at `arr[col][row]`.
#
#     Example Transpose:
#     [1, 2, 3]       [1, 4, 7]
#     [4, 5, 6]  -->  [2, 5, 8]
#     [7, 8, 9]       [3, 6, 9]
#
# 2.  **Reverse each row:** After transposing, if we reverse each individual row, we get the
#     final rotated matrix.
#
#     Example Reverse:
#     [1, 4, 7]  -->  [7, 4, 1]
#     [2, 5, 8]  -->  [8, 5, 2]
#     [3, 6, 9]  -->  [9, 6, 3]
#
# This two-step process correctly rotates the matrix 90 degrees clockwise and can be done in-place.

# --- ALGORITHM ---
# The process is broken into two distinct parts:
#
# Part 1: Transpose the Matrix
# 1. Iterate through the matrix with an outer loop `i` from 0 to `n-1`.
# 2. The inner loop `j` should go from `i + 1` to `n-1`. We start `j` from `i+1` to only process
#    the upper triangle of the matrix, avoiding swapping elements back to their original place.
# 3. Inside the inner loop, swap `arr[i][j]` with `arr[j][i]`.
#
# Part 2: Reverse Each Row
# 1. Iterate through each row of the (now transposed) matrix.
# 2. For each row, use a two-pointer approach to reverse it.
# 3. Initialize a left pointer `i = 0` and a right pointer `j = n-1`.
# 4. While `i < j`, swap the elements at the pointers and move the pointers towards the center (`i++`, `j--`).

def rotateOp(arr: List[List[int]]) -> None:
    n = len(arr)

    # Step 1: Transpose the matrix
    # Iterate through the upper triangle of the matrix.
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Swap the element with its counterpart across the main diagonal.
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        # Using two pointers to reverse the elements in the current row.
        arr[i].reverse()
    
    printMatrix(arr)
      
# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2)
# Why? The transpose step involves iterating through roughly half the cells (O(N^2/2)). The
# reverse step involves visiting each cell once (O(N^2)). Total time is O(N^2) + O(N^2), which is O(N^2).
#
# Space Complexity: O(1)
# Why? All swaps are done directly on the input matrix. We are not using any extra data
# structures that scale with the size of the matrix. This meets the "in-place" requirement.
#
# --- HOW TO REMEMBER ---
# This is a classic matrix trick. Remember the formula:
# **Clockwise Rotate = Transpose + Reverse Rows**
# (For a counter-clockwise rotation, the formula is: Transpose + Reverse Columns).

arr = [ [1,2,3], [4,5,6], [7,8,9] ]
print("Optimal Approach Result:")
rotateOp(arr)
print("-" * 20)