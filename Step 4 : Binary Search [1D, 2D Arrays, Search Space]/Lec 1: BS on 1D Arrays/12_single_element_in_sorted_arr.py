

# Brute Approach
def singleElBrute(arr):
    n = len(arr)

    if n == 1:
        return arr[0]
    
    for i in range(n):

        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]
            
    return -1

arr = [1,1,2,2,3,3,4,5,5,6,6]
print(singleElBrute(arr))

"""
# Optimal Approach ( Binary Search )
# Observation
1. If u divide the array into two parts from the single elements
    a. in the left array, all the duplicate pairs are like this => (even place, odd place)
    b. in the right array, all the duplicate pairs are like this => (odd place, even place)
2. (even,odd) => element in right half and (odd, even) => element in left half
"""

def singleElOp(arr):
    n = len(arr)
    low = 0
    high = n - 1

    if n == 0:
        return arr[0]
    
    # check for extreme left
    if arr[0] != arr[1]:
        return arr[0]
    
    # check for extreme right
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    
    low = 1
    high = n - 2

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        # Left Half
        if mid % 2 == 1 and arr[mid] == arr[mid - 1] or mid % 2 == 0 and arr[mid] == arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1,1,2,2,3,3,4,5,5,6,6]
print(singleElOp(arr))
