# ========================
# 🧠 Quick Sort Algorithm (with Full Explanation)
# ========================

# ✅ Time Complexity:
# - Best Case: O(N log N)     → Balanced partitions
# - Average Case: O(N log N)
# - Worst Case: O(N^2)        → Skewed partitions (e.g., already sorted)

# ✅ Space Complexity:
# - Average: O(log N) due to recursion stack
# - Worst: O(N) in case of skewed recursion tree

# ✅ In-Place Sorting: Yes
# ✅ Stable Sort: No

# -------------------------------------------------------------
# 🔧 Quick Sort Intuition:
# -------------------------------------------------------------
# - "Divide and Conquer" strategy.
# - Pick a pivot element (we use the first element, arr[low]).
# - Partition the array: Move all elements smaller than the pivot to its left,
#   and all elements larger than the pivot to its right. The pivot is now in its
#   final sorted position.
# - Recursively apply the same logic to the left and right subarrays.

# qs(arr, low, high)
#   → partition the array with qs_pivot()
#   → get the pivot index (correct place of pivot)
#   → recursively apply qs(arr, low, pivot - 1)   // Sort left part
#                         qs(arr, pivot + 1, high)  // Sort right part

# -------------------------------------------------------------
# 🌳 Recursion Tree & Visual Dry Run
# -------------------------------------------------------------
# Initial Call: qs([64, 34, 25, 12, 22, 11, 90], 0, 6)
#
#                                          qs([64, 34, 25, 12, 22, 11, 90], 0, 6)
#                                          Pivot: 64
#                                          Partitioned: [11, 34, 25, 12, 22, |64|, 90] -> pivot_idx=5
#                                                     /                             \
#                                                    /                               \
#                        qs([11, 34, 25, 12, 22], 0, 4)                           qs([90], 6, 6)
#                        Pivot: 11                                                 (Base Case: low>=high, return)
#                        Partitioned: [|11|, 34, 25, 12, 22] -> pivot_idx=0
#                                     /                \
#                                    /                  \
#                qs([], 0, -1)                     qs([34, 25, 12, 22], 1, 4)
#                (Base Case)                         Pivot: 34
#                                                    Partitioned: [11, |22, 25, 12|, 34, 64, 90] -> pivot_idx=4
#                                                                 /                   \
#                                                                /                     \
#                                             qs([22, 25, 12], 1, 3)                qs([], 5, 4)
#                                             Pivot: 22                               (Base Case)
#                                             Partitioned: [11, |12|, 22, |25|, 34, 64, 90] -> pivot_idx=2
#                                                         /         \
#                                                        /           \
#                                           qs([12], 1, 1)        qs([25], 3, 3)
#                                           (Base Case)             (Base Case)
#
# Final Sorted Array: [11, 12, 22, 25, 34, 64, 90]

# -------------------------------------------------------------
# 🔁 qs_pivot(arr, low, high): The Partitioning Logic
# -------------------------------------------------------------
# - Select the first element (arr[low]) as the pivot.
# - Use two pointers, i and j, to find the correct position for the pivot.
def qs_pivot(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    # --- Visual Start ---
    # arr: [...]
    # pivot = arr[low]
    #  i →            ← j

    while i < j:
        # Move pointer 'i' to the right until we find an element > pivot
        # The condition `i <= high - 1` prevents `i` from going out of bounds.
        while i <= high and arr[i] <= pivot:
            i += 1
        
        # Move pointer 'j' to the left until we find an element <= pivot
        # The condition `j >= low + 1` prevents `j` from going out of bounds.
        while j >= low and arr[j] > pivot:
            j -= 1
            
        # If the pointers 'i' and 'j' haven't crossed...
        if i < j:
            # ...it means we've found an element on the left that's too big (at i)
            # and an element on the right that's too small (at j). Swap them.
            # Visual: arr[..., big_val_at_i, ..., small_val_at_j, ...] -> arr[..., small_val_at_j, ..., big_val_at_i, ...]
            arr[i], arr[j] = arr[j], arr[i]

    # The loop ends when j <= i. At this point, j is the final sorted position for the pivot.
    # Swap the pivot (which is still at arr[low]) with the element at arr[j].
    # Visual: [pivot, ..., arr[j], ...] -> [arr[j], ..., pivot, ...]
    arr[low], arr[j] = arr[j], arr[low]
    
    # Return the index where the pivot is now located.
    return j

# -------------------------------------------------------------
# 🔁 qs(arr, low, high): The Recursive Sorting Logic
# -------------------------------------------------------------
# - Base case: if low >= high, the subarray has 0 or 1 elements, so it's already sorted.
# - Recursive step: Partition the array and then recursively sort the left and right parts.
def qs(arr, low, high, depth=0):
    # This is a visual aid to see the recursion depth and the current state.
    indent = "  " * depth
    print(f"{indent}qs(arr, low={low}, high={high}) on subarray: {arr[low:high+1]}")
    
    if low < high:
        # 1. Partition the array. After this call, arr[pivot_idx] is in its final sorted place.
        print(f"{indent}  - Partitioning around pivot: {arr[low]}")
        pivot_idx = qs_pivot(arr, low, high)
        print(f"{indent}  - Array after partition (pivot {arr[pivot_idx]} is now at index {pivot_idx}): {arr}")

        # 2. Recursively sort the left subarray (elements smaller than the pivot).
        print(f"{indent}  -> [L] Recursing on left part: indices {low} to {pivot_idx - 1}")
        qs(arr, low, pivot_idx - 1, depth + 1)
        
        # 3. Recursively sort the right subarray (elements larger than the pivot).
        print(f"{indent}  -> [R] Recursing on right part: indices {pivot_idx + 1} to {high}")
        qs(arr, pivot_idx + 1, high, depth + 1)
    else:
        # Base Case: The subarray is sorted (or empty), so we return.
        print(f"{indent}  - Base Case reached (low >= high). Returning.")


# -------------------------------------------------------------
# 🚀 Driver Code & Final Output
# -------------------------------------------------------------
arr = [64, 34, 25, 12, 22, 11, 90]
print("Initial Array:", arr)
print("-" * 30)
print("Visual Dry Run:")
qs(arr, 0, len(arr) - 1)
print("-" * 30)
print("Quick Sort Final Result:", arr)

# =========================================================================
# 💻 EXPECTED OUTPUT OF THE VISUAL TRACE
# =========================================================================
#
# 📞 Call: qs(low=0, high=6) on [64] [34] [25] [12] [22] [11] [90]
#    - 🔄 Partitioning around pivot [64]...
#    - ✨ Partitioned. Pivot [64] is now at index 5.
#      State: [11] [34] [25] [12] [22] [64] [90]
#    ├─ Left Call...
#     📞 Call: qs(low=0, high=4) on [11] [34] [25] [12] [22] 64 90
#        - 🔄 Partitioning around pivot [11]...
#        - ✨ Partitioned. Pivot [11] is now at index 0.
#          State: [11] [34] [25] [12] [22] 64 90
#        ├─ Left Call...
#         📞 Call: qs(low=0, high=-1) on 11 34 25 12 22 64 90
#            - ✅ Base Case (low >= high), returning.
#        └─ Right Call...
#         📞 Call: qs(low=1, high=4) on 11 [34] [25] [12] [22] 64 90
#            - 🔄 Partitioning around pivot [34]...
#            - ✨ Partitioned. Pivot [34] is now at index 4.
#              State: 11 [22] [25] [12] [34] 64 90
#            ├─ Left Call...
#             📞 Call: qs(low=1, high=3) on 11 [22] [25] [12] 34 64 90
#                - 🔄 Partitioning around pivot [22]...
#                - ✨ Partitioned. Pivot [22] is now at index 2.
#                  State: 11 [12] [22] [25] 34 64 90
#                ├─ Left Call...
#                 📞 Call: qs(low=1, high=1) on 11 [12] 22 25 34 64 90
#                    - ✅ Base Case (low >= high), returning.
#                └─ Right Call...
#                 📞 Call: qs(low=3, high=3) on 11 12 22 [25] 34 64 90
#                    - ✅ Base Case (low >= high), returning.
#            └─ Right Call...
#             📞 Call: qs(low=5, high=4) on 11 22 25 12 34 64 90
#                - ✅ Base Case (low >= high), returning.
#    └─ Right Call...
#     📞 Call: qs(low=6, high=6) on 11 34 25 12 22 64 [90]
#        - ✅ Base Case (low >= high), returning.
#
# Final Sorted Array: [11, 12, 22, 25, 34, 64, 90]