from typing import List

# PROBLEM STATEMENT
# Given an array `nums` with n objects colored red, white, or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# Example: arr = [2, 0, 2, 1, 1, 0] -> [0, 0, 1, 1, 2, 2]

# =================================================================================================
# APPROACH 1: BRUTE FORCE (Using a standard sorting algorithm)
# =================================================================================================
#
# INTUITION:
# The most straightforward way to sort an array of numbers is to use a well-known,
# efficient sorting algorithm. Since the colors are represented by numbers (0, 1, 2),
# we can treat this as a general integer sorting problem. Algorithms like Merge Sort,
# Quick Sort, or Heap Sort can be used. The provided code uses Merge Sort.
#
# VISUAL EXPLANATION (Merge Sort):
# Merge sort is a "divide and conquer" algorithm.
# 1. Divide: It repeatedly divides the array into two halves until each sub-array contains only one element.
# 2. Conquer (Merge): It then merges these sub-arrays back together in a sorted manner.
#
#    [2, 0, 2, 1, 1, 0]
#         /         \
#    [2, 0, 2]     [1, 1, 0]  <- Divide phase
#     /    \         /    \
#    [2]  [0, 2]   [1]  [1, 0]
#          /  \         /  \
#         [0] [2]      [1] [0]
#
#    Now, merge back up, sorting at each step:
#         [0, 2]       [0, 1]
#         /    \         /    \
#    [0, 2, 2]     [0, 1, 1]  <- Merge phase
#         \         /
#       [0, 0, 1, 1, 2, 2]    <- Final sorted array
#
# COMPLEXITY:
# Time Complexity: O(N log N) - Standard for comparison-based sorting algorithms like Merge Sort.
# Space Complexity: O(N) - Merge sort requires a temporary array to store the merged parts.
#

# Helper function to merge two sorted halves of an array
def merge(arr: List[int], s: int, m: int, e: int) -> None:
    temp = []
    left = s
    right = m + 1

    # Compare elements from left and right halves and add the smaller one to temp
    while left <= m and right <= e:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # Add any remaining elements from the left half
    while left <= m:
        temp.append(arr[left])
        left += 1

    # Add any remaining elements from the right half
    while right <= e:
        temp.append(arr[right])
        right += 1

    # Copy the sorted elements from temp back to the original array
    for i in range(s, e + 1):
        arr[i] = temp[i - s]

# Main recursive function for Merge Sort
def mergeSort(arr: List[int], s: int, e: int) -> None:
    # Base case: if the array has 0 or 1 element, it's already sorted
    if s >= e:
        return

    m = (s + e) // 2

    # Recursively sort the left half
    mergeSort(arr, s, m)
    # Recursively sort the right half
    mergeSort(arr, m + 1, e)

    # Merge the two sorted halves
    merge(arr, s, m, e)

def sortColorBrute(arr: List[int]) -> List[int]:
    n = len(arr)
    mergeSort(arr, 0, n - 1)
    return arr

arr_brute = [0, 1, 2, 0, 2, 2, 1, 1]
print(f"Brute Force Sort: {sortColorBrute(arr_brute)}")


# =================================================================================================
# APPROACH 2: BETTER (Counting Sort)
# =================================================================================================
#
# INTUITION:
# Since we know the array will only ever contain three distinct values (0, 1, and 2),
# we can optimize by avoiding a comparison-based sort. The idea is to iterate through
# the array once to count the occurrences of 0s, 1s, and 2s. Then, in a second pass,
# we overwrite the original array with the correct number of 0s, followed by 1s, and then 2s.
# This is a two-pass algorithm.
#
# VISUAL EXPLANATION:
# arr = [2, 0, 1, 2, 0, 1]
#
# Pass 1: Count the numbers
# - Iterate through the array:
# - Found a 2 -> count2 = 1
# - Found a 0 -> count0 = 1
# - Found a 1 -> count1 = 1
# - Found a 2 -> count2 = 2
# - Found a 0 -> count0 = 2
# - Found a 1 -> count1 = 2
# Final counts: count0 = 2, count1 = 2, count2 = 2
#
# Pass 2: Overwrite the array
# - Place `count0` (2) zeros: arr = [0, 0, 1, 2, 0, 1]
# - Place `count1` (2) ones:  arr = [0, 0, 1, 1, 0, 1]
# - Place `count2` (2) twos:  arr = [0, 0, 1, 1, 2, 2]
# Final sorted array: [0, 0, 1, 1, 2, 2]
#
# VISUAL DRY RUN:
# arr = [0, 1, 2, 0, 2, 2, 1, 1]
#
# 1. Initialize counts: count0 = 0, count1 = 0, count2 = 0
# 2. First Pass (Counting):
#    - After iterating through `arr`:
#    - count0 becomes 2 (for the two 0s)
#    - count1 becomes 3 (for the three 1s)
#    - count2 becomes 3 (for the three 2s)
#
# 3. Second Pass (Overwriting):
#    - `i = 0`. `i < count0 (2)`.
#    - `arr[0] = 0`. i=1. `arr` -> [0, 1, 2, 0, 2, 2, 1, 1]
#    - `arr[1] = 0`. i=2. `arr` -> [0, 0, 2, 0, 2, 2, 1, 1]
#    - `i = 2`. `i < count0 + count1 (5)`.
#    - `arr[2] = 1`. i=3. `arr` -> [0, 0, 1, 0, 2, 2, 1, 1]
#    - `arr[3] = 1`. i=4. `arr` -> [0, 0, 1, 1, 2, 2, 1, 1]
#    - `arr[4] = 1`. i=5. `arr` -> [0, 0, 1, 1, 1, 2, 1, 1]
#    - `i = 5`. `i < count0 + count1 + count2 (8)`.
#    - `arr[5] = 2`. i=6. `arr` -> [0, 0, 1, 1, 1, 2, 1, 1]
#    - `arr[6] = 2`. i=7. `arr` -> [0, 0, 1, 1, 1, 2, 2, 1]
#    - `arr[7] = 2`. i=8. `arr` -> [0, 0, 1, 1, 1, 2, 2, 2]
# 4. Return `arr` -> [0, 0, 1, 1, 1, 2, 2, 2]
#
# COMPLEXITY:
# Time Complexity: O(N) + O(N) = O(N). We iterate through the array twice.
# Space Complexity: O(1). We only use a few variables to store the counts.
#

def sortColorBetter(arr: List[int]) -> List[int]:
    count0, count1, count2 = 0, 0, 0

    # First pass: count the number of 0s, 1s, and 2s
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        elif num == 2:
            count2 += 1
    
    i = 0

    # Second pass: overwrite the array with the sorted values
    # Place all the 0s
    while i < count0:
        arr[i] = 0
        i += 1
    
    # Place all the 1s
    while i < count0 + count1:
        arr[i] = 1
        i += 1
    
    # Place all the 2s
    while i < count0 + count1 + count2:
        arr[i] = 2
        i += 1

    return arr

arr_better = [0, 1, 2, 0, 2, 2, 1, 1]
print(f"Better Sort: {sortColorBetter(arr_better)}")


# =================================================================================================
# APPROACH 3: OPTIMAL (Dutch National Flag Algorithm)
# =================================================================================================
#
# INTUITION:
# This problem is a classic example of the "Dutch National Flag problem". The goal is to sort
# the array in a single pass (O(N)) and with constant space (O(1)). We can achieve this by
# maintaining three pointers: `s` (for start), `i` (for current element), and `e` (for end).
# The array is conceptually divided into four sections:
# 1. `arr[0...s-1]`   : All 0s (the "red" part)
# 2. `arr[s...i-1]`   : All 1s (the "white" part)
# 3. `arr[i...e]`     : The unsorted section we are currently processing.
# 4. `arr[e+1...n-1]` : All 2s (the "blue" part)
#
# We iterate with the `i` pointer from the beginning to the end (`e`).
# - If `arr[i]` is 0, it belongs in the "0s" section. We swap it with `arr[s]` and increment both `s` and `i`.
# - If `arr[i]` is 1, it's already in the correct potential place. We just move to the next element by incrementing `i`.
# - If `arr[i]` is 2, it belongs in the "2s" section at the end. We swap it with `arr[e]` and decrement `e`. 
# We DO NOT increment `i` because the element we just brought from the end (`arr[e]`) needs to be processed.
# The loop continues as long as `i <= e`.
#
# VISUAL EXPLANATION:
#
# Initial State:
#   arr = [ ? | ? | ? | ? | ? | ? ]
#          s,i                     e
#
# We maintain this structure during the sort:
#   [   0s   |   1s   |  unsorted  |   2s   ]
#            ^        ^            ^
#            s        i            e
#
# VISUAL DRY RUN:
# arr = [0, 1, 2, 0, 2, 2, 1, 2], n = 8
# Initial: s = 0, i = 0, e = 7
#
# # i=0, s=0, e=7: arr[i] is 0.
# #   - arr[i] == 0. Swap arr[0] with arr[s=0]. No change.
# #   - s -> 1, i -> 1.
# #   - arr: [0, 1, 2, 0, 2, 2, 1, 2] | s=1, i=1, e=7 | Partitions: [0s: 0] [1s: ] [unsorted: 1,2,0,2,2,1,2] [2s: ]
#
# # i=1, s=1, e=7: arr[i] is 1.
# #   - arr[i] == 1. It's in the right place for now.
# #   - i -> 2.
# #   - arr: [0, 1, 2, 0, 2, 2, 1, 2] | s=1, i=2, e=7 | Partitions: [0s: 0] [1s: 1] [unsorted: 2,0,2,2,1,2] [2s: ]
#
# # i=2, s=1, e=7: arr[i] is 2.
# #   - arr[i] == 2. Swap arr[2] with arr[e=7].
# #   - arr becomes [0, 1, 2, 0, 2, 2, 1, 2].
# #   - e -> 6. `i` remains 2, because we need to check the new arr[2].
# #   - arr: [0, 1, 2, 0, 2, 2, 1, 2] | s=1, i=2, e=6 | Partitions: [0s: 0] [1s: 1] [unsorted: 2,0,2,2,1] [2s: 2]
#
# # i=2, s=1, e=6: arr[i] is 2.
# #   - arr[i] == 2. Swap arr[2] with arr[e=6].
# #   - arr becomes [0, 1, 1, 0, 2, 2, 2, 2].
# #   - e -> 5. `i` remains 2.
# #   - arr: [0, 1, 1, 0, 2, 2, 2, 2] | s=1, i=2, e=5 | Partitions: [0s: 0] [1s: 1] [unsorted: 1,0,2,2] [2s: 2,2]
#
# # i=2, s=1, e=5: arr[i] is 1.
# #   - arr[i] == 1. Move on.
# #   - i -> 3.
# #   - arr: [0, 1, 1, 0, 2, 2, 2, 2] | s=1, i=3, e=5 | Partitions: [0s: 0] [1s: 1,1] [unsorted: 0,2,2] [2s: 2,2]
#
# # i=3, s=1, e=5: arr[i] is 0.
# #   - arr[i] == 0. Swap arr[3] with arr[s=1].
# #   - arr becomes [0, 0, 1, 1, 2, 2, 2, 2].
# #   - s -> 2, i -> 4.
# #   - arr: [0, 0, 1, 1, 2, 2, 2, 2] | s=2, i=4, e=5 | Partitions: [0s: 0,0] [1s: 1,1] [unsorted: 2,2] [2s: 2,2]
#
# # i=4, s=2, e=5: arr[i] is 2.
# #   - arr[i] == 2. Swap arr[4] with arr[e=5]. No change in values.
# #   - e -> 4. `i` remains 4.
# #   - arr: [0, 0, 1, 1, 2, 2, 2, 2] | s=2, i=4, e=4 | Partitions: [0s: 0,0] [1s: 1,1] [unsorted: 2] [2s: 2,2,2]
#
# # i=4, s=2, e=4: arr[i] is 2.
# #   - arr[i] == 2. Swap arr[4] with arr[e=4]. No change.
# #   - e -> 3. `i` remains 4.
# #   - arr: [0, 0, 1, 1, 2, 2, 2, 2] | s=2, i=4, e=3 | Partitions: [0s: 0,0] [1s: 1,1] [unsorted: ] [2s: 2,2,2,2]
#
# # Loop condition i <= e (4 <= 3) is now FALSE. Loop terminates.
#
# Final Result: [0, 0, 1, 1, 2, 2, 2, 2]
#
# COMPLEXITY:
# Time Complexity: O(N), as each element is visited at most a constant number of times by pointers i and e.
# Space Complexity: O(1), as sorting is done in-place without any extra data structures.
#

# Simple helper function to swap two elements in an array
def swap(arr: List[int], i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]

def sortColorOp(arr: List[int]) -> List[int]:
    n = len(arr)
    s, i, e = 0, 0, n - 1

    # The loop continues as long as our 'current' pointer has not passed the 'end' pointer
    while i <= e:
        if arr[i] == 0:
            # If the element is 0, swap it with the element at the 'start' pointer
            swap(arr, i, s)
            # Both 'start' and 'current' pointers move forward
            s += 1
            i += 1
        elif arr[i] == 2:
            # If the element is 2, swap it with the element at the 'end' pointer
            swap(arr, i, e)
            # Only the 'end' pointer moves backward. 'i' stays put to process
            # the new element that was swapped from the end.
            e -= 1   
        elif arr[i] == 1: 
            # If the element is 1, it's in the correct middle partition.
            # Just move the 'current' pointer forward.
            i += 1
    
    return arr

arr_op = [0, 1, 2, 0, 2, 2, 1, 2]
print(f"Optimal Sort: {sortColorOp(arr_op)}")