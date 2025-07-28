from typing import List

# BRUTE Force
def medianBrute(arr):
    n = len(arr)
    m = len(arr[0])
    temp = []

    for i in range(n):
        for j in range(m):
            temp.append(arr[i][j])

    temp.sort()

    return temp[n * m // 2]


# Optimal Approach
def upperBound(arr: List[int], m: int, k: int) -> int:
    low = 0
    high = m - 1
    ans = m

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans

def smallerEquals(arr, n, m, req):
    sum = 0

    for i in range(n):
        sum += upperBound(arr[i], m = m, k = req)
    
    return sum

def medianOp(arr):
    n = len(arr)
    m = len(arr[0])
    req = (n * m) // 2

    low = float("inf")
    high = float("-inf")

    for i in range(n):
        low = min(low, arr[i][0])
        high = max(high, arr[i][m - 1])

    while low <= high:
        mid = low + (high - low) // 2

        smaller_equals = smallerEquals(arr, n = n, m = m, req = mid)

        if smaller_equals <= req:
            low = mid + 1
        else:
            high = mid - 1
    
    return low


mat =  [[1, 3, 5], 
        [2, 6, 9], 
        [3, 6, 9]]
# Median of mat => 5

print(medianBrute(mat)) 
print(medianOp(mat)) 