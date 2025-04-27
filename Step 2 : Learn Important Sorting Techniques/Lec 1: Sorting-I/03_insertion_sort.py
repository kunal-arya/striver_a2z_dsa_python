# -------------------------------------------
# 📚 INSERTION SORT
# -------------------------------------------

def insertion_sort(arr):
    """
    Insertion Sort:
    - Take one element at a time and insert it into its correct position.
    - The left side remains sorted.

    Tips:
    - 'Sort like playing cards' - insert each new card into the right place in your hand.
    - Very efficient for small or nearly sorted arrays.

    Time Complexity:
    - Best Case: O(n) (when the array is already sorted)
    - Average Case: O(n²)
    - Worst Case: O(n²)

    Space Complexity: O(1) (in-place)

    Animation: https://visualgo.net/en/sorting?slide=5-1
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        # Move elements that are greater than key one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert key at the correct position
    return arr

# Example usage
print("Insertion Sort:", insertion_sort([12, 11, 13, 5, 6]))