# Merge Sort Algorithm
# Time Complexity: O(N log N)
# Space Complexity: O(N) (because of temp array)
# Stable Sort

# Function to merge two sorted halves of the array
def merge(arr, low, mid, high):
    temp = []               # Temporary array to store merged elements
    left = low              # Starting index of left sorted part
    right = mid + 1         # Starting index of right sorted part

    # Compare elements from left and right halves and add the smaller one
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # If any elements left in the left half, add them
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # If any elements left in the right half, add them
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy the merged elements back to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]   # Correctly placing elements based on original indices

# Recursive function to divide the array and call merge
def merge_sort(arr, low, high):
    if low >= high:
        return  # Base case: Single element is already sorted

    mid = (low + high) // 2   # Find the middle point

    # Recursively sort the first half
    merge_sort(arr, low, mid)

    # Recursively sort the second half
    merge_sort(arr, mid + 1, high)

    # Merge the sorted halves
    merge(arr, low, mid, high)

# Main driver code
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr, 0, len(arr) - 1)
print("Merge Sort:", arr)
