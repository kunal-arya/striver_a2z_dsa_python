from typing import List

# Optimal Approach

# Observation: If intervals are sorted by their start times, overlapping intervals will be adjacent or very close.
# Intuition: Sorting allows us to process intervals sequentially and easily check for overlaps with the last merged interval.
# We maintain a 'current' merged interval. For each subsequent interval:
# - If it overlaps with the 'current' merged interval, we extend the 'current' merged interval's end.
# - If it does not overlap, the 'current' merged interval is complete, so we add it to our result list
#   and start a new 'current' merged interval with the non-overlapping interval.

def mergeOverlappingSubOp(arr: List[List[int]]) -> List[List[int]]:
    n = len(arr)
    res = []

    # Step 1: Sort the intervals based on their start times.
    # This is crucial because it ensures that when we iterate, we're always looking
    # at the "next" potential interval that could merge with the current one.
    arr.sort()

    # Initialize the 'current' merged interval with the first interval from the sorted list.
    start_sub = arr[0][0]
    end_sub = arr[0][1] # Correction: Initialize end_sub with the end of the first interval.

    # Iterate through the rest of the intervals, starting from the second one.
    for i in range(1,n):
        # Check for overlap: If the end of the current merged interval is greater than or equal to
        # the start of the next interval, they overlap.
        if end_sub >= arr[i][0]:
            # If they overlap, extend the end of the current merged interval to the maximum
            # of its current end and the end of the next interval.
            end_sub = max(end_sub, arr[i][1])
        else:
            # If no overlap, the current merged interval is complete. Add it to the result list.
            res.append([start_sub,end_sub])
            # Start a new 'current' merged interval with the current non-overlapping interval.
            start_sub = arr[i][0]
            end_sub = arr[i][1]
    
    # After the loop finishes, the last merged interval (or the only interval if there was only one)
    # will still be in 'start_sub' and 'end_sub'. Add it to the result.
    res.append([start_sub,end_sub])
        
    return res


arr = [[1,3],[2,4],[2,6],[8,9],[9,10],[9,11], [15,18], [16,17]]

print(mergeOverlappingSubOp(arr))