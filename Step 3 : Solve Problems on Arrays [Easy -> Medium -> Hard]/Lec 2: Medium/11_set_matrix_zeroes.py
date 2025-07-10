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

# --- INTUITION ---
# The most direct approach is to iterate through the matrix. When we find a 0, we then iterate
# through its entire row and column and set them to 0.
#
# However, this has a major flaw: if we set a cell to 0, and our main loop later encounters
# this *new* 0, it will mistakenly think it was an original 0 and proceed to zero out its
# row and column, which is incorrect.
#
# To solve this, we can't immediately set cells to 0. Instead, when we find an original 0,
# we can iterate through its row and column and mark the non-zero elements with a special
# temporary value (like -1, assuming the matrix has non-negative integers).
# After we've scanned the entire matrix and marked all the cells that need to be changed,
# we can do a final pass to convert all the marked cells (-1) to 0.

# --- ALGORITHM ---
# 1. Traverse the matrix cell by cell from (0,0) to (m-1, n-1).
# 2. If you find an element `arr[r][c]` that is 0:
#    a. Call a function to iterate through row `r` and change all non-zero elements to -1.
#    b. Call a function to iterate through column `c` and change all non-zero elements to -1.
# 3. After the first traversal is complete, traverse the matrix again.
# 4. If any element is -1, change it to 0. This completes the process.

def setMatrixZeroesBrute(arr: List[List[int]]) -> None:
    # Get matrix dimensions
    colLen = len(arr)
    rowLen = len(arr[0])

    # First pass: find original zeroes and mark their rows/columns
    for colIdx in range(colLen):
        for rowIdx in range(rowLen):
            if arr[colIdx][rowIdx] == 0:
                markRowZero(arr=arr, FixedColIdx=colIdx, rowLen=rowLen)
                markColZero(arr=arr, FixedRowIdx=rowIdx, colLen=colLen)
    
    # Second pass: change all marked cells (-1) to 0
    for colIdx in range(colLen):
        for rowIdx in range(rowLen):
            if arr[colIdx][rowIdx] == -1:
                arr[colIdx][rowIdx] = 0

def markRowZero(*, arr: List[List[int]], FixedColIdx: int, rowLen: int):
    # Mark all non-zero elements in a given row with -1
    for rowIdx in range(rowLen):
        if arr[FixedColIdx][rowIdx] != 0:
            arr[FixedColIdx][rowIdx] = -1

def markColZero(*, arr: List[List[int]], FixedRowIdx: int, colLen: int):
    # Mark all non-zero elements in a given column with -1
    for colIdx in range(colLen):
        if arr[colIdx][FixedRowIdx] != 0:
            arr[colIdx][FixedRowIdx] = -1

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

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O((M*N) * (M+N))
# Why? The main nested loops run M*N times. Inside, if we find a zero, we call two functions
# that iterate M and N times respectively. This makes the approach very slow.
#
# Space Complexity: O(1)
# Why? We are modifying the matrix in-place and not using any extra data structures that
# scale with the size of the matrix.
#
# --- HOW TO REMEMBER ---
# Brute Force = "Mark then Sweep". It's inefficient because you might repeatedly mark the same
# rows/columns. The key is using a temporary marker to avoid the "new zero" problem.

# =================================================================================================
# Approach 2: Better (Use Marker Arrays)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach is slow because we do a lot of repeated work. A better way is to
# separate the "information gathering" phase from the "modification" phase.
#
# We can use two separate arrays, one to keep track of which rows need to be zeroed and another
# for the columns.
#
# 1.  **First Pass (Find Zeros):** Traverse the entire matrix once. If you find a zero at `arr[r][c]`,
#     you simply record this information, for example, by setting `row_marker[r] = 1` and `col_marker[c] = 1`.
# 2.  **Second Pass (Set Zeros):** Traverse the matrix again. For each cell `arr[r][c]`, check your
#     marker arrays. If `row_marker[r]` is 1 OR `col_marker[c]` is 1, you know this cell must be zero.
#
# This way, you avoid redundant marking and only traverse the full matrix twice.

# --- ALGORITHM ---
# 1. Create a row marker array `rowArr` of size `N` (number of columns) and a column marker array `colArr` of size `M` (number of rows). Initialize both to all zeros.
# 2. Traverse the matrix from (0,0) to (m-1, n-1).
# 3. If `arr[r][c] == 0`, set `colArr[r] = 1` and `rowArr[c] = 1`.
# 4. After the first traversal, traverse the matrix again.
# 5. For each cell `arr[r][c]`, if `colArr[r] == 1` or `rowArr[c] == 1`, set `arr[r][c] = 0`.

def setMatrixZeroesBetter(arr: List[List[int]]) -> None:
    colLen = len(arr)    # Number of rows
    rowLen = len(arr[0]) # Number of columns

    # Marker arrays for rows and columns
    colArr = [0] * colLen
    rowArr = [0] * rowLen

    # First pass: Identify which rows and columns contain a zero
    for colIdx in range(colLen):
        for rowIdx in range(rowLen):
            if arr[colIdx][rowIdx] == 0:
                colArr[colIdx] = 1
                rowArr[rowIdx] = 1

    # Second pass: Use the markers to set elements to zero
    for colIdx in range(colLen):
        for rowIdx in range(rowLen):
            if colArr[colIdx] or rowArr[rowIdx]:
                arr[colIdx][rowIdx] = 0

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

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(M*N)
# Why? We do two full passes of the matrix. O(M*N) + O(M*N) = O(2 * M*N), which is O(M*N).
#
# Space Complexity: O(M + N)
# Why? We are using two extra arrays whose sizes depend on the dimensions of the matrix.
#
# --- HOW TO REMEMBER ---
# Better = "Use Marker Arrays". It cleanly separates finding from setting, trading extra space for a much better time complexity.

# =================================================================================================
# Approach 3: Optimal (Use First Row and Column as Markers)
# =================================================================================================

# --- INTUITION ---
# The "Better" approach is good on time but uses O(M+N) space. To optimize to O(1) space, we need
# to find a way to store the marker information without creating new arrays. The clever idea is to
# use the first row and first column of the matrix itself as our marker arrays.
#
# - The first row (`arr[0][...]`) can act as the `rowArr` (marker for columns).
# - The first column (`arr[...][0]`) can act as the `colArr` (marker for rows).
#
# However, this creates a problem with the cell `arr[0][0]`. It's part of both the first row and
# first column. If `arr[0][0]` becomes 0, does it mean we should zero out the first row, or the first
# column, or both? This ambiguity is a problem.
#
# To solve this, we can use `arr[0][0]` to control the first row, and a separate, single boolean
# variable (e.g., `row0_should_be_zero`) to handle the state of the first column.
#
# The process is:
# 1. First, check if the first row or first column have any original zeros and store this info in our flags.
# 2. Then, use the first row/column to mark zeros for the *rest* of the matrix (the submatrix from (1,1)).
# 3. Apply the markings to the submatrix.
# 4. Finally, use the initial flags to zero out the first row/column if needed.

# --- ALGORITHM ---
# 1. Initialize a flag `row0 = 1`. This will track if the first column needs to be zeroed.
# 2. **First Pass (Marking):**
#    - Iterate through the whole matrix.
#    - If `arr[r][c] == 0`:
#      - Mark the corresponding row by setting `arr[r][0] = 0`.
#      - Mark the corresponding column. If it's not the first column (`c != 0`), set `arr[0][c] = 0`. If it *is* the first column (`c == 0`), set our flag `row0 = 0`.
# 3. **Second Pass (Set Zeros for Inner Matrix):**
#    - Iterate through the matrix from (1,1) to (m-1, n-1).
#    - For each cell `arr[r][c]`, if its row marker `arr[r][0]` is 0 or its column marker `arr[0][c]` is 0, set `arr[r][c] = 0`.
# 4. **Final Step (Set Zeros for First Row/Col):**
#    - Check the marker for the first row, which is `arr[0][0]`. If `arr[0][0] == 0`, set the entire first row to 0.
#    - Check the marker for the first column, which is our flag `row0`. If `row0 == 0`, set the entire first column to 0.

def setMatrixZeroesOp(arr: List[List[int]]):
    rowLen = len(arr[0])
    colLen = len(arr)

    # `row0` will be our flag for whether the first column should be zeroed.
    row0 = 1
    
    # Pass 1: Use first row/col as markers.
    for colIdx in range(colLen):
        for rowIdx in range(rowLen):
            if arr[colIdx][rowIdx] == 0:
                # Mark the row using the first element of that row.
                arr[colIdx][0] = 0

                # Mark the column. If it's the first col, use our flag.
                # Otherwise, use the first element of that column.
                if rowIdx != 0:
                    arr[0][rowIdx] = 0
                else:
                    row0 = 0

    # Pass 2: Zero out the inner matrix based on markers.
    # We go backwards to avoid overwriting markers before they are used.
    for colIdx in range(1, colLen):
        for rowIdx in range(1, rowLen):
            if arr[colIdx][0] == 0 or arr[0][rowIdx] == 0:
                arr[colIdx][rowIdx] = 0
    
    # Final step: Zero out the first row if its marker (arr[0][0]) is set.
    # Must be done after the inner matrix is processed.
    if arr[0][0] == 0:
        for rowIdx in range(rowLen):
            arr[0][rowIdx] = 0
    
    # Final step: Zero out the first col if its flag (row0) is set.
    if row0 == 0:
        for colIdx in range(colLen):
            arr[colIdx][0] = 0

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

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(M*N)
# Why? We perform a constant number of passes over the matrix, so the time is proportional to the number of cells.
#
# Space Complexity: O(1)
# Why? We only use one extra variable (`row0`), giving us constant extra space.
#
# --- HOW TO REMEMBER ---
# Optimal = "Use First Row/Col as Markers". It's the same logic as the better approach, but
# cleverly reuses the matrix's own space. The key trick is to handle the special case of `arr[0][0]`
# with an independent variable to avoid ambiguity.