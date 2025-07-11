# =================================================================================================
# PROBLEM: Set Matrix Zeroes
# =================================================================================================
#
# Given an `m x n` integer matrix, if an element is 0, set its entire row and column to 0.
# The operation must be done in-place.
#
# For example:
# Input:
# [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 1, 1]
# ]
# Output:
# [
#   [1, 0, 1],
#   [0, 0, 0],
#   [1, 0, 1]
# ]
#
# The problem will be solved in three ways:
# 1. Brute Force: A naive approach that has a major flaw if not handled carefully.
# 2. Better: An improved two-pass approach using extra memory.
# 3. Optimal: The most efficient solution that reuses the matrix's own space.
#
# =================================================================================================

from typing import List

def printMatrix(arr):
    for row in arr:
        print(' '.join(str(x) for x in row))

# =================================================================================================
# Approach 1: Brute Force (Mark non-zero elements to be changed)
# =================================================================================================

def setMatrixZeroesBrute(arr: List[List[int]]) -> None:
    # Get matrix dimensions
    rowLen = len(arr)
    colLen = len(arr[0])

    # First pass: find original zeroes and mark their rows/columns
    for rowIdx in range(rowLen):
        for colIdx in range(colLen):
            if arr[rowIdx][colIdx] == 0:
                markRowZero(arr=arr, FixedRowIdx=rowIdx, colLen=colLen)
                markColZero(arr=arr, FixedColIdx=colIdx, rowLen=rowLen)
    
    # Second pass: change all marked cells (-1) to 0
    for rowIdx in range(rowLen):
        for colIdx in range(colLen):
            if arr[rowIdx][colIdx] == -1:
                arr[rowIdx][colIdx] = 0

def markRowZero(*, arr: List[List[int]], FixedRowIdx: int, colLen: int):
    # Mark all non-zero elements in a given row with -1
    for colIdx in range(colLen):
        if arr[FixedRowIdx][colIdx] != 0:
            arr[FixedRowIdx][colIdx] = -1

def markColZero(*, arr: List[List[int]], FixedColIdx: int, rowLen: int):
    # Mark all non-zero elements in a given column with -1
    for rowIdx in range(rowLen):
        if arr[rowIdx][FixedColIdx] != 0:
            arr[rowIdx][FixedColIdx] = -1

arr = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1],
    [1,1,1,1]
]
setMatrixZeroesBrute(arr)
print(f"\nBrute Solution Result: \n")
printMatrix(arr)

# =================================================================================================
# Approach 2: Better (Use Marker Arrays)
# =================================================================================================

def setMatrixZeroesBetter(arr: List[List[int]]) -> None:
    rowLen = len(arr)    # Number of rows
    colLen = len(arr[0]) # Number of columns

    # Marker arrays for rows and columns
    rowArr = [0] * rowLen
    colArr = [0] * colLen

    # First pass: Identify which rows and columns contain a zero
    for rowIdx in range(rowLen):
        for colIdx in range(colLen):
            if arr[rowIdx][colIdx] == 0:
                rowArr[rowIdx] = 1
                colArr[colIdx] = 1

    # Second pass: Use the markers to set elements to zero
    for rowIdx in range(rowLen):
        for colIdx in range(colLen):
            if rowArr[rowIdx] or colArr[colIdx]:
                arr[rowIdx][colIdx] = 0

arr = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1],
    [1,1,1,1]
]
setMatrixZeroesBetter(arr)
print(f"\nBetter Solution Result: \n")
printMatrix(arr)

# =================================================================================================
# Approach 3: Optimal (Use First Row and Column as Markers)
# =================================================================================================

def setMatrixZeroesOp(arr: List[List[int]]):
    rowLen = len(arr)       # number of rows
    colLen = len(arr[0])    # number of columns

    row0 = 1  # Flag to indicate if first column needs to be zeroed

    # Pass 1: Use first row and column as markers
    for rowIdx in range(rowLen):
        for colIdx in range(colLen):
            if arr[rowIdx][colIdx] == 0:
                arr[rowIdx][0] = 0
                if colIdx != 0:
                    arr[0][colIdx] = 0
                else:
                    row0 = 0

    # Pass 2: Set zeroes based on markers (excluding first row and column)
    for rowIdx in range(1, rowLen):
        for colIdx in range(1, colLen):
            if arr[rowIdx][0] == 0 or arr[0][colIdx] == 0:
                arr[rowIdx][colIdx] = 0

    # Final pass: zero first row if needed
    if arr[0][0] == 0:
        for colIdx in range(colLen):
            arr[0][colIdx] = 0

    # Final pass: zero first column if needed
    if row0 == 0:
        for rowIdx in range(rowLen):
            arr[rowIdx][0] = 0

arr = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1],
    [1,1,1,1]
]
setMatrixZeroesOp(arr)
print(f"\nOptimal Solution Result: \n")
printMatrix(arr)