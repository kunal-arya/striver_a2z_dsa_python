from typing import List

def linearSearch(arr: List[int], k: int) -> int:
    n = len(arr)

    for i in range(n):
        if arr[i] == k:
            return i
    
    return -1

arr = [1,3,4,3,2,6,8,10,32,43]
k = 8

print(linearSearch(arr,k))

