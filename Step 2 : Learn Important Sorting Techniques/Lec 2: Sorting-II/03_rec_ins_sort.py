# recursive insertion sort

def rec_ins_sort(arr, i, n):
    if i == n:
        return arr
    
    j = i - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j -= 1

    return rec_ins_sort(arr, i + 1, n)

print(rec_ins_sort([12,11,13,5,6],0,5))