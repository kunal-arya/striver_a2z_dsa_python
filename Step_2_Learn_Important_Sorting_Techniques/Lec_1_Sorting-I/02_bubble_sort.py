# -------------------------------------------
# 📚 BUBBLE SORT
# -------------------------------------------

def bubble_sort(arr):
    """
    Bubble Sort:
    - Compare adjacent elements and swap if out of order.
    - After each full pass, the largest element 'bubbles up' to the end.

    Tips:
    - 'Bubble up big elements' like heavy bubbles in water.
    - Optimized: If no swaps in a pass, array is sorted early.

    Time Complexity:
    - Best Case: O(n) (when the array is already sorted)
    - Average Case: O(n²)
    - Worst Case: O(n²)

    Space Complexity: O(1) (in-place)

    Animation: https://visualgo.net/en/sorting?slide=4-1
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # Optimization flag
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if needed
                swapped = True
        if not swapped:
            # If no swaps were made, the list is already sorted
            break
    return arr

# Example usage
print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
