# =================================================
# Quick Sort Algorithm
# =================================================
#
# Time Complexity:
# - Best & Average Case: O(N log N)
# - Worst Case: O(N^2)
#
# Space Complexity: O(log N) for the recursion stack.
#
# -------------------------------------------------
# Core Idea: Divide and Conquer
# -------------------------------------------------
# 1. Pick a 'pivot' element.
# 2. Partition: Rearrange the array so that all elements smaller than the pivot
#    are on its left, and all elements greater are on its right.
# 3. Recurse: Apply quick sort to the left and right subarrays.
#
# -------------------------------------------------
# Recursion Tree & Visual Dry Run
# -------------------------------------------------
# Initial Array: [64, 34, 25, 12, 22, 11, 90]
#
#                                  qs(arr, 0, 6) pivot=64
#                                        |
#                       [11, 34, 25, 12, 22] |64| [90]
#                       /                      \
#                 qs(arr, 0, 4) pivot=11      qs(arr, 6, 6) -> base case
#                      |
#             |11| [34, 25, 12, 22]
#             /          \
# qs(arr, 0,-1) -> base   qs(arr, 1, 4) pivot=34
#                            |
#                   [22, 25, 12] |34|
#                   /              \
#           qs(arr, 1, 3) pivot=22  qs(arr, 5, 4) -> base
#                 |
#           [12] |22| [25]
#           /      \
# qs(arr, 1,1)    qs(arr, 3,3) -> base cases
#
# Final Sorted Array: [11, 12, 22, 25, 34, 64, 90]
#
# -------------------------------------------------

def partition(arr, low, high):
    """
    This function takes the first element as a pivot, places the pivot element
    at its correct position in the sorted array, and places all smaller
    elements to the left of the pivot and all greater elements to the right.
    """
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        # Find an element on the left side that is > pivot
        while i <= high and arr[i] <= pivot:
            i += 1

        # Find an element on the right side that is < pivot
        while j >= low and arr[j] > pivot:
            j -= 1

        # If i and j haven't crossed, swap them
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Why swap pivot with arr[j]?
    # When the `while i < j` loop ends, `j` is the final position where the
    # pivot belongs. This is because the `j` pointer has stopped at the last
    # element that is smaller than or equal to the pivot. All elements to the
    # left of `j` are guaranteed to be smaller than or equal to the pivot.
    # Therefore, swapping the pivot (arr[low]) with arr[j] places the pivot
    # in its correct sorted position.
    arr[low], arr[j] = arr[j], arr[low]

    # We return `j` to the main quick_sort function so it knows the split point.
    # The next recursive calls will sort the subarrays to the left (low to j-1)
    # and right (j+1 to high) of this newly placed pivot.
    return j

def quick_sort(arr, low, high):
    """
    The main function that implements QuickSort.
    - arr: The array to be sorted.
    - low: Starting index.
    - high: Ending index.
    """
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place.
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# --- Driver Code ---
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
