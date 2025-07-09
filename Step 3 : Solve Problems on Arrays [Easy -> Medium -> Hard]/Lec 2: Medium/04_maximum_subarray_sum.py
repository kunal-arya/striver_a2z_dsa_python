# =================================================================================================
# PROBLEM: Maximum Subarray Sum
# =================================================================================================
#
# Given an array of integers, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# For example:
# Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# The subarray [4, -1, 2, 1] has the largest sum = 6.
#
# The problem will be solved in three ways:
# 1. Brute Force: The most obvious, but very slow approach.
# 2. Better: An improvement that reduces one level of looping.
# 3. Optimal (Kadane's Algorithm): The most efficient, single-pass solution.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Brute Force (Generate all subarrays, sum them up, find max)
# =================================================================================================

# --- INTUITION ---
# The most straightforward way to solve this is to consider every single possible subarray.
# How do we define a subarray? By its starting point (i) and its ending point (j).
# So, the plan is:
# 1. Generate all possible pairs of (start index, end index).
# 2. For each pair, calculate the sum of the elements in that subarray.
# 3. Keep track of the maximum sum found so far.
# This requires three nested loops:
# - Loop i: To select the starting element of the subarray.
# - Loop j: To select the ending element of the subarray.
# - Loop k: To iterate from i to j and calculate the sum.

# --- ALGORITHM ---
# 1. Initialize `maxSum` to a very small number (negative infinity).
# 2. Use a loop `i` from 0 to n-1 to mark the start of the subarray.
# 3. Inside it, use a loop `j` from `i` to n-1 to mark the end of the subarray.
# 4. Inside this, use a loop `k` from `i` to `j` to calculate the sum of `arr[k]`.
# 5. Compare this `sum` with `maxSum` and update `maxSum` if the current sum is greater.
# 6. After all loops complete, `maxSum` will hold the answer.

def maximumSubArraySumBrute(arr):
    n = len(arr)
    maxSum = float("-inf") # Start with the smallest possible number

    # Loop 1: Defines the starting point of the subarray
    for i in range(n):
        # Loop 2: Defines the ending point of the subarray
        for j in range(i, n):
            # Now we have a subarray from index i to j. Let's find its sum.
            current_sum = 0
            # Loop 3: Calculates the sum of the current subarray (from i to j)
            for k in range(i, j + 1):
                current_sum += arr[k]
            
            # Update maxSum if the sum of the current subarray is greater
            maxSum = max(maxSum, current_sum)

    return maxSum

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^3)
# Why? We have three nested loops. The outer two loops define O(N^2) subarrays, and for each of
# these subarrays, we iterate again (up to N times) to find its sum.
#
# Space Complexity: O(1)
# Why? We are not using any extra space that scales with the input array size.
#
# --- HOW TO REMEMBER ---
# Brute Force = "Generate and Check Everything". Here, we generate every subarray (loops i, j)
# and then check its sum (loop k). Three nested loops = O(N^3).


arr = [-2,-3,4,-1,-2,1,5,-3]
print(f"Brute Force Result: {maximumSubArraySumBrute(arr)}") # Expected: 7 (from [4,-1,-2,1,5])

# =================================================================================================
# Approach 2: Better (Optimize the sum calculation)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach was slow because of the third loop (k). It recalculated the sum
# of the subarray from scratch every single time. We can optimize this.
#
# For a fixed starting point `i`, as we extend the ending point `j`, we don't need to
# re-calculate the sum of the subarray `arr[i...j]` from the beginning. We can just take the
# sum of the previous subarray `arr[i...j-1]` and add the new element `arr[j]`.
#
# This simple optimization eliminates the need for the third loop.

# --- ALGORITHM ---
# 1. Initialize `maxSum` to a very small number.
# 2. Use a loop `i` from 0 to n-1 to mark the start of the subarray.
# 3. Inside `i`, initialize `current_sum = 0`.
# 4. Use a second loop `j` from `i` to n-1. In this loop:
#    a. Add `arr[j]` to `current_sum`. Now `current_sum` holds the sum of `arr[i...j]`.
#    b. Compare `current_sum` with `maxSum` and update `maxSum` if needed.
# 5. Return `maxSum`.

def maximumSubArraySumBetter(arr):
    n = len(arr)
    maxSum = float('-inf')

    # Loop 1: Fix the starting point of the subarray
    for i in range(n):
        current_sum = 0
        # Loop 2: Iterate through all possible ending points for the fixed start
        for j in range(i, n):
            # Extend the subarray by one element and update the sum
            current_sum += arr[j]
            # Check if this new subarray sum is the maximum we've seen so far
            maxSum = max(maxSum, current_sum)
    
    return maxSum

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2)
# Why? We have two nested loops. This is a significant improvement over O(N^3).
#
# Space Complexity: O(1)
# Why? We are still only using a few variables, not creating any large data structures.
#
# --- HOW TO REMEMBER ---
# Better = "Eliminate Redundant Work". We got rid of the innermost loop by carrying the sum
# forward instead of recalculating it. Two nested loops = O(N^2).

arr = [-2,-3,4,-1,-2,1,5,-3]
print(f"Better Approach Result: {maximumSubArraySumBetter(arr)}") # Expected: 7


# =================================================================================================
# Approach 3: Optimal (Kadane's Algorithm)
# =================================================================================================

# --- INTUITION ---
# The previous approaches still considered many unnecessary subarrays. Kadane's algorithm is
# a brilliant, single-pass dynamic programming approach.
#
# The core idea is this: As we iterate through the array, we keep track of the maximum possible
# sum of a subarray that *ends at the current position*. Let's call this `current_sum`.
#
# For each new element, we have two choices:
# 1. Either we extend the previous subarray by adding the new element to `current_sum`.
# 2. Or, we start a fresh new subarray, because the `current_sum` from before was negative,
#    and carrying it forward would only decrease our total sum. A negative "prefix" can never
#    help maximize a future sum.
#
# So, the rule is simple: keep adding elements to `current_sum`. At each step, update a
# global `maxSum`. If at any point `current_sum` becomes negative, we reset it to 0,
# effectively "dropping" the previous subarray because it's no longer useful.

# --- ALGORITHM ---
# 1. Initialize `maxSum` to a very small number (to handle cases where all numbers are negative).
# 2. Initialize `current_sum` to 0.
# 3. Iterate through the array one element at a time (`num`).
#    a. Add the current element to `current_sum`: `current_sum += num`.
#    b. Check if this `current_sum` is greater than `maxSum`. If yes, update `maxSum`.
#    c. **The key step**: If `current_sum` becomes negative, reset it to 0. This is like saying,
#       "This subarray has a negative sum, it's dead weight. Let's start a new subarray from the next element."
# 4. Return `maxSum`.

def maxSubArraySumOp(arr):
    # `maxSum` stores the global maximum sum found so far, across all subarrays.
    # We initialize it to a very small number to correctly handle arrays with all negative numbers.
    # e.g., for [-2, -1], the answer should be -1, not 0.
    maxSum = float("-inf")
    
    # `current_sum` stores the sum of the subarray we are currently considering.
    current_sum = 0

    # Iterate through the array just once.
    for num in arr:
        # Add the current element to our running subarray sum.
        current_sum += num

        # Did this new, extended subarray create a new maximum?
        if maxSum < current_sum:
            maxSum = current_sum
        
        # KADANE'S CRUCIAL STEP:
        # If the current subarray sum is negative, it cannot be a prefix of any
        # future maximum subarray. So, we discard it and start fresh.
        if current_sum < 0:
            current_sum = 0

    return maxSum

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? We only iterate through the array a single time.
#
# Space Complexity: O(1)
# Why? We only use two variables (`maxSum` and `current_sum`) regardless of the array size.
#
# --- HOW TO REMEMBER ---
# Kadane's Algorithm = "The 'Don't Carry Negative Baggage' Algorithm".
# If your current path (sum) becomes negative, drop it and start a new path from the next step.

arr = [-2,-3,4,-1,-2,1,5,-3]
print(f"Optimal (Kadane's) Result: {maxSubArraySumOp(arr)}") # Expected: 7