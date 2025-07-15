# =============================================================================
# PROBLEM STATEMENT: Count Inversions in Array
# =============================================================================
# Given an array of integers, count the number of inversions.
# An inversion is a pair (i, j) where i < j but arr[i] > arr[j]
# 
# Example: [5,3,2,4,1] has inversions:
# (0,1): 5>3, (0,2): 5>2, (0,3): 5>4, (0,4): 5>1
# (1,2): 3>2, (1,4): 3>1, (2,4): 2>1, (3,4): 4>1
# Total: 8 inversions
#
# INTUITION: Count how many smaller elements appear after each element
# REAL-WORLD USE: Measure how far an array is from being sorted

from typing import List

# =============================================================================
# APPROACH 1: BRUTE FORCE - O(n²) TIME, O(1) SPACE
# =============================================================================
# INTUITION: Check every pair (i,j) where i < j
# OBSERVATION: If arr[i] > arr[j] and i < j, it's an inversion
# MEMORY TIP: Simple nested loops - outer for each element, inner for elements after it

def countInversion(arr: List[int]):
    n = len(arr)
    count = 0
    
    # For each element, check all elements that come after it
    for i in range(n):
        for j in range(i + 1, n):  # j starts from i+1 to ensure i < j
            if arr[i] > arr[j]:     # Inversion condition
                count += 1
    
    return count

# VISUAL DRY RUN: arr = [5,3,2,4,1]
# i=0 (5): Compare with j=1(3)✓, j=2(2)✓, j=3(4)✓, j=4(1)✓ → 4 inversions
# i=1 (3): Compare with j=2(2)✓, j=3(4)✗, j=4(1)✓ → 2 inversions  
# i=2 (2): Compare with j=3(4)✗, j=4(1)✓ → 1 inversion
# i=3 (4): Compare with j=4(1)✓ → 1 inversion
# Total: 4 + 2 + 1 + 1 = 8 inversions

arr = [5,3,2,4,1]
print(countInversion(arr))

# =============================================================================
# APPROACH 2: MERGE SORT OPTIMIZATION - O(n log n) TIME, O(n) SPACE
# =============================================================================
# KEY INSIGHT: During merge, when arr[left] > arr[right], ALL elements from 
# left to mid are greater than arr[right] (since left half is sorted)
# This gives us (mid - left + 1) inversions in one comparison!

# Tell to Interviewer that I am altering the data, If u want me not to alter it
# I will create copy of the array.

def merge(arr, start, mid, end):
    """
    Merge two sorted halves and count cross-inversions
    
    VISUALIZATION of merge process:
    Left half: [3,5] (sorted)    Right half: [1,2,4] (sorted)
    
    When 3 > 1: Both 3 and 5 are > 1, so count += 2
    When 3 > 2: Both 3 and 5 are > 2, so count += 2  
    When 5 > 4: Only 5 is > 4, so count += 1
    
    Total cross-inversions: 2 + 2 + 1 = 5
    """
    count = 0               # LOCAL variable to track inversions in this merge
    temp = []               # Temporary array to store merged result
    left = start            # Pointer for left half [start...mid]
    right = mid + 1         # Pointer for right half [mid+1...end]
    
    # Main merge logic with inversion counting
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            # No inversion: left element is smaller/equal
            temp.append(arr[left])
            left += 1
        else:
            # INVERSION FOUND! arr[left] > arr[right]
            # CRITICAL INSIGHT: Since left half is sorted,
            # ALL elements from current 'left' to 'mid' are > arr[right]
            # So we get (mid - left + 1) inversions at once!
            temp.append(arr[right])
            count += (mid - left + 1)  # Count multiple inversions
            right += 1
    
    # Copy remaining elements from left half (if any)
    while left <= mid:
        temp.append(arr[left])
        left += 1
        
    # Copy remaining elements from right half (if any)
    while right <= end:
        temp.append(arr[right])
        right += 1
        
    # Copy merged result back to original array
    for i in range(start, end + 1):
        arr[i] = temp[i - start]
    
    return count  # Return the count of inversions found in this merge

def mergeSort(arr, start, end) -> int:
    """
    Recursive merge sort that counts inversions
    
    ALGORITHM FLOW:
    1. Divide array into two halves
    2. Recursively count inversions in left half
    3. Recursively count inversions in right half  
    4. Count cross-inversions while merging
    5. Return total count (left + right + cross)
    """
    if start >= end:
        return 0  # Base case: single element or empty has 0 inversions
    
    mid = (start + end) // 2
    
    # Recursively sort and count inversions in both halves
    left_count = mergeSort(arr, start, mid)          # Left half inversions
    right_count = mergeSort(arr, mid + 1, end)       # Right half inversions
    
    # Count cross-inversions between left and right halves
    cross_count = merge(arr, start, mid, end)

    # Return total inversions: left + right + cross
    return left_count + right_count + cross_count

def inversionCount(arr):
    """
    Main function to count inversions using merge sort approach
    """
    return mergeSort(arr, 0, len(arr) - 1)

# =============================================================================
# DETAILED STEP-BY-STEP EXECUTION: arr = [5,3,2,4,1]
# =============================================================================
# STEP 1: Initial call mergeSort([5,3,2,4,1], 0, 4)
# mid = 2, so divide into [5,3,2] and [4,1]
#
# STEP 2: mergeSort([5,3,2], 0, 2)  
# mid = 1, divide into [5,3] and [2]
#
# STEP 3: mergeSort([5,3], 0, 1)
# mid = 0, divide into [5] and [3]
# merge([5], [3]) → 5 > 3, count = 1, result: [3,5]
# Returns: 0 + 0 + 1 = 1
#
# STEP 4: Back to mergeSort([5,3,2], 0, 2)
# merge([3,5], [2]) → 3 > 2, count = 2 (both 3,5 > 2), result: [2,3,5]
# Returns: 1 + 0 + 2 = 3
#
# STEP 5: mergeSort([4,1], 3, 4)
# merge([4], [1]) → 4 > 1, count = 1, result: [1,4]  
# Returns: 0 + 0 + 1 = 1
#
# STEP 6: Final merge([2,3,5], [1,4])
# 2 > 1: count += 3 (all 2,3,5 > 1)
# 3 > 4: false, no inversion
# 5 > 4: count += 1 (only 5 > 4)
# merge returns: 4
# Final result: [1,2,3,4,5], total count = 3 + 1 + 4 = 8

arr = [5,3,2,4,1]
print(inversionCount(arr))

# =============================================================================
# MEMORY HELPERS & KEY INSIGHTS
# =============================================================================
# 1. INVERSION DEFINITION: (i,j) where i < j but arr[i] > arr[j]
#    Think: "How many elements are looking backwards?"
# 
# 2. BRUTE FORCE PATTERN: Nested loops with condition check
#    Outer loop: each element
#    Inner loop: elements after current element
#    Check: if current > future element → inversion
# 
# 3. MERGE SORT MAGIC: The key insight is during merge step
#    When left[i] > right[j], then:
#    - left[i] > right[j] ✓
#    - left[i+1] > right[j] ✓ (since left half is sorted)
#    - left[i+2] > right[j] ✓ (since left half is sorted)
#    - ... all elements from left[i] to left[mid] > right[j]
#    - So we get (mid - left + 1) inversions in one comparison!
# 
# 4. LOCAL VARIABLES APPROACH (IMPROVED):
#    - Each function returns its own count
#    - No need for global variables (cleaner, more functional)
#    - mergeSort returns: left_count + right_count + cross_count
#    - merge returns: count of inversions found during merge
#    - Base case returns: 0 (no inversions in single element)
# 
# 5. ADVANTAGES OF LOCAL APPROACH:
#    - Thread-safe (no shared state)
#    - Easier to test and debug
#    - More functional programming style
#    - No risk of forgetting to reset global counter
#    - Each recursive call is independent
# 
# 6. TIME COMPLEXITY ANALYSIS:
#    - Merge sort: O(n log n) - same time as regular merge sort
#    - Each merge operation: O(n) - linear scan of elements
#    - Total levels: O(log n) - height of recursion tree
#    - Overall: O(n log n)
# 
# 7. SPACE COMPLEXITY:
#    - Temporary arrays in merge: O(n)
#    - Recursion stack: O(log n)
#    - Overall: O(n)
# 
# 8. INTERVIEW TIPS:
#    - Start with brute force explanation
#    - Explain why merge sort works: "count cross-inversions during merge"
#    - Draw small example showing (mid - left + 1) calculation
#    - Mention that this is a classic "divide and conquer" optimization
#    - Emphasize the local variable approach for cleaner code
# 
# 9. EDGE CASES TO CONSIDER:
#    - Already sorted array: 0 inversions
#    - Reverse sorted array: maximum inversions = n*(n-1)/2
#    - Single element: 0 inversions
#    - Duplicate elements: handle with <= in merge condition
# 
# 10. COMMON MISTAKES (FIXED):
#     - ✗ Using global variables (thread-unsafe, harder to debug)
#     - ✓ Using local variables with proper return values
#     - ✗ Using < instead of <= in merge (affects handling of duplicates)
#     - ✗ Wrong inversion count formula (should be mid - left + 1)
#     - ✗ Forgetting to return 0 in base case

# =============================================================================
# VISUAL REPRESENTATION OF MERGE PROCESS
# =============================================================================
# Example: Merging [3,5] and [1,2,4]
# 
# Step 1: Compare 3 and 1
# 3 > 1 → Inversion! 
# Since left half [3,5] is sorted, BOTH 3 and 5 are > 1
# count += (1 - 0 + 1) = 2
# temp = [1], left=0, right=1
# 
# Step 2: Compare 3 and 2  
# 3 > 2 → Inversion!
# Since left half [3,5] is sorted, BOTH 3 and 5 are > 2
# count += (1 - 0 + 1) = 2
# temp = [1,2], left=0, right=2
# 
# Step 3: Compare 3 and 4
# 3 < 4 → No inversion
# temp = [1,2,3], left=1, right=2
# 
# Step 4: Compare 5 and 4
# 5 > 4 → Inversion!
# Only 5 is > 4 (since we already processed 3)
# count += (1 - 1 + 1) = 1
# temp = [1,2,3,4], left=1, right=3
# 
# Step 5: Copy remaining
# temp = [1,2,3,4,5]
# Total inversions in this merge: 2 + 2 + 1 = 5

# =============================================================================
# COMPLEXITY COMPARISON
# =============================================================================
# BRUTE FORCE:
# - Time: O(n²) - nested loops
# - Space: O(1) - only counter variable
# - Best for: small arrays, educational purposes
# 
# MERGE SORT (LOCAL VARIABLES):
# - Time: O(n log n) - divide and conquer
# - Space: O(n) - temporary arrays + recursion stack
# - Best for: large arrays, production code
# - Additional benefits: thread-safe, cleaner code structure
# 
# IMPROVEMENT FACTOR: For n=1000, brute force does ~500,000 comparisons
# while merge sort does ~10,000 comparisons!

# =============================================================================
# RETURN VALUE FLOW EXAMPLE
# =============================================================================
# For arr = [5,3,2,4,1]:
# 
# mergeSort([5,3,2,4,1], 0, 4):
#   ├── mergeSort([5,3,2], 0, 2): returns 3
#   │   ├── mergeSort([5,3], 0, 1): returns 1
#   │   │   ├── mergeSort([5], 0, 0): returns 0
#   │   │   ├── mergeSort([3], 1, 1): returns 0  
#   │   │   └── merge([5], [3]): returns 1
#   │   ├── mergeSort([2], 2, 2): returns 0
#   │   └── merge([3,5], [2]): returns 2
#   ├── mergeSort([4,1], 3, 4): returns 1
#   │   ├── mergeSort([4], 3, 3): returns 0
#   │   ├── mergeSort([1], 4, 4): returns 0
#   │   └── merge([4], [1]): returns 1
#   └── merge([2,3,5], [1,4]): returns 4
# 
# Final result: 3 + 1 + 4 = 8 inversions