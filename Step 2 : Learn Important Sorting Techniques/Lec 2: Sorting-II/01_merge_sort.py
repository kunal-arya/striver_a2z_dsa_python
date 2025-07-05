# ========================
# 🧠 Merge Sort Algorithm (with Full Explanation)
# ========================

# ✅ Time Complexity: O(N log N)
# ✅ Space Complexity: O(N) (due to temporary array)
# ✅ Stable Sorting Algorithm

# -------------------------------------------------------------
# 🔧 Merge Sort Intuition:
# -------------------------------------------------------------
# - Recursively divide the array into two halves.
# - When each part has only one element, they are considered sorted.
# - Then merge the two sorted halves back together in sorted order.
#
# merge_sort(arr, low, high)
#   → split into merge_sort(arr, low, mid) and merge_sort(arr, mid+1, high)
#   → merge both sorted parts using merge(arr, low, mid, high)

# -------------------------------------------------------------
# 📊 Visual Breakdown of Steps:
# -------------------------------------------------------------
# Input: [64, 34, 25, 12, 22, 11, 90]
#
# Split phase:
#   [64, 34, 25, 12, 22, 11, 90]
#     /                 \
# [64, 34, 25, 12]     [22, 11, 90]
#   /       \             /     \
# [64, 34] [25, 12]   [22, 11]  [90]
#  /   \     /   \      /   \
#[64][34] [25][12]  [22][11]
#
# Merge phase:
# [64, 34]     → [34, 64]
# [25, 12]     → [12, 25]
# [34, 64] + [12, 25] → [12, 25, 34, 64]
#
# [22, 11]     → [11, 22]
# [11, 22] + [90] → [11, 22, 90]
#
# [12, 25, 34, 64] + [11, 22, 90] → [11, 12, 22, 25, 34, 64, 90]

# -------------------------------------------------------------
# 🔄 merge(arr, low, mid, high):
# -------------------------------------------------------------
# - Merge two sorted parts of array: [low...mid] and [mid+1...high]
# - Compare elements from both sides and add smaller one to temp[]
# - Then copy merged temp[] back to arr[low...high]

def merge(arr, low, mid, high):
    temp = []               # Temporary array to store merged elements
    left = low              # Starting index of left sorted part
    right = mid + 1         # Starting index of right sorted part

    # Compare elements from both halves
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Copy any remaining elements from left part
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # Copy any remaining elements from right part
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy the merged temp array back to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]  # Adjusted index for correct placement

# -------------------------------------------------------------
# 🔁 merge_sort(arr, low, high):
# -------------------------------------------------------------
# - Recursively divide array into halves
# - Merge each half back using merge()

def merge_sort(arr, low, high):
    if low >= high:
        return  # Base case: Single element is already sorted

    mid = (low + high) // 2

    # Recursively sort first and second halves
    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)

    # Merge sorted halves
    merge(arr, low, mid, high)

# -------------------------------------------------------------
# 🚀 Driver Code & Final Output
# -------------------------------------------------------------
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr, 0, len(arr) - 1)
print("Merge Sort:", arr)

# Output:
# Merge Sort: [11, 12, 22, 25, 34, 64, 90]