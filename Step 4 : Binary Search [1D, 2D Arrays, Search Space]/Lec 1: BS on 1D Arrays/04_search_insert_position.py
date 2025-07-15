from typing import List

# Brute Approach
def searchInsertPosBrute(arr: List[int], x: int) -> int:
    n = len(arr)

    for i in range(n):
        if arr[i] >= x:
            return i
        
    return n

arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
print(searchInsertPosBrute(arr,9))

# Binary Search (Optimal Solution - Lower Bound )
def searchInsertPosOp(arr: List[int], x: int) -> int:
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
print(searchInsertPosOp(arr,9))