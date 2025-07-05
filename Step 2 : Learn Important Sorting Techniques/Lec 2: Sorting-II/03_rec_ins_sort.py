# ============================================
# 🧠 Recursive Insertion Sort (With Explanation)
# ============================================

# ✅ Time Complexity:
# - Best Case: O(n)           → Already sorted array
# - Average/Worst Case: O(n²) → Repeated shifting of elements

# ✅ Space Complexity:
# - O(n) due to recursion stack (n recursive calls)

# ------------------------------------------------------------
# 🔧 Intuition:
# ------------------------------------------------------------
# - Just like iterative insertion sort, we want to build the sorted portion of the array
#   from left to right — one element at a time.
# - For each index `i`, we insert arr[i] into its correct position in the sorted subarray [0...i-1].
# - We do this recursively by processing one element at a time.

# ------------------------------------------------------------
# 🧮 Dry Run:
# ------------------------------------------------------------
# Input: [12, 11, 13, 5, 6]

# Step 1: i = 1 → Compare 11 with 12 → swap → [11, 12, 13, 5, 6]
# Step 2: i = 2 → 13 > 12 → OK → No swap → [11, 12, 13, 5, 6]
# Step 3: i = 3 → 5 < 13 → swap → [11, 12, 5, 13, 6]
#                  5 < 12 → swap → [11, 5, 12, 13, 6]
#                  5 < 11 → swap → [5, 11, 12, 13, 6]
# Step 4: i = 4 → 6 < 13 → swap → [5, 11, 12, 6, 13]
#                  6 < 12 → swap → [5, 11, 6, 12, 13]
#                  6 < 11 → swap → [5, 6, 11, 12, 13]

# Final: [5, 6, 11, 12, 13]

# ------------------------------------------------------------
# 🔗 Visual Reference:
# ------------------------------------------------------------
# Animation: https://visualgo.net/en/sorting?slide=5-1

# ------------------------------------------------------------
# 🔁 Recursive Insertion Sort Function
# ------------------------------------------------------------

def rec_insertion_sort(arr, i, n):
    """
    Recursive Insertion Sort:
    - Insert arr[i] into its correct position in the sorted part [0...i-1]
    - Repeat recursively for i+1 to end of array.
    """
    # 🛑 Base Case: All elements processed
    if i == n:
        return arr

    # 🔁 Shift arr[i] into its correct position
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break

    # 🔂 Recursive call for next element
    return rec_insertion_sort(arr, i + 1, n)

# ------------------------------------------------------------
# 🚀 Driver Code
# ------------------------------------------------------------

arr = [12, 11, 13, 5, 6]
print("Recursive Insertion Sort:", rec_insertion_sort(arr, 1, len(arr)))

# Output:
# Recursive Insertion Sort: [5, 6, 11, 12, 13]