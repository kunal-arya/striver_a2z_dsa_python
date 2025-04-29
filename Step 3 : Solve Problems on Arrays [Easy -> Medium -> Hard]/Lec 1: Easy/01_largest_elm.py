# Largest Element in the array

def largest(arr,n):
    if(n == 0):
        return 0
    
    max_el = arr[0]
    
    if n == 1:
        return max_el
    

    for i in range(1,n):
        if arr[i] > max_el:
            max_el = arr[i]

    
    return max_el

arr = [64, 34, 25, 12, 22, 11, 90]
print(largest(arr, len(arr)))