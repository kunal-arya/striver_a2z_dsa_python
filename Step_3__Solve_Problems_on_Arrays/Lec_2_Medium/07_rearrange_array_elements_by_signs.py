# =================================================================================================
# PROBLEM: Rearrange Array Elements by Sign
# =================================================================================================
#
# Given a 1-indexed array of integers `nums` of even length, containing an equal number of
# positive and negative integers.
#
# You must rearrange the elements of `nums` such that the modified array follows these rules:
# 1. Every consecutive pair of integers has opposite signs.
# 2. For all integers with the same sign, the relative order is preserved.
# 3. The rearranged array begins with a positive integer.
#
# This means positive numbers should be at even indices (0, 2, 4...) and negative numbers
# should be at odd indices (1, 3, 5...).
#
# For example:
# Input: arr = [3, 1, -2, -5, 2, -4]
# Positive numbers in order: [3, 1, 2]
# Negative numbers in order: [-2, -5, -4]
# Output: [3, -2, 1, -5, 2, -4]
#
# The problem will be solved in two ways:
# 1. Brute Force / Better: A two-pass approach using extra space.
# 2. Optimal: A more elegant one-pass approach, also using extra space.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Brute Force (Separate into two arrays and then merge)
# =================================================================================================

# --- INTUITION ---
# The problem requires us to group positive and negative numbers while keeping their original
# relative order, and then interleave them. The most straightforward way to handle this is to
# physically separate the elements into two distinct groups first.
#
# 1.  **Separate:** Create two new lists, one for all the positive numbers and one for all the
#     negative numbers. Iterate through the input array and populate these lists. This naturally
#     preserves the relative order of elements within each group.
# 2.  **Combine:** Once we have our separated, ordered lists, we can build the final array. We know
#     the pattern: the first element comes from the positive list, the second from the negative,
#     the third from the positive, and so on. We can iterate and place them at the correct
#     even/odd indices in the original array.

# --- ALGORITHM ---
# 1. Create an empty list called `positive` and another called `negative`.
# 2. Iterate through the input array `arr`.
#    - If an element is positive or zero, append it to the `positive` list.
#    - If it's negative, append it to the `negative` list.
# 3. Now that we have two separate lists, iterate from `i = 0` to `(n/2) - 1`.
#    - For each `i`, place the i-th positive element at the even index `2*i`.
#    - Place the i-th negative element at the odd index `2*i + 1`.
# 4. Return the modified `arr`.

def rearrangeArrayElBrute(arr):
    n = len(arr)

    # --- Step 1: Separate positive and negative numbers into two lists ---
    # This preserves the relative order within each group.
    positive = []
    negative = []

    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    
    # --- Step 2: Reassemble the array from the two lists ---
    # We loop n/2 times, as there are n/2 positive and n/2 negative numbers.
    for i in range(n // 2):
        # Place the i-th positive number at the even index (0, 2, 4, ...)
        arr[2 * i] = positive[i]
        # Place the i-th negative number at the odd index (1, 3, 5, ...)
        arr[2 * i + 1] = negative[i]

    return arr

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? We perform two passes over the data. The first pass to segregate elements is O(N).
# The second pass to rebuild the array is O(N/2), which is also O(N). Total: O(N) + O(N) = O(N).
#
# Space Complexity: O(N)
# Why? We create two new lists, `positive` and `negative`, which together store all N elements
# of the original array. The space required grows linearly with the input size.
#
# --- HOW TO REMEMBER ---
# Brute Force = "Separate and Conquer" or "The Two Piles Method".
# You make two separate piles (lists) and then build the final result from them.
# This is intuitive but requires extra space for the piles.

arr = [3,1,-2,-5,2,-4]
print(f"Brute Force Result: {rearrangeArrayElBrute(arr)}") # Expected: [3, -2, 1, -5, 2, -4]

# =================================================================================================
# Approach 2: Optimal (One-Pass with Two Pointers)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach took two full passes. We can optimize this to a single pass.
# Instead of first separating all elements and then placing them, can we place each element
# directly into its final correct position in a new result array as we encounter it?
#
# Yes. We know exactly where the next positive number should go (the next available even index)
# and where the next negative number should go (the next available odd index).
# We can use two "pointers" to keep track of these positions.
#
# - A `positive_idx` pointer, starting at 0, will tell us where to place the next positive number.
# - A `negative_idx` pointer, starting at 1, will tell us where to place the next negative number.
#
# As we iterate through the input array, we check the sign of the number and place it in the
# result array at the position indicated by the corresponding pointer, then advance that pointer
# by 2 to get it ready for the next element of the same sign.

# --- ALGORITHM ---
# 1. Create a new answer array `res` of the same size `n`.
# 2. Initialize a pointer `pos_idx = 0` (to track the next even index).
# 3. Initialize another pointer `neg_idx = 1` (to track the next odd index).
# 4. Iterate through the input array `arr` just once.
# 5. For each element `num` in `arr`:
#    - If `num` is positive: place it in `res[pos_idx]` and increment `pos_idx` by 2.
#    - If `num` is negative: place it in `res[neg_idx]` and increment `neg_idx` by 2.
# 6. Return the `res` array.

def rearrangeArrayElOp(arr):
    n = len(arr)

    # Create a new array to store the result.
    res = [0] * n
    
    # `positive_idx` will point to the next available even index (0, 2, 4, ...).
    positive_idx = 0
    # `negative_idx` will point to the next available odd index (1, 3, 5, ...).
    negative_idx = 1

    # Iterate through the input array once.
    for i in range(n):
        # If the number is positive, place it at the next available positive slot.
        if arr[i] >= 0:
            res[positive_idx] = arr[i]
            # Move the pointer to the next even position.
            positive_idx += 2
        # Otherwise, the number is negative, so place it at the next available negative slot.
        else:
            res[negative_idx] = arr[i]
            # Move the pointer to the next odd position.
            negative_idx += 2
    
    return res

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? We iterate through the input array exactly once to place all elements into the result array.
#
# Space Complexity: O(N)
# Why? Although we are more time-efficient by using a single pass, we still create a new
# result array `res` of size N. Therefore, the space complexity remains O(N).
# This is considered optimal because an in-place solution that preserves relative order is
# very complex and less efficient in time.
#
# --- HOW TO REMEMBER ---
# Optimal = "Two-Pointer Placement" or "Fill the Slots".
# Instead of sorting into piles first, you directly place each item into its correct type of slot
# (even/odd) in the final answer. The two pointers just remember the next open slot for each type.

arr = [3,1,-2,-5,2,-4]
print(f"Optimal Approach Result: {rearrangeArrayElOp(arr)}") # Expected: [3, -2, 1, -5, 2, -4]

# =================================================================================================
# VARIANT: Unequal Number of Positive and Negative Elements
# =================================================================================================
#
# A common follow-up question is: What if the number of positive and negative integers is not equal?
# The goal is still to arrange them in an alternating pattern for as long as possible, and then
# place the remaining elements (which will all have the same sign) at the end of the array.
#
# The relative order of elements with the same sign must still be preserved.
#
# For example:
# Input: arr = [1, 2, -3, -1, -4, 5]
# Positives: [1, 2, 5]
# Negatives: [-3, -1, -4]
# Here they are equal, so the result is [1, -3, 2, -1, 5, -4]
#
# Input: arr = [-1, 2, 3, 4, -5]
# Positives: [2, 3, 4] (3 elements)
# Negatives: [-1, -5]  (2 elements)
# Result: [2, -1, 3, -5, 4]  (Alternating part is [2, -1, 3, -5]. Leftover is [4])
#
# --- INTUITION ---
# Since we can't create a perfectly alternating array for the entire length, the strategy is to:
# 1.  Create the alternating pattern for as long as both positive and negative numbers are available.
#     The length of this pattern will be determined by the smaller of the two groups.
# 2.  Once we run out of numbers from the smaller group, we will have a "leftover" set of numbers
#     from the larger group.
# 3.  Simply append these leftover numbers to the end of the array.
#
# This approach ensures the alternating pattern is maximized and the relative order is maintained.
# The most straightforward way to implement this is to first separate the numbers, just like in the
# brute-force method of the original problem.

# --- ALGORITHM ---
# 1. Create two lists, `pos` and `neg`, to store the positive and negative numbers separately.
#    This segregation preserves their relative order.
# 2. Iterate through the input `arr` and populate `pos` and `neg`.
# 3. Determine which list is smaller. Let the length of the shorter list be `min_len`.
# 4. Interleave the elements: Loop `i` from 0 to `min_len - 1`. In each iteration, place `pos[i]`
#    at index `2*i` and `neg[i]` at index `2*i + 1` in the result array.
# 5. Append the leftovers: After the loop, find the starting index for the leftovers, which is `2 * min_len`.
#    - If the `pos` list was longer, iterate through its remaining elements (from `min_len` onwards)
#      and place them at the end of the array.
#    - If the `neg` list was longer, do the same with its remaining elements.
# 6. Return the modified array.

def rearrangeArrayElOp2(arr):
    n = len(arr)
    pos = []
    neg = []

    # Step 1: Separate positives and negatives into two lists.
    for num in arr:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)

    p = len(pos)
    ne = len(neg)
    
    # Step 2: Interleave elements for as long as both lists have elements.
    # The number of pairs we can form is limited by the shorter list.
    if p > ne:
        # Case where there are more positives than negatives.
        # We can form 'ne' pairs.
        for i in range(ne):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
        
        # Now, append the remaining positive numbers.
        # The interleaved part took up 2 * ne spots.
        arr_idx = 2 * ne
        for i in range(ne, p):
            arr[arr_idx] = pos[i]
            arr_idx += 1
    else:
        # Case where there are more (or equal) negatives than positives.
        # We can form 'p' pairs.
        for i in range(p):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
        
        # Now, append the remaining negative numbers.
        # The interleaved part took up 2 * p spots.
        arr_idx = 2 * p
        for i in range(p, ne):
            arr[arr_idx] = neg[i]
            arr_idx += 1
    
    return arr

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? The process involves a few passes, but none are nested in a way that creates O(N^2) complexity.
# 1. Segregation pass: O(N)
# 2. Interleaving and appending passes: Together, these loops touch each element once to place it
#    in the final array. This is also O(N).
# The total complexity is O(N) + O(N) = O(N).
#
# Space Complexity: O(N)
# Why? We create two helper arrays (`pos` and `neg`) that, in total, store all N elements of the
# input array. The space required is proportional to the input size.
#
# --- HOW TO REMEMBER ---
# This variant is a direct extension of the "Separate and Conquer" method.
# Remember it as: "Interleave the common part, then append the rest."

arr_variant = [3, 1, -2, -5, 2, -4, -3, 8] # 4 positives, 4 negatives - for testing
print(f"Result for unequal lists (example 1): {rearrangeArrayElOp2(arr_variant)}") 
# Expected: [3, -2, 1, -5, 2, -4, 8, -3] -> My code logic is slightly different
# My code result for [3, 1, -2, -5, 2, -4, 8, -3]: [3, -2, 1, -5, 2, -4, 8, -3]

arr_variant_2 = [1, -2, -3, 4, 5, -6, 7] # 4 positives, 3 negatives
print(f"Result for unequal lists (example 2): {rearrangeArrayElOp2(arr_variant_2)}")
# Expected: [1, -2, 4, -3, 5, -6, 7]