# Problem:
# Given two sorted arrays, arr1 of size n and arr2 of size m, the task is to merge them into a single sorted array.
# The final sorted array should be stored in-place, meaning the first n elements should be in arr1
# and the remaining m elements should be in arr2. This version of the solution is allowed to use extra space.

# Observation/Intuition:
# The most straightforward way to solve this is to use a third array to store the merged result.
# We can use a standard two-pointer approach to iterate through both arrays. A 'left' pointer for arr1
# and a 'right' pointer for arr2 are used. We compare the elements at arr1[left] and arr2[right]
# and append the smaller of the two to our temporary array (arr3). The corresponding pointer is then incremented.
# This process continues until one of the arrays is fully traversed. After that, we append the
# remaining elements from the other array to arr3.
# Finally, the sorted elements from arr3 are copied back into arr1 and arr2 to satisfy the problem's in-place requirement.

# Time Complexity: O(n + m)
# The first three while loops run in O(n + m) time to fill arr3.
# The final two for loops also run in O(n + m) time to copy the elements back.
# The total time complexity is O(n + m) + O(n + m) = O(n + m).

# Space Complexity: O(n + m)
# We use an auxiliary array 'arr3' of size n + m to store the merged elements.
from typing import List
import math

def mergeTwoSortedArrayBrute(arr1: List[int], arr2: List[int]):
    n = len(arr1)
    m = len(arr2)

    arr3 = []
    left = 0
    right = 0

    # Two-pointer traversal to merge into a temporary array
    while left < n and right < m:
        left_el = arr1[left]
        right_el = arr2[right]
        if left_el < right_el:
            arr3.append(left_el)
            left += 1
        else:
            arr3.append(right_el)
            right += 1
    
    # Append remaining elements from arr1, if any
    while left < n:
        left_el = arr1[left]
        arr3.append(left_el)
        left += 1
    
    # Append remaining elements from arr2, if any
    while right < m:
        right_el = arr2[right]
        arr3.append(right_el)
        right += 1

    j = 0
    # Copy the first n elements from the temporary array back to arr1
    for i in range(n):
        arr1[i] = arr3[j]
        j += 1

    # Copy the remaining m elements from the temporary array to arr2
    for i in range(m):
        arr2[i] = arr3[j]
        j += 1

    return {
        "arr1": arr1,
        "arr2": arr2
    } 

arr1_brute = [1,3,5,7]
arr2_brute = [0,2,6,8,9]

print("Brute-force approach:")
print(mergeTwoSortedArrayBrute(arr1_brute, arr2_brute))
print("-" * 20)


# Problem:
# Merge two sorted arrays without using any extra space (i.e., with O(1) space complexity).

# Optimal Approach 1:
# Intuition:
# The final merged arrangement requires the first array (arr1) to contain the n smallest elements
# and the second array (arr2) to contain the m largest elements.
# We can observe that the largest elements of arr1 might need to be swapped with the smallest elements of arr2.
# This approach starts by comparing the last element of arr1 with the first element of arr2.
# If arr1[left] > arr2[right] (where 'left' starts at n-1 and 'right' starts at 0),
# it means the element from arr1 belongs in arr2 and vice versa. So, we swap them.
# We continue this process by moving the 'left' pointer backwards and the 'right' pointer forwards,
# swapping whenever an element in arr1 is greater than an element in arr2.
# Once this loop finishes (when left < 0 or right >= m, or when arr1[left] <= arr2[right]),
# we have successfully moved all the n smallest elements into the arr1 "space" and the m largest
# into the arr2 "space", but the arrays themselves are not internally sorted.
# The final step is to sort both arr1 and arr2 independently to get the final result.

# Time Complexity: O(min(n, m)) + O(n*log(n)) + O(m*log(m))
# The initial while loop runs at most min(n, m) times.
# The dominant part is sorting the two arrays, which takes O(n*log(n)) and O(m*log(m)) respectively.

# Space Complexity: O(1)
# All operations are performed in-place, without using any extra data structures.
def mergeTwoSortedArrOp(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    left = n - 1
    right = 0

    # Swap elements to partition smaller elements into arr1 and larger into arr2
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            # If arr1's element is smaller, the arrays are correctly partitioned at this point
            break

    # Sort both arrays to get the final result
    arr1.sort()
    arr2.sort()
    
    return {
        "arr1": arr1,
        "arr2": arr2
    }

arr1_op1 = [1,3,5,7]
arr2_op1 = [0,2,6,8,9]

print("Optimal approach 1:")
print(mergeTwoSortedArrOp(arr1_op1, arr2_op1))
print("-" * 20)


# Optimal Approach 2 (Gap Method):
# Intuition:
# This method is derived from the Shell Sort algorithm. It works by treating the two arrays as
# a single, contiguous array of length (n + m).
# The core idea is to compare and swap elements that are a certain `gap` distance apart.
# We start with a large `gap` (initially ceil((n+m)/2)) and iterate through the conceptual
# combined array, comparing element `i` with element `i + gap` and swapping if they are in the wrong order.
# After one pass, we reduce the gap (gap = ceil(gap / 2)). This process is repeated
# until the gap becomes 1.
# The decreasing gap helps in moving elements to their correct positions over longer distances initially
# and then fine-tuning their positions as the gap shrinks.
# The comparisons and swaps can happen in three scenarios:
# 1. Both elements are in arr1.
# 2. The first element is in arr1 and the second is in arr2.
# 3. Both elements are in arr2.
# The logic correctly handles these three cases to simulate operations on a single array.
# By the time the algorithm finishes with a gap of 1, the two arrays are fully sorted.

# Time Complexity: O((n+m) * log(n+m))
# The outer while loop runs log2(n+m) times as the gap is repeatedly halved.
# The inner while loop runs O(n+m) times for each gap.

# Space Complexity: O(1)
# All swaps are performed in-place.
def swapIfGreater(arr1, arr2, i, j):
    """Helper function to swap elements if arr1[i] > arr2[j]"""
    if arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]

def mergeTwoSortedArrOp2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    Tlen = n + m
    
    # Initialize gap to half of the total length
    gap = math.ceil(Tlen / 2)
    
    while gap > 0:
        left = 0
        right = left + gap

        while right < Tlen:
            # Case 1: left pointer is in arr1, right pointer is in arr2
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # Case 2: Both pointers are in arr2
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # Case 3: Both pointers are in arr1
            else:
                swapIfGreater(arr1, arr1, left, right)
            
            left += 1
            right += 1
        
        # Break the loop if the gap becomes 1, as the next gap will be 0
        if gap == 1:
            break
        
        # Reduce the gap
        gap = math.ceil(gap / 2)

    return {
        "arr1": arr1,
        "arr2": arr2
    }

arr1_op2 = [1,3,5,7]
arr2_op2 = [0,2,6,8,9]

print("Optimal approach 2 (Gap Method):")
print(mergeTwoSortedArrOp2(arr1_op2, arr2_op2))
print("-" * 20)