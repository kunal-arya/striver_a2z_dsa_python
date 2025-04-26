# reverse an array

# Using Two pointers
def reverse_arr(arr, l, *, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse_arr(arr,l + 1,r = r - 1)




arr = [1,2,3,4,5]
r = len(arr) - 1
reverse_arr(arr,0,r = r)
print(arr)

# Using One Pointer
def reverse_arr_op(arr,i = 0):
    n = len(arr)
    if i >= n // 2:
        return
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
    reverse_arr_op(arr,i + 1)

reverse_arr_op(arr)
print(arr)

