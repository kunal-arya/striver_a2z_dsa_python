# =================================================================================================
# PROBLEM: 48. Rotate Image
# =================================================================================================
#
# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees
# clockwise in-place (i.e., without using another 2D matrix).
#
# Example:
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
# We'll implement two methods:
# 1. Brute Force – using an extra matrix (for understanding).
# 2. Optimal – in-place using Transpose + Reverse strategy.
#
# =================================================================================================

from typing import List

def printMatrix(matrix: List[List[int]]) -> None:
    for row in matrix:
        print(" ".join(map(str, row)))

# =================================================================================================
# Approach 1: Brute Force (Using Extra Matrix)
# =================================================================================================

# --- INTUITION ---
# Element at [row][col] goes to [col][n - 1 - row] in the rotated matrix.
# This approach uses extra space to build a new matrix.

def rotateBrute(matrix: List[List[int]]) -> None:
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            rotated[col][n - 1 - row] = matrix[row][col]

    print("Brute Force Rotated Matrix:")
    printMatrix(rotated)

# --- COMPLEXITY ---
# Time: O(N^2)
# Space: O(N^2) – not in-place

# =================================================================================================
# Approach 2: Optimal (In-Place Rotation)
# =================================================================================================

# --- INTUITION ---
# Clockwise 90° rotation = Transpose + Reverse each row
#
# Step 1: Transpose the matrix (flip across the main diagonal)
# Step 2: Reverse each row

def rotateOptimal(matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Step 1: Transpose (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    print("Optimal In-Place Rotated Matrix:")
    printMatrix(matrix)

# --- COMPLEXITY ---
# Time: O(N^2)
# Space: O(1) – in-place

# =================================================================================================
# DRIVER CODE
# =================================================================================================

original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
printMatrix(original_matrix)
print("-" * 30)

# Brute Force (uses extra space)
rotateBrute([row[:] for row in original_matrix])  # Pass a copy
print("-" * 30)

# Optimal (modifies in-place)
matrix_to_rotate = [row[:] for row in original_matrix]  # Copy for fair comparison
rotateOptimal(matrix_to_rotate)
print("-" * 30)