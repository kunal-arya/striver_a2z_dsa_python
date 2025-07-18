# -------------------------------------------
# 📚 SELECTION SORT
# -------------------------------------------

def selection_sort(arr):
    """
    Selection Sort:
    - Find the minimum element and place it at the beginning.
    - Repeat for each position.

    Tips:
    - 'Select and swap' method.
    - Imagine picking the smallest kid and moving him to the front.

    Time Complexity:
    - Best Case: O(n²) (always scans the entire remaining array)
    - Average Case: O(n²)
    - Worst Case: O(n²)

    Space Complexity: O(1) (in-place)

    Animation: https://visualgo.net/en/sorting?slide=3-1
    """
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume current i is the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Update min index if smaller element found
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap minimum with current position
    return arr

# Example usage
print("Selection Sort:", selection_sort([64, 25, 12, 22, 11]))