# =================================================================================================
# PROBLEM: 128. Longest Consecutive Sequence
# =================================================================================================
#
# Given an unsorted array of integers `nums`, your task is to return the length of the
# longest consecutive elements sequence.
#
# The crucial constraint is that your algorithm must run in O(n) time complexity.
#
# For example:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is [1, 2, 3, 4]. Its length is 4.
#
# The problem will be solved in three ways:
# 1. Brute Force: A simple but highly inefficient approach.
# 2. Better: An improved approach using sorting.
# 3. Optimal: The most efficient solution using a hash set, meeting the O(n) requirement.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Brute Force (For each element, search for its sequence)
# =================================================================================================

# --- INTUITION ---
# The most straightforward idea is to check every number in the array and see if it can be the
# starting point of a consecutive sequence.
# For each element `x`, we can search the entire array to see if `x+1` exists. If it does, we then
# search for `x+2`, and so on. We keep a count of how long each potential sequence is and
# update a global `longest` variable.
#
# This is "brute force" because for every single element, we are repeatedly searching the
# entire array, which is very time-consuming.

# --- ALGORITHM ---
# 1. Initialize `longest` to 1 (since any single element is a sequence of length 1).
# 2. Iterate through each element `num` in the input array `arr`.
# 3. For each `num`, assume it's the start of a sequence. Initialize `current_count = 1`.
# 4. Use a `while` loop to check if `num + 1` exists in the array.
#    - The check `num + 1 in arr` requires a linear scan of the array, which takes O(N) time.
# 5. If it exists, increment `num` by 1 and increment `current_count`. Continue the `while` loop.
# 6. Once the sequence breaks (e.g., `num + 1` is not found), update `longest = max(longest, current_count)`.
# 7. After checking all elements, return `longest`.

from typing import List

def longestSubsequenceBrute(arr: List[int]) -> int:
    if not arr: return 0
    longest = 1

    # For every element in the array...
    for i in range(len(arr)):
        x = arr[i]
        current_count = 1
        # ...try to build a sequence starting from it.
        # This 'in' check on a list is O(N) and is the source of the inefficiency.
        while x + 1 in arr:
            x = x + 1
            current_count += 1
        longest = max(longest, current_count)
    
    return longest

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2) or O(N^3)
# Why? The outer loop runs N times. The inner `while` loop's `in arr` check is O(N). If the
# sequence is long, this check happens many times for a single outer loop iteration.
# A simpler way to view it: for each of the N elements, we might search the array up to N times.
# This results in a complexity of at least O(N^2).
#
# Space Complexity: O(1)
# Why? We are not using any extra data structures that scale with the input size.
#
# --- HOW TO REMEMBER ---
# Brute Force = "Search for everything." For each number, we search the entire array again and again.
# The `in list` operation is the performance bottleneck.

arr = [102,4,100,1,101,2,3,1,1]
print(f"Brute Force Result: {longestSubsequenceBrute(arr)}") # Expected: 4


# =================================================================================================
# Approach 2: Better (Using Sorting)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach was slow because we had to search for consecutive elements. What if we
# could place all the elements in order first? Sorting the array does exactly that!
#
# If we sort the array, any consecutive sequence like `[1, 2, 3, 4]` will appear as adjacent
# elements in the sorted array (possibly with duplicates in between, e.g., `[1, 2, 2, 3, 4]`).
#
# After sorting, we can just do a single pass through the array and keep track of the current
# consecutive streak.

# --- ALGORITHM ---
# 1. Handle the edge case of an empty array.
# 2. Sort the input array `arr`. This is the key step.
# 3. Initialize `longest = 1` and `current_count = 1`.
# 4. Keep track of the `last_smallest` element in the current sequence. Initialize it to the first element of the sorted array.
# 5. Iterate through the sorted array from the second element.
#    - If the current number is the same as `last_smallest` (a duplicate), ignore it and continue.
#    - If the current number is `last_smallest + 1`, it extends our sequence. Increment `current_count` and update `last_smallest`.
#    - If the sequence is broken, reset `current_count` to 1 and update `last_smallest` to the current number.
# 6. In every step, update `longest = max(longest, current_count)`.
# 7. Return `longest`.

def longestSubsequenceBetter(arr: List[int]) -> int:
    if not arr: return 0
    
    # The core of this approach is sorting the array first.
    arr.sort()

    longest = 1
    current_count = 1
    # `last_smallest` tracks the last unique number in our current sequence.
    last_smallest = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]
        
        # If the number is a duplicate of the last one, skip it.
        if num == last_smallest:
            continue
        # If it's the next number in the sequence, increment the count.
        elif num - 1 == last_smallest:
            current_count += 1
        # If the sequence is broken, reset the count.
        else:
            current_count = 1
        
        # Update the last number seen and the longest count found so far.
        last_smallest = num
        longest = max(longest, current_count)

    return longest

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N log N)
# Why? The dominant operation is sorting the array, which takes O(N log N) time. The subsequent
# single pass through the array takes O(N) time. The total complexity is O(N log N + N) = O(N log N).
#
# Space Complexity: O(1) or O(N)
# Why? This depends on the sorting algorithm used by the language. Python's Timsort can use up to
# O(N) space in the worst case. If an in-place sort like Heapsort were used, it would be O(1).
#
# --- HOW TO REMEMBER ---
# Better = "Sort and Scan". Sorting makes finding consecutive elements trivial, but it isn't fast enough
# to meet the O(N) constraint of the problem.


# =================================================================================================
# Approach 3: Optimal (Using a Hash Set)
# =================================================================================================

# --- INTUITION ---
# The sorting approach is O(N log N). To achieve the required O(N), we need a way to find numbers
# without sorting. This points towards a hash-based data structure (like a hash set or hash map)
# which provides average O(1) time for lookups.
#
# We can put all the numbers into a hash set. This allows us to check for the existence of any
# number (e.g., `x+1`) in constant time. This is a huge improvement over the O(N) list search.
#
# However, if we just iterate through the set and for each number `x`, we check for `x+1`, `x+2`, etc.,
# we'd still be doing redundant work. For a sequence `[1,2,3,4]`, we would start a count from 1, then
# from 2, then from 3, etc.
#
# The crucial optimization is: **Only start counting a sequence if we are at its true beginning.**
# A number `num` is the start of a sequence if and only if `num - 1` is NOT in the hash set.
# By adding this single check, we ensure that the inner `while` loop (which counts the sequence length)
# runs only once for each distinct consecutive sequence, not for every element within it.

# --- ALGORITHM ---
# 1. Create a hash set and add all elements from the input array to it. This takes O(N) time and handles duplicates automatically.
# 2. Initialize `longest = 0`.
# 3. Iterate through each `num` in the hash set.
# 4. **The key step:** Check if `num - 1` is **not** in the hash set.
#    - If this condition is true, it means `num` is the starting point of a new sequence.
# 5. If `num` is a starting point, initialize `current_count = 1` and `current_num = num`.
# 6. Use a `while` loop to check if `current_num + 1` is in the hash set. This check is now O(1).
#    - If it is, increment `current_num` and `current_count`.
# 7. After the `while` loop finishes, the sequence has ended. Update `longest = max(longest, current_count)`.
# 8. Return `longest`.

def longestSubsequenceOp(arr: list[int]) -> int:
    if not arr: return 0
    # Step 1: Put all elements into a hash set for O(1) lookups.
    hash_set = set(arr)
    longest = 0

    # Step 2: Iterate through the unique numbers.
    for num in hash_set:
        # Step 3: THE CRUCIAL CHECK. Only start counting if 'num' is the start of a sequence.
        if num - 1 not in hash_set:
            count = 1
            x = num
            # Step 4: Count the length of the sequence starting from 'num'.
            # Each lookup (x + 1 in hash_set) is O(1).
            while x + 1 in hash_set:
                x += 1
                count += 1
            longest = max(longest, count) 

    return longest

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why?
# 1. Building the set takes O(N).
# 2. We iterate through the N unique elements in the set. The `if` condition is O(1).
# 3. The inner `while` loop seems tricky, but each number in the set is visited by the `while` loop
#    at most once over the entire execution of the function. This means the two nested loops together
#    result in a linear number of operations, not quadratic. Thus, the total time is O(N) + O(N) = O(N).
# This is better than the O(N log N) sorting solution because hash set operations are, on average, O(1).
#
# Space Complexity: O(N)
# Why? We store all unique elements of the input array in the `hash_set`. In the worst case,
# all elements are unique, requiring O(N) space.
#
# --- HOW TO REMEMBER ---
# Optimal = "Hash Set + Smart Start". Use a hash set for O(1) lookups. The "smart start" trick
# (`if num - 1 not in set`) is the key to avoiding redundant work and achieving O(N) time.

arr = [102,4,100,1,101,2,3,1,1]
print(f"Optimal Result: {longestSubsequenceOp(arr)}") # Expected: 4