# =================================================================================================
# PROBLEM: Leaders in an Array
# =================================================================================================
#
# You are given an array `arr` of positive integers. Your task is to find all the leaders in the array.
#
# Definition of a Leader: An element is a "leader" if it is greater than or equal to all the
# elements to its right. The rightmost element is always considered a leader by this definition
# because there are no elements to its right.
#
# For example:
# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation:
# - 17 is a leader because all elements to its right [4, 3, 5, 2] are smaller than it.
# - 5 is a leader because the element to its right [2] is smaller than it.
# - 2 is a leader because it's the rightmost element.
#
# The problem will be solved in two ways:
# 1. Brute Force: A straightforward approach that directly follows the definition.
# 2. Optimal: An efficient single-pass solution that scans the array from right to left.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Brute Force (Check every element against all elements to its right)
# =================================================================================================

# --- INTUITION ---
# The most direct way to solve this is to take the definition of a leader and translate it
# directly into code. The definition says "for an element to be a leader, it must be greater
# than all elements to its right."
#
# This leads to a simple, albeit slow, plan:
# 1. Pick an element from the array. Let's call it our `candidate`.
# 2. To verify if it's a leader, we must compare it with every single element that comes after it.
# 3. If we find even one element to its right that is larger than our `candidate`, we know it's
#    not a leader, and we can stop checking for this candidate and move to the next one.
# 4. If we check all elements to its right and none are larger, then our `candidate` is a leader.
# This process is repeated for every element in the array.

# --- ALGORITHM ---
# 1. Initialize an empty list `leader` to store the results.
# 2. Use an outer loop `i` to iterate through each element of the array. This `arr[i]` is our candidate.
# 3. For each candidate, assume it is a leader by using a boolean flag, e.g., `isLeader = True`.
# 4. Use an inner loop `j` to iterate through all elements to the right of `i` (from `i+1` to the end).
# 5. Inside the inner loop, if any element `arr[j]` is greater than our candidate `arr[i]`, then
#    `arr[i]` fails the test. Set `isLeader = False` and `break` the inner loop immediately.
# 6. After the inner loop finishes, if `isLeader` is still `True`, it means no element to the
#    right was greater, so we add `arr[i]` to our `leader` list.
# 7. Return the `leader` list.

from typing import List

def leaderInArrBrute(arr: List[int]) -> List[int]:
    n = len(arr)
    leader = []

    # Outer loop to pick a candidate element.
    for i in range(n):
        num = arr[i]
        isLeader = True # Assume the current number is a leader until proven otherwise.

        # Inner loop to check all elements to the right of the candidate.
        for j in range(i + 1, n):
            # If we find any element to the right that is greater, it's not a leader.
            if arr[j] > num:
                isLeader = False
                break # No need to check further for this candidate.
        
        # If the flag is still true after checking all right-side elements, it's a leader.
        if isLeader:
            leader.append(num)

    return leader

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2)
# Why? We have two nested loops. The outer loop runs N times, and for each of those iterations,
# the inner loop can run up to N times in the worst case. This gives us an N * N complexity.
#
# Space Complexity: O(L) where L is the number of leaders.
# Why? We are using an extra list `leader` to store the result. In the worst case,
# (e.g., a sorted descending array like [5, 4, 3, 2, 1]), every element is a leader,
# so the space required would be O(N).
#
# --- HOW TO REMEMBER ---
# Brute Force = "Literal Definition". You take the problem's definition and implement it
# step-by-step, which often results in nested loops for "check all X against all Y" scenarios.


arr = [10,22,12,3,0,6]
print(f"Brute Force Result: {leaderInArrBrute(arr)}") # Expected: [22, 12, 6]

# =================================================================================================
# Approach 2: Optimal (Scan from the Right)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach is slow because we repeatedly scan the same right-side elements.
# The key insight for optimization is to change our perspective. Instead of scanning from left
# to right, let's scan from RIGHT to LEFT.
#
# Why does this help?
# - We know the rightmost element is always a leader. So, we can start with it.
# - Now, let's move one step to the left. For this new element to be a leader, it only needs to
#   be greater than or equal to all elements to its right. But we just came from the right! We can
#   simply keep track of the maximum element we have encountered so far on our journey from the right.
#
# Let's maintain a variable, `max_from_right`.
# 1. Start at the end. The rightmost element is a leader. Initialize `max_from_right` with its value.
# 2. Move left. For the current element, compare it with `max_from_right`.
#    - If the current element is greater than `max_from_right`, it means it's greater than *all*
#      elements to its right. So, it's a new leader! We then update `max_from_right` to this new, larger value.
#    - If it's not greater, it can't be a leader. We still update `max_from_right` if needed.
# This way, we only need a single pass.

# --- ALGORITHM ---
# 1. Initialize an empty list `leader` to store the results.
# 2. Get the last element of the array. It's always a leader, so add it to the `leader` list.
# 3. Initialize a variable `max_from_right` with the value of the last element.
# 4. Iterate through the array from the second-to-last element down to the first (from `n-2` to `0`).
# 5. In each iteration, let the current element be `num`.
#    a. Compare `num` with `max_from_right`. If `num > max_from_right`, then `num` is a leader. Add it to the `leader` list.
#    b. After the check, update `max_from_right = max(max_from_right, num)`. This is crucial to ensure `max_from_right` always holds the true maximum of the elements seen so far from the right.
# 6. The leaders have been collected in reverse order. Reverse the `leader` list to get the correct final order.
# 7. Return the `leader` list.

def leaderInArrOp(arr: List[int]) -> List[int]:
    n = len(arr)
    leader = []
    
    # The rightmost element is always a leader.
    max_from_right = arr[n - 1]
    leader.append(max_from_right)

    # Iterate from the second-to-last element to the beginning.
    for i in range(n - 2, -1, -1):
        num = arr[i]

        # If the current element is greater than the max found so far from the right...
        if num > max_from_right:
            # ...it is a leader.
            leader.append(num)
            # This element is now the new maximum from the right.
            max_from_right = num

    # The leaders were found from right to left, so the list is in reverse order.
    leader.reverse()
    return leader

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? We iterate through the array once from right to left (O(N)). The final reverse operation
# also takes O(L) time, where L is the number of leaders (at most N). Thus, the total time is linear.
#
# Space Complexity: O(L) or O(N) in the worst case.
# Why? Same as the brute-force approach, we need space to store the output leaders.
#
# --- HOW TO REMEMBER ---
# Optimal = "Scan from the Right". For problems involving "elements to the right", a right-to-left
# scan is a powerful optimization technique. It allows you to maintain the state of the "right side"
# in a single variable (`max_from_right`) instead of re-scanning.

arr = [10,22,12,3,0,6]
print(f"Optimal Approach Result: {leaderInArrOp(arr)}") # Expected: [22, 12, 6]