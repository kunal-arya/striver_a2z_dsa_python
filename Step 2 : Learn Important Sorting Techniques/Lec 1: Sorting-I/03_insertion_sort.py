# ============================================
# 📚 Insertion Sort (With Full Explanation)
# ============================================

# ✅ Time Complexity:
# - Best Case: O(n)       → When the array is already sorted
# - Average Case: O(n²)   → Random order
# - Worst Case: O(n²)     → Reverse sorted array

# ✅ Space Complexity:
# - O(1) → In-place sort, no extra memory

# ✅ Stable Sort:
# - Yes, maintains relative order of equal elements

# ------------------------------------------------------------
# 🔧 Intuition:
# ------------------------------------------------------------
# - Mimics how you sort playing cards in your hand.
# - Pick one card at a time and insert it at the correct position on the left side.
# - The left side of the array is always **sorted**.
# - For every new element (starting from index 1), go backward and shift elements
#   until you find the correct spot.

# ------------------------------------------------------------
# 🧮 Dry Run:
# ------------------------------------------------------------
# Input: [12, 11, 13, 5, 6]

# Step 1: i = 0 → nothing happens, 12 is the only element
# Step 2: i = 1 → 11 < 12 → swap → [11, 12, 13, 5, 6]
# Step 3: i = 2 → 13 > 12 → OK → no swap → [11, 12, 13, 5, 6]
# Step 4: i = 3 → 5 < 13 → swap → [11, 12, 5, 13, 6]
#                  5 < 12 → swap → [11, 5, 12, 13, 6]
#                  5 < 11 → swap → [5, 11, 12, 13, 6]
# Step 5: i = 4 → 6 < 13 → swap → [5, 11, 12, 6, 13]
#                  6 < 12 → swap → [5, 11, 6, 12, 13]
#                  6 < 11 → swap → [5, 6, 11, 12, 13]

# Final Output: [5, 6, 11, 12, 13]

# ------------------------------------------------------------
# 🖼️ Visualization:
# ------------------------------------------------------------
# 🔗 https://visualgo.net/en/sorting?slide=5-1
# This site shows the animation of insertion sort step by step.

# ------------------------------------------------------------
# 🔁 Insertion Sort Function
# ------------------------------------------------------------

def insertion_sort(arr):
    """
    Insertion Sort:
    - Take one element at a time and insert it into its correct position.
    - The left side remains sorted.

    Tips:
    - 'Sort like playing cards' - insert each new card into the right place in your hand.
    - Very efficient for small or nearly sorted arrays.
    """
    n = len(arr)
    
    for i in range(n - 1):
        # Traverse backwards from the element at i+1 and swap with previous if needed
        for j in range(i + 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap if out of order
            else:
                break  # Stop if the current element is in the correct place
    
    return arr

# ------------------------------------------------------------
# 🚀 Driver Code
# ------------------------------------------------------------

arr = [12, 11, 13, 5, 6]
print("Insertion Sort:", insertion_sort(arr))

# Output:
# Insertion Sort: [5, 6, 11, 12, 13]
