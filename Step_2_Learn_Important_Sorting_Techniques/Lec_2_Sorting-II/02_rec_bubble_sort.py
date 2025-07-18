# ================================
# 🧠 Recursive Bubble Sort Algorithm (with Full Explanation)
# ================================

# ✅ Time Complexity:
# - Best Case: O(n)           → Already sorted array (no swaps in first pass)
# - Average/Worst Case: O(n²) → For unsorted input

# ✅ Space Complexity: O(n)
# - Due to recursion stack (each function call adds a frame)

# -------------------------------------------------------------
# 🔧 Intuition:
# -------------------------------------------------------------
# - Like regular Bubble Sort, we push the largest element to the end in each pass
# - But instead of using a loop to run multiple passes, we use recursion
# - Each recursive call works on a smaller subarray: size n-1, n-2, ..., 1
#
# Key idea: Do one full pass per recursive call, then recurse on remaining unsorted part.

# -------------------------------------------------------------
# 🧮 Dry Run:
# -------------------------------------------------------------
# arr = [64, 34, 25, 12]
# Pass 1: Compare all pairs → largest moves to the end
#   [64, 34] → swap → [34, 64]
#   [64, 25] → swap → [34, 25, 64]
#   [64, 12] → swap → [34, 25, 12, 64]
# Pass 2: [34, 25, 12]
#   [34, 25] → swap → [25, 34]
#   [34, 12] → swap → [25, 12, 34]
# Pass 3: [25, 12]
#   [25, 12] → swap → [12, 25]
# Pass 4: [12] → base case hit

# Final Result: [12, 25, 34, 64]

# -------------------------------------------------------------
# 🔁 Recursive Bubble Sort Function
# -------------------------------------------------------------

def recursive_bubble_sort(arr, n):
    """
    Recursive Bubble Sort:
    - Compares adjacent elements and swaps if needed.
    - Uses recursion instead of outer loop.
    """

    # 🛑 Base case: array of size 1 is already sorted
    if n == 1:
        return arr

    # 🌀 One complete pass of Bubble Sort:
    # After this pass, the largest element moves to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap if out of order

    # 🔁 Recur on the remaining unsorted subarray (excluding last sorted element)
    return recursive_bubble_sort(arr, n - 1)

# -------------------------------------------------------------
# 🚀 Driver Code & Final Output
# -------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90]
print("Recursive Bubble Sort:", recursive_bubble_sort(arr, len(arr)))

# Output:
# Recursive Bubble Sort: [11, 12, 22, 25, 34, 64, 90]
