# Quick Sort Algorithm
# ---------------------
# Quick Sort is a Divide and Conquer algorithm.
# It picks an element as pivot and partitions the given array around the pivot.
# Common pivot selection: first element, last element, random element, or median.

# Time Complexity:
# - Best Case: O(N log N)  --> when partition divides array equally
# - Average Case: O(N log N)
# - Worst Case: O(N^2)     --> when array is already sorted or reverse sorted (poor pivot choice)

# Space Complexity:
# - O(log N) auxiliary stack space due to recursive calls (in average case)
# - O(N) in worst case if recursion tree becomes skewed

# Quick Sort is NOT a stable sort.
# In-place sorting algorithm (doesn't use extra space except recursion stack).


# Partition function to place pivot at correct sorted position
def qs_pivot(arr, low, high):
    pivot = arr[low]  # Choosing pivot as the first element
    i, j = low, high

    while i < j:
        # Move i towards right while arr[i] <= pivot
        while i <= high - 1 and arr[i] <= pivot:
            i += 1

        # Move j towards left while arr[j] > pivot
        while j >= low + 1 and arr[j] > pivot:
            j -= 1

        # Swap arr[i] and arr[j] if i < j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element with element at j
    arr[j], arr[low] = arr[low], arr[j]
    return j  # Return the correct position of pivot


# Main Quick Sort recursive function
def qs(arr, low, high):
    if low < high:
        pivot_idx = qs_pivot(arr, low, high)  # Partition the array
        qs(arr, low, pivot_idx - 1)           # Recursively sort left part
        qs(arr, pivot_idx + 1, high)           # Recursively sort right part


# Driver code
arr = [64, 34, 25, 12, 22, 11, 90]
qs(arr, 0, len(arr) - 1)
print("Quick Sort:", arr)
