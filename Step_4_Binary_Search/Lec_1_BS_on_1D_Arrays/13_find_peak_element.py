#!/usr/bin/env python3
"""
DSA Problem Solution Template
============================

Problem: Find a peak element in an array. A peak element is an element that is not smaller than its neighbors. For an element arr[i], it is a peak if arr[i-1] <= arr[i] >= arr[i+1]. For the first element, it is a peak if arr[0] >= arr[1]. For the last element, it is a peak if arr[n-1] >= arr[n-2].
Platform: GeeksforGeeks, LeetCode
Difficulty: Medium
Topics: Array, Binary Search
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A list of integers `arr`.
- Output: The index of any peak element.
- Constraints: The array can have one or more elements. The elements can be positive, negative, or zero.
- Edge Cases: 
    - Array with a single element.
    - Peak element at the beginning or end of the array.
    - Array with multiple peaks.
    - Strictly increasing or decreasing arrays.

APPROACH (Optimal - Binary Search):
1. Handle edge cases first: If the array has one element, return index 0. If the first element is a peak, return 0. If the last element is a peak, return n-1.
2. Initialize `low = 1` and `high = n - 2`. We've already checked the boundaries.
3. Loop while `low <= high`:
    a. Calculate `mid = low + (high - low) // 2`.
    b. If `arr[mid]` is greater than its left and right neighbors, we've found a peak, return `mid`.
    c. If `arr[mid]` is on an "increasing curve" (i.e., `arr[mid] < arr[mid + 1]`), it means a peak must exist on the right side. So, we eliminate the left half by setting `low = mid + 1`.
    d. If `arr[mid]` is on a "decreasing curve" (i.e., `arr[mid] > arr[mid + 1]`), it means the peak could be `mid` or on the left side. So, we eliminate the right half by setting `high = mid - 1`.
    e. If there are duplicates and `arr[mid]` is in a valley, we can move to either side. Here, we move to the right.

TIME COMPLEXITY: O(log n) for the optimal solution. O(n) for the brute-force.
SPACE COMPLEXITY: O(1) for both solutions.
"""

# ==============================================================================
# SOLUTION
# ==============================================================================

def findPeakElOp(arr):
    """
    Main solution function using the optimal binary search approach.
    
    Args:
        arr: A list of integers.
    
    Returns:
        The index of a peak element. Returns -1 if no peak is found (though a peak always exists in a non-empty array as per the problem's usual definition).
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    n = len(arr)

    # STEP 1: Edge case handling
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    # STEP 2: Initialize pointers for binary search
    # NOTE: We search in the range [1, n-2] because we've already checked the boundaries.
    low = 1
    high = n - 2

    # STEP 3: Main algorithm logic (Binary Search)
    while low <= high:
        mid = low + (high - low) // 2

        # Check if mid is a peak
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        
        # If we are on the increasing curve, a peak is on the right
        elif arr[mid] > arr[mid - 1]:
            low = mid + 1
            
        # If we are on the decreasing curve, a peak is on the left
        # This also handles the case where arr[mid] < arr[mid-1]
        else: # This includes arr[mid] < arr[mid-1] or arr[mid] == arr[mid-1]
            high = mid - 1

    return -1 # Should not be reached in a valid problem instance

# ==============================================================================
# ALTERNATIVE SOLUTIONS
# ==============================================================================

def findPeakElBrute(arr):
    """
    Brute force approach - easier to understand but less efficient.
    Iterates through the array to find a peak.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Check if arr[i] is a peak
        is_left_smaller = (i == 0) or (arr[i - 1] < arr[i])
        is_right_smaller = (i == n - 1) or (arr[i + 1] < arr[i])
        
        if is_left_smaller and is_right_smaller:
            return i
    return -1 # Should not be reached

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

# No helper functions needed for this specific problem.

# ==============================================================================
# TEST CASES
# ==============================================================================

def test_solution():
    """
    Test cases to verify the solution works correctly.
    """
    
    # TEST CASE 1: Peak in the middle
    input1 = [1, 2, 3, 4, 5, 6, 8, 5, 1]
    # Valid peaks are at index 6 (value 8)
    result1 = findPeakElOp(input1)
    assert result1 == 6, f"Test 1 failed: expected 6, got {result1}"
    print("✓ Test 1 passed")
    
    # TEST CASE 2: Peak at the beginning
    input2 = [5, 4, 3, 2, 1]
    result2 = findPeakElOp(input2)
    assert result2 == 0, f"Test 2 failed: expected 0, got {result2}"
    print("✓ Test 2 passed")

    # TEST CASE 3: Peak at the end
    input3 = [1, 2, 3, 4, 5]
    result3 = findPeakElOp(input3)
    assert result3 == 4, f"Test 3 failed: expected 4, got {result3}"
    print("✓ Test 3 passed")

    # TEST CASE 4: Single element
    input4 = [42]
    result4 = findPeakElOp(input4)
    assert result4 == 0, f"Test 4 failed: expected 0, got {result4}"
    print("✓ Test 4 passed")

    # TEST CASE 5: Array with two elements, peak at start
    input5 = [2, 1]
    result5 = findPeakElOp(input5)
    assert result5 == 0, f"Test 5 failed: expected 0, got {result5}"
    print("✓ Test 5 passed")

    # TEST CASE 6: Array with two elements, peak at end
    input6 = [1, 2]
    result6 = findPeakElOp(input6)
    assert result6 == 1, f"Test 6 failed: expected 1, got {result6}"
    print("✓ Test 6 passed")

    # TEST CASE 7: Brute force check
    brute_result = findPeakElBrute(input1)
    assert brute_result == 6, f"Test 7 (Brute) failed: expected 6, got {brute_result}"
    print("✓ Test 7 (Brute) passed")

    print("All tests passed! ✨")

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS (Optimal Solution):

TIME COMPLEXITY:
- Best Case: O(1) - When the peak is at the start or end of the array.
- Average Case: O(log n) - Standard binary search performance.
- Worst Case: O(log n) - When the search space is halved at each step until the element is found.
- Explanation: The binary search algorithm divides the search space in half with each iteration. This logarithmic behavior is highly efficient for large datasets.

SPACE COMPLEXITY:
- O(1) 
- Explanation: The solution uses a few variables (low, high, mid, n) to keep track of indices. The space required does not scale with the size of the input array.

TRADE-OFFS:
- The binary search approach is significantly faster (O(log n)) than the linear scan (O(n)) for large arrays.
- The brute-force method is simpler to write and understand but is inefficient. For competitive programming or performance-critical applications, the binary search is always preferred.
"""

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Run tests
    test_solution()
    
    # Example usage with the optimal function
    sample_input = [1, 2, 1, 3, 5, 6, 4]
    peak_index = findPeakElOp(sample_input)
    print(f"Sample Input: {sample_input}")
    print(f"A peak element is at index: {peak_index}, value: {sample_input[peak_index]}")
    
    # Example usage with the brute force function
    peak_index_brute = findPeakElBrute(sample_input)
    print(f"Brute force found a peak at index: {peak_index_brute}, value: {sample_input[peak_index_brute]}")