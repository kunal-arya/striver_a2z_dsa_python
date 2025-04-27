def recursive_bubble_sort(arr, n):
    """
    Recursive Bubble Sort:
    - Compare adjacent elements and swap if needed, like the iterative version,
    but using recursion instead of a loop.
    
    Time Complexity:
    - Best Case: O(n) (when the array is already sorted)
    - Average Case: O(n²)
    - Worst Case: O(n²)
    
    Space Complexity: O(n) (because of recursion stack)
    """
    # Base case: if the length is 1, array is sorted
    if n == 1:
        return arr

    # One pass of bubble sort: after this pass, the largest element is in the correct place
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]  # Swap if elements are out of order
    
    # Recursively call for the next smaller subarray (excluding the last sorted element)
    return recursive_bubble_sort(arr, n-1)


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Recursive Bubble Sort:", recursive_bubble_sort(arr, len(arr)))
