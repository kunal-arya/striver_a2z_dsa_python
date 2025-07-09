# =================================================================================================
# PROBLEM: Permutations
# =================================================================================================
#
# Given an array `arr` of distinct integers, return all the possible permutations.
# You can return the answer in any order.
#
# For example:
# Input: arr = [1, 2, 3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
#
# This foundational problem helps in understanding the "Next Permutation" problem.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Generating Permutations using a Frequency Array (Extra Space)
# =================================================================================================

# --- INTUITION ---
# This approach uses classic recursion and backtracking. The idea is to build a permutation one
# element at a time.
#
# Imagine you have `n` empty slots to fill.
# - For the first slot, you can pick any of the `n` numbers from the input array.
# - For the second slot, you can pick any of the `n-1` *remaining* numbers.
# - ...and so on, until all slots are filled.
#
# To keep track of which numbers are "remaining" (i.e., have not been used in the current
# permutation we're building), we use an auxiliary `freq` (frequency) array. `freq[i] = True`
# means `arr[i]` is already in our temporary permutation (`ds`).
#
# The "backtracking" step is crucial: after a recursive call returns, we must undo our choice
# (e.g., remove the last added element and reset its frequency) so we can explore other possibilities.

# --- RECURSION TREE FOR arr = [1, 2, 3] ---
#
# f(ds=[], freq=[F,F,F])
# |
# +-- i=0, pick 1 --> f(ds=[1], freq=[T,F,F])
# |   |
# |   +-- i=1, pick 2 --> f(ds=[1,2], freq=[T,T,F])
# |   |   |
# |   |   +-- i=2, pick 3 --> f(ds=[1,2,3], freq=[T,T,T]) -> Base Case, Add [1,2,3]
# |   |
# |   +-- i=2, pick 3 --> f(ds=[1,3], freq=[T,F,T])
# |       |
# |       +-- i=1, pick 2 --> f(ds=[1,3,2], freq=[T,T,T]) -> Base Case, Add [1,3,2]
# |
# +-- i=1, pick 2 --> f(ds=[2], freq=[F,T,F])
# |   |
# |   +-- i=0, pick 1 --> f(ds=[2,1], freq=[T,T,F])
# |   |   |
# |   |   +-- i=2, pick 3 --> f(ds=[2,1,3], freq=[T,T,T]) -> Base Case, Add [2,1,3]
# |   |
# |   +-- i=2, pick 3 --> f(ds=[2,3], freq=[F,T,T])
# |       |
# |       +-- i=0, pick 1 --> f(ds=[2,3,1], freq=[T,T,T]) -> Base Case, Add [2,3,1]
# |
# +-- i=2, pick 3 --> f(ds=[3], freq=[F,F,T])
#     |
#     ... (generates [3,1,2] and [3,2,1])
#

# --- ALGORITHM ---
# 1. Start with an empty permutation `ds` and a boolean `freq` array, all `False`.
# 2. **Base Case:** If the size of `ds` equals the size of the input `arr`, we have a complete permutation. Add a copy of `ds` to the final answer list and return.
# 3. **Recursive Step:** Loop through every element in the input `arr`.
# 4. If the element `arr[i]` has not been used yet (`freq[i]` is `False`):
#    a. Mark it as used: `freq[i] = True`.
#    b. Add it to the current permutation: `ds.append(arr[i])`.
#    c. Make a recursive call to find the rest of the permutation.
#    d. **Backtrack:** Undo the changes. Remove the element `ds.pop()` and un-mark its frequency `freq[i] = False`.

from typing import List

def printAllPermutations(arr: List[int]):
    n = len(arr)
    freq = [False] * n         # Frequency array to mark used elements
    ans: List[List[int]] = []  # Stores all final permutations
    ds = []                    # Data structure to build one permutation at a time

    recurPermutate(arr, ans, ds, freq)
    return ans

def recurPermutate(arr, ans: List[List[int]], ds: List[int], freq):
    # Base case: if our temporary permutation is full, we found a valid one.
    if len(ds) == len(arr):
        if ds not in ans:
            ans.append(ds[:]) # Append a copy, not the reference
        return

    # Iterate through all numbers in the original array
    for i in range(len(arr)):
        # If the number at index 'i' is not already used
        if not freq[i]:
            freq[i] = True         # Mark as used
            ds.append(arr[i])      # Add to current permutation
            recurPermutate(arr, ans, ds, freq) # Recurse
            # Backtrack: undo the choice to explore other paths
            ds.pop()
            freq[i] = False

# --- COMPLEXITY ---
# Time: O(N! * N). There are N! permutations. For each, we iterate N times in the recursion.
# Space: O(N) for the frequency array and O(N) for recursion depth. The answer list takes O(N! * N).


# =================================================================================================
# Approach 2: Generating Permutations using Swapping (In-place)
# =================================================================================================

# --- INTUITION ---
# This is a more space-efficient way to think about the problem. Instead of building a new list,
# we generate permutations by swapping elements in the original array itself.
#
# The idea is to fix the element at each position, one by one, from left to right.
# - To fix the element at index `0`, we can try putting every number from the array at this position.
#   We do this by swapping `arr[0]` with `arr[0]`, then `arr[0]` with `arr[1]`, and so on.
# - After fixing the element at index `0` (by swapping), we recursively solve the problem for the
#   rest of the array, i.e., from `index + 1`.
# - The backtracking step here is to swap the elements back to their original positions, so the array
#   is restored for the next iteration of the loop.

# --- RECURSION TREE FOR arr = [1, 2, 3] ---
#
# f(idx=0, arr=[1,2,3])
# |
# +-- i=0, swap(0,0) -> arr=[1,2,3] -> f(idx=1, arr=[1,2,3])
# |   |
# |   +-- i=1, swap(1,1) -> arr=[1,2,3] -> f(idx=2, arr=[1,2,3])
# |   |   |
# |   |   +-- i=2, swap(2,2) -> arr=[1,2,3] -> f(idx=3) -> Base Case, Add [1,2,3]
# |   |       (swap back)
# |   |   (swap back)
# |   +-- i=2, swap(1,2) -> arr=[1,3,2] -> f(idx=2, arr=[1,3,2])
# |       |
# |       +-- i=2, swap(2,2) -> arr=[1,3,2] -> f(idx=3) -> Base Case, Add [1,3,2]
# |           (swap back)
# |       (swap back to [1,2,3])
# |
# +-- i=1, swap(0,1) -> arr=[2,1,3] -> f(idx=1, arr=[2,1,3])
# |   |
# |   ... (generates [2,1,3] and [2,3,1])
# |   (swap back to [1,2,3])
# |
# +-- i=2, swap(0,2) -> arr=[3,2,1] -> f(idx=1, arr=[3,2,1])
#     |
#     ... (generates [3,2,1] and [3,1,2])
#     (swap back to [1,2,3])

# --- ALGORITHM ---
# 1. Start a recursive function with the initial `index = 0`.
# 2. **Base Case:** If `index` reaches the end of the array, the current state of the array is a complete permutation. Add a copy to the answer list.
# 3. **Recursive Step:** Loop `i` from the current `index` to the end of the array.
# 4. For each `i`:
#    a. `swap(arr, index, i)`: Place the element `arr[i]` at the current `index` position.
#    b. `recursivePermutation2(arr, ans, index + 1)`: Recursively generate permutations for the rest of the array.
#    c. **Backtrack:** `swap(arr, index, i)`: Swap back to restore the array for the next iteration of the loop.

def printAllPermutations2(arr: List[int]):
    ans = []
    recursivePermutation2(arr, ans, 0)
    return ans

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def recursivePermutation2(arr, ans, idx):
    # Base case: if we have fixed all positions up to the end, we have a permutation.
    if idx == len(arr):
        if arr not in ans:
            ans.append(arr[:])
        return

    # For the current position 'idx', try placing every element from 'idx' to the end.
    for i in range(idx, len(arr)):
        swap(arr, i, idx) # Place arr[i] at the current fixed position
        recursivePermutation2(arr, ans, idx + 1) # Recurse for the next position
        swap(arr, i, idx) # Backtrack: swap back to restore the original order for the loop

# --- COMPLEXITY ---
# Time: O(N! * N). Same reasoning as Approach 1.
# Space: O(N) for recursion depth. More space-efficient as it doesn't need a frequency array.


# =================================================================================================
# PROBLEM: Next Permutation
# =================================================================================================
#
# Implement the next permutation, which rearranges numbers into the lexicographically next
# greater permutation of numbers. If such an arrangement is not possible, it must rearrange
# it as the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.
#
# Example:
# [1, 2, 3] -> [1, 3, 2]
# [3, 2, 1] -> [1, 2, 3]
# [1, 1, 5] -> [1, 5, 1]
#
# =================================================================================================

# ---------------------------------
# Brute Force Approach
# ---------------------------------

# --- INTUITION ---
# The most straightforward way is to literally find all possible orderings (permutations) of the
# numbers, sort them lexicographically (like words in a dictionary), find the given input
# array in this sorted list, and then return the one that comes right after it.
# If the input array is the very last one in the sorted list, we "wrap around" and return the first one.

def next_permutation_brute(arr: List[int]):
    # Step 1: Generate all unique permutations
    ans = sorted(printAllPermutations2(arr)) # Assumes distinct elements, otherwise needs modification
    
    # Step 2: Find the current permutation in the sorted list
    for i in range(len(ans)):
        if ans[i] == arr:
            # Step 3: Return the next one, or the first one if it's the last
            if i == len(ans) - 1:
                return ans[0] # Wrap around
            else:
                return ans[i + 1]
            
    return -1 # Should not be reached for valid inputs

# --- COMPLEXITY ---
# Time: O(N! * N). Generating all permutations is extremely slow.
# Space: O(N! * N). Storing all permutations requires a massive amount of memory.
# This approach is only feasible for very small N.

arr = [2,1,5,4,3,0,0] # This array has duplicates, the simple permutation generator needs a tweak to handle them, but the logic holds
print(f"Brute Force Result: {next_permutation_brute(arr)}")


# ---------------------------------
# Optimal Approach (Single Pass)
# ---------------------------------

# --- INTUITION AND KEY OBSERVATIONS ---
# The goal is to find the *next* lexicographically greater permutation with minimal changes.

# OBSERVATION 1: The Dictionary Analogy & The Break Point
# Think about words in a dictionary. The word `report` comes just before `repose`.
# They share the longest possible prefix: `repo`. The change happens at the first character
# from the right that is not part of a descending suffix. In `report`, the suffix `rt` is descending.
# The character before it is `o`.
#
# Applying this to numbers: a permutation like `[2, 1, 5, 4, 3]` has a suffix `[5, 4, 3]` that is
# sorted in descending order. This means `543` is the largest possible number you can make with these
# three digits. To get the next permutation, you can't just shuffle the suffix. You must change
# the number just before it, which is `1`.
#
# This `1` is our "break point" or "pivot". It's the first number from the right that is smaller
# than its right neighbor (`1 < 5`). Finding this point is Step 1. We scan from the right because
# we want to keep the prefix as long as possible, thus making the smallest possible change.

# OBSERVATION 2: The Swap
# We've identified the pivot `arr[i]` (the `1` in our example). We need to increase it to make the
# overall number larger. We should swap it with a number from its right-hand suffix (`[5, 4, 3]`).
# To make the resulting permutation the *very next* one (i.e., the smallest possible increase),
# we must swap `arr[i]` with the *smallest number in the suffix that is still greater than `arr[i]`*.
#
# In `[2, 1, 5, 4, 3]`:
# - Pivot is `1`.
# - Suffix is `[5, 4, 3]`.
# - Numbers in suffix greater than `1` are `5, 4, 3`.
# - The smallest of these is `3`.
# - So, we swap `1` and `3`. The array becomes `[2, 3, 5, 4, 1]`.

# OBSERVATION 3: Minimizing the Suffix
# After the swap, our array is `[2, 3, 5, 4, 1]`. The prefix `[2, 3]` is now fixed.
# To get the smallest possible final number, the new suffix `[5, 4, 1]` must be arranged in its
# smallest possible permutation, which is ascending order: `[1, 4, 5]`.
#
# So, we sort the suffix.
# Final result: `[2, 3, 1, 4, 5]`.
#
# A key optimization: The original suffix (`[5, 4, 3]`) was already sorted in descending order.
# After we swap an element out of it, the new suffix (`[5, 4, 1]` in our example) remains sorted
# in descending order. Therefore, to sort it in ascending order, we simply need to **reverse** it.

# --- ALGORITHM ---
# 1. **Find Break Point:** Iterate from the second-to-last element (`n-2`) backwards. Find the first index `i` such that `arr[i] < arr[i+1]`. Let's call this `idx`.
# 2. **Handle Edge Case:** If no such index is found (`idx == -1`), the entire array is in descending order (e.g., `[3,2,1]`). This is the last permutation. The next one is the first one (sorted ascending). So, just reverse the whole array and return.
# 3. **Find Swap Element:** Iterate from the end of the array backwards to `idx`. Find the first element `arr[j]` that is greater than `arr[idx]`.
# 4. **Swap:** Swap `arr[idx]` and `arr[j]`.
# 5. **Reverse Suffix:** Reverse the part of the array from `idx + 1` to the end.

def next_permutation_op(arr: List[int]):
    n = len(arr)
    idx = -1
    # Step 1: Find the break Point.
    # The first element from the right which is smaller than its right neighbor.
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            idx = i
            break

    # If no break point is found, the array is the last permutation.
    if idx == -1:
        arr.reverse()
        return arr
    
    # Step 2: Find the smallest element on the right of arr[idx] which is > arr[idx]
    # and swap them.
    for i in range(n - 1, idx, -1): # Iterate from end towards idx
        if arr[i] > arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            break

    # Step 3: Reverse the part of the array to the right of the original break point.
    # This makes the suffix the smallest possible permutation.
    start = idx + 1
    end = n - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

# --- COMPLEXITY ---
# Time: O(N). In the worst case, we make three passes over the array (one to find idx, one to find swap, one to reverse).
# Space: O(1). The operations are done in-place.

arr = [2,1,5,4,3,0,0]
print(f"Optimal Result: {next_permutation_op(arr)}") # Expected: [2, 3, 0, 0, 1, 4, 5]