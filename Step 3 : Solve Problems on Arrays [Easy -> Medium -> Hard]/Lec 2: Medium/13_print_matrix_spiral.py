from typing import List

def printMatrix(matrix: List[List[int]]):
    for row in matrix:
        print("\t".join(str(x) for x in row))
        print("\n")


# Optimal Approach ( This question has only one way and that's the optimal Way )
def spiralPrint(arr: List[List[int]]):
    rowLen = len(arr)
    colLen = len(arr[0])

    start_row = 0
    end_row = rowLen - 1
    start_col = 0
    end_col = colLen - 1

    new = []

    while start_row <= end_row and start_col <= end_col:
        # Left to Right => Row is Fixed -> start_row, col we have to iterate
        for colIdx in range(start_col,end_col + 1):
            new.append(arr[start_row][colIdx])
        start_row += 1
        
        # Up to Down => Column is Fixed -> end_column, row we have to iterate
        for rowIdx in range(start_row, end_row + 1):
            new.append(arr[rowIdx][end_col])
        end_col -= 1
        
        # Right to Left => Row is Fixed -> end_row, col we have to iterate reverse
        # Plus also check if still => start_row <= end_row is true b/c u just increased the start_row in first loop
        if start_row <= end_row:
            for colIdx in range(end_col,start_col - 1, -1):
                new.append(arr[end_row][colIdx])
            end_row -= 1
            
        # down to up => Column is Fixed -> start_col, row we have to iterate reverse order
        # Plus also check if still => start_col <= end_col is true b/c u just decreased the end_col in second loop
        if start_col <= end_col:
            for rowIdx in range(end_row,start_row - 1, -1):
                new.append(arr[rowIdx][start_col])
            start_col += 1

    print(new)


arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

spiralPrint(arr)



