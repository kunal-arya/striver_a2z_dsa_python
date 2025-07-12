from typing import List

# Problem Statement: 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#   - a, b, c, and d are distinct indices.
#   - nums[a] + nums[b] + nums[c] + nums[d] == target
# The solution set must not contain duplicate quadruplets.

# -----------------------------------------------------------------------------
# Approach 1: Brute Force
# -----------------------------------------------------------------------------
#
# Observation:
# The most direct way to find all quadruplets is to check every single possible
# combination of four distinct elements from the array.
#
# Inuition:
# We can use four nested loops to generate all possible combinations of four indices
# (i, j, k, l). To ensure the indices are distinct, each subsequent loop starts one
# position after the previous one (e.g., j starts at i+1).
#
# Visual Explanation:
# 1. Four nested loops (for i, j, k, l) pick four distinct numbers from the array.
# 2. Inside the innermost loop, calculate their sum.
# 3. If the sum matches the target, a potential quadruplet is found.
# 4. To handle uniqueness and avoid duplicate quadruplets like [-1, 0, 1, 2] and [2, 1, 0, -1],
#    the found quadruplet is sorted to create a canonical representation.
# 5. This sorted list is converted into a tuple and added to a set. The set data structure
#    automatically ensures that each unique quadruplet is stored only once.
# 6. Finally, the set of tuples is converted back into a list of lists for the output.
#
# Time Complexity: O(n⁴)
# - Due to the four nested loops iterating through the array.
# Space Complexity: O(number of unique quadruplets)
# - To store the result in the set. The space is proportional to the size of the output.

def fourSumBrute(arr: List[int], target: int):
    n = len(arr)
    res = set()
    for i in range(n):
        for j in range(i + 1,n):
            for k in range(j + 1,n):
                for l in range(k + 1,n):
                    current_sum = arr[i] + arr[j] + arr[k] + arr[l]

                    if current_sum == target:
                        new = [arr[i], arr[j], arr[k], arr[l]]
                        new.sort()
                        res.add(tuple(new))

    
    return [list(four) for four in res]

# -----------------------------------------------------------------------------
# Approach 2: Better (Using Hashing)
# -----------------------------------------------------------------------------
#
# Observation:
# We can improve the brute-force approach by reducing the number of loops. If we fix three
# numbers, the fourth required number is uniquely determined:
# fourth = target - (num1 + num2 + num3).
# We don't need a fourth loop just to search for this number.
#
# Inuition:
# We can use a hash set for a very fast lookup (O(1) on average). We can fix three
# numbers using three nested loops (for i, j, k). For each combination, we calculate
# the required fourth number and check if it has been seen before using the hash set.
#
# Visual Explanation:
# 1. Use three nested loops instead of four. The outer two loops fix `arr[i]` and `arr[j]`.
# 2. Inside the second loop, a `hash_set` is created.
# 3. The third loop (for k) iterates from `j + 1`. In this loop, we calculate the `fourth`
#    number required to meet the target.
# 4. We check if this `fourth` number already exists in our `hash_set`. If it does, we
#    have found a valid quadruplet.
# 5. Similar to the brute-force approach, we sort the quadruplet and add it to a result set
#    to handle uniqueness.
# 6. After the check, we add the current `arr[k]` to the `hash_set`, making it available for
#    future iterations of the `k` loop (for the same i and j).
#
# Time Complexity: O(n³)
# - We have three nested loops, and hash set operations take O(1) on average.
# Space Complexity: O(n) + O(number of quadruplets)
# - O(n) for the hash set used in the inner loop, plus space for the final result.

def fourSumBetter(arr: List[int], target: int):
    n = len(arr)
    res = set()

    for i in range(n):
        for j in range(i + 1,n):
            hash_set = set()
            for k in range(j + 1,n):
                fourth = target - (arr[i] + arr[j] + arr[k])

                if fourth in hash_set:
                    temp = [arr[i], arr[j], arr[k], fourth]
                    temp.sort()
                    res.add(tuple(temp))

                hash_set.add(arr[k])
    
    return [list(fourth) for fourth in res]

# -----------------------------------------------------------------------------
# Approach 3: Optimal (Two Pointers)
# -----------------------------------------------------------------------------
#
# Observation:
# The problem can be broken down. If we fix two numbers, the problem becomes finding
# two other numbers that sum up to a new target (`target - num1 - num2`). This is a
# classic "2Sum" problem. The 2Sum problem can be solved efficiently if the array is sorted.
#
# Inuition:
# First, sort the array. Then, iterate with two nested loops to fix the first two
# numbers (`arr[i]` and `arr[j]`). For the rest of the array, use the two-pointer
# technique (one pointer at the start `k`, one at the end `l`) to find the remaining
# two numbers. The sorted nature of the array allows us to efficiently skip duplicate
# values, eliminating the need for a set to store unique results.
#
# Visual Explanation:
# 1. Sort the entire array. This is critical for the two-pointer approach.
# 2. Use two outer loops to fix `arr[i]` and `arr[j]`.
# 3. Include checks like `if i > 0 and arr[i] == arr[i - 1]: continue`. This vital
#    optimization skips duplicate values for `i` (and `j`), preventing the algorithm from
#    finding the same quadruplet multiple times.
# 4. For each pair `(i, j)`, set up two pointers: `k = j + 1` and `l = n - 1`.
# 5. In a `while k < l` loop, calculate the sum of the four numbers.
#    - If `sum < target`, we need a larger sum, so move the left pointer: `k += 1`.
#    - If `sum > target`, we need a smaller sum, so move the right pointer: `l -= 1`.
#    - If `sum == target`, we found a quadruplet. Add it to the result list.
#      Then, advance both pointers (`k += 1`, `l -= 1`) and continue to skip any subsequent
#      duplicates for `k` and `l` to find the next unique pair.
#
# Time Complexity: O(n³)
# - O(n log n) for the initial sort.
# - The three nested loops (i, j, and the k/l while loop) result in O(n³) complexity,
#   which dominates the sort time.
# Space Complexity: O(1)
# - Ignoring the space required for the output list. We don't use any extra hash sets
#   or data structures that scale with the input size.

def fourSumOp(arr: List[int], target: int):
    n = len(arr)
    arr.sort()
    res = []

    for i in range(n):
        # Skip duplicates for the first element
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):
            # Skip duplicates for the second element
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            # Two-pointer approach for the remaining part of the array
            k = j + 1
            l = n - 1

            while k < l:
                current_sum = arr[i] + arr[j] + arr[k] + arr[l]

                if current_sum < target:
                    k += 1
                elif current_sum > target:
                    l -= 1
                else:
                    # Found a valid quadruplet
                    temp = [arr[i], arr[j], arr[k], arr[l]]
                    res.append(temp)
                    k += 1
                    l -= 1

                    # Skip duplicates for the third and fourth elements
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                    while k < l and arr[l] == arr[l + 1]:
                        l -= 1
    return res

# --- Example Execution ---
arr = [1,0,-1,0,-2,2]
target = 0

print("Brute Force: ", fourSumBrute(arr, target=target))
print("Better:      ", fourSumBetter(arr, target=target))
print("Optimal:     ", fourSumOp(arr, target=target))