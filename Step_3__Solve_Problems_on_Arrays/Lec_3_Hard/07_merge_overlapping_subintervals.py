from typing import List

# PROBLEM STATEMENT:
# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Brute Approach

# Observation: The given problem statement refers to "Merge Sorted Array" (LeetCode 88), but the provided code
# (mergeIntervalsBrute and mergeIntervalsOp) is for "Merge Overlapping Intervals" (LeetCode 56).
# The comments and logic provided are relevant to the "Merge Overlapping Intervals" problem.
# For the "Merge Sorted Array" problem, a brute force approach would involve copying elements and then sorting.
# Intuition for Merge Sorted Array (Brute Force):
# 1. Copy all elements of nums2 into the available zeroed-out space in nums1.
# 2. Sort the entire nums1 array.

def mergeIntervalsBrute(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr)
    res = []
    # Step 1: Sort the intervals based on their start times.
    # This is a common and necessary step for interval problems to efficiently identify overlaps.
    arr.sort()

    # Iterate through each interval.
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        # Optimization/Observation: If the current interval's end 
        # is already covered by the last merged interval in 'res',
        # then this interval has already been processed as part of a previous merge.
        # This check helps avoid redundant processing and duplicate entries in 'res'.
        if (len(res) > 0 and end <= res[-1][1]):
            continue

        # For the current interval, try to merge it with subsequent intervals.
        # This inner loop extends the 'end' of the current interval as 
        # long as overlaps are found.
        for j in range(i + 1,n):
            # If the current interval's 'end' overlaps with the 
            # start of the next interval (arr[j][0]),
            # extend the 'end' to include the maximum of the
            # current 'end' and the end of arr[j].
            if arr[j][0] <= end:
                end = max(arr[j][1],end)
            else:
                # If no overlap, then arr[j] and subsequent intervals 
                # will not overlap with the current merged interval.
                # So, we can break from the inner loop.
                break
        
        # After checking all possible merges for the current 'start', 
        # add the merged interval to the result.
        res.append([start,end])

    return res


arr = [[1,3],[2,4],[2,6],[8,9],[9,10],[9,11], [15,18], [16,17]]

print(mergeIntervalsBrute(arr))

# Optimal Approach

# Observation: If intervals are sorted by their start times, overlapping intervals will be adjacent or very close.
# Intuition: Sorting allows us to process intervals sequentially and easily check for overlaps with the last merged interval.
# We maintain a 'current' merged interval. For each subsequent interval:
# - If it overlaps with the 'current' merged interval, we extend the 'current' merged interval's end.
# - If it does not overlap, the 'current' merged interval is complete, so we add it to our result list
#   and start a new 'current' merged interval with the non-overlapping interval.

def mergeIntervalsOp(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr)
    res = []
    arr.sort()

    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        if len(res) == 0 or start > res[-1][1]:
            res.append([start,end])
        else:
            res[-1][1] = max(end, res[-1][1])

        
    return res


arr = [[1,3],[2,4],[2,6],[8,9],[9,10],[9,11], [15,18], [16,17]]

print(mergeIntervalsOp(arr))