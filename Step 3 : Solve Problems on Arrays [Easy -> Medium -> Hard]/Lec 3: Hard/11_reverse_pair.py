from typing import List

# Brute Force
# TC => O(n^2)
# SC => O(1)
def reversePairBrute(arr: List[int]) -> int:
    n = len(arr)

    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > 2 * arr[j]:
                count += 1

    return count


arr = [40,25,19,12,9,6,2]
print(reversePairBrute(arr))

# Optimal Approach
# Time Complexity => O(2nLogN)
# Space Complexity => O(n)
def merge(arr: List[int], low: int, mid: int, high: int) -> None:
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        righ += 1
    
    for i in range(low,high + 1):
        arr[i] = temp[i - low]

def countPairs(arr: List[int],low: int, mid: int, high: int) -> int:
    count = 0 
    right = mid + 1

    for left in range(low,mid + 1):
        while right <= high and arr[left] > 2 * arr[right]:
            right += 1
        count += right - (mid + 1)

    return count


def mergeSort(arr: List[int], low: int, high: int) -> int:
    if low >= high:
        return 0
    
    mid = (low + high) // 2

    leftCount  = mergeSort(arr,low,mid)
    rightCount = mergeSort(arr,mid + 1,high)

    crossCount = countPairs(arr,low,mid,high)

    merge(arr,low,mid,high)

    return leftCount + rightCount + crossCount

def reversePairOp(arr: List[int]) -> int:
    return mergeSort(arr,0,len(arr) - 1)

arr = [40,25,19,12,9,6,2]
print(reversePairOp(arr))