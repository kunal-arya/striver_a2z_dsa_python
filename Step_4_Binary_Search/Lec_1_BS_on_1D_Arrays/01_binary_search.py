"""
Binary Search - Complete Solution with Documentation
Problem Source: Classic DSA Problem / LeetCode #704
"""

from typing import List

# ==================== PROBLEM STATEMENT ====================
"""
Problem: Find the index of a target element in a sorted array.
Given a sorted array of integers and a target value, return the index of the target if found, otherwise return -1.
"""

# ==================== OBSERVATIONS ====================
"""
Key Constraints & Edge Cases:
1. Array is sorted in ascending order (crucial for binary search)
2. All elements are unique (typical assumption)
3. Array can be empty (return -1)
4. Target may not exist in array (return -1)
5. Array size can be 1 (single element case)
6. Target can be smaller than arr[0] or larger than arr[n-1]

Patterns Noticed:
- Sorted array allows elimination of half the search space at each step
- Middle element comparison determines which half to search next
- Search space reduces logarithmically: n → n/2 → n/4 → n/8 → ... → 1
"""

# ==================== INTUITION ====================
"""
Key Insight:
In a sorted array, we can eliminate half the search space by comparing with the middle element.
- If target == middle: Found the answer
- If target < middle: Target must be in the left half (if it exists)
- If target > middle: Target must be in the right half (if it exists)

This "divide and conquer" approach reduces time complexity from O(n) to O(log n).
"""

# ==================== DRY RUN ====================
"""
Example: arr = [1,2,4,6,8,13,16,19], target = 6

Iteration 1:
low=0, high=7, mid=(0+7)//2=3
arr[3]=6, target=6 → arr[mid] == target → return 3

Alternative example: arr = [1,2,4,6,8,13,16,19], target = 13

Iteration 1:
low=0, high=7, mid=3, arr[3]=6
target=13 > arr[3]=6 → search right half
low=4, high=7

Iteration 2:
low=4, high=7, mid=(4+7)//2=5
arr[5]=13, target=13 → arr[mid] == target → return 5
"""

# ==================== APPROACH ====================
"""
Algorithm: Binary Search (Divide and Conquer)
1. Initialize two pointers: low=0, high=n-1
2. While low <= high:
   - Calculate middle index: mid = (low + high) // 2
   - If arr[mid] == target: return mid
   - If arr[mid] > target: search left half (high = mid - 1)
   - If arr[mid] < target: search right half (low = mid + 1)
3. If loop ends without finding target: return -1

Recursive variant follows the same logic but uses function calls instead of loops.
"""

# ==================== TIME & SPACE COMPLEXITY ====================
"""
Iterative Binary Search:
- Time Complexity: O(log n) - Search space halves each iteration
- Space Complexity: O(1) - Only using constant extra variables

Recursive Binary Search:
- Time Complexity: O(log n) - Same logic as iterative
- Space Complexity: O(log n) - Due to recursion call stack

Linear Search (for comparison):
- Time Complexity: O(n) - May need to check every element
- Space Complexity: O(1) - Only using constant extra variables

Binary Search is significantly faster for large arrays!
"""

# ==================== SOLUTION IMPLEMENTATIONS ====================

def findElementLinear(arr: List[int], target: int) -> int:
    """
    Linear Search - O(n) time complexity
    Check each element sequentially until target is found
    """
    n = len(arr)
    
    # Check each element one by one
    for i in range(n):
        if arr[i] == target:
            return i                       # Target found at index i
    
    return -1                              # Target not found


def findElementBinaryIterative(arr: List[int], target: int) -> int:
    """
    Binary Search - Iterative Implementation - O(log n) time, O(1) space
    Most efficient and commonly used implementation
    """
    n = len(arr)
    low = 0                                # Left boundary of search space
    high = n - 1                          # Right boundary of search space
    
    # Continue while search space is valid
    while low <= high:
        # Calculate middle index (avoids integer overflow)
        mid = (low + high) // 2

        # OVERFLOW CASE: if low and high both are INT_MAX
        # then if u try to add INT_MAX + INT_MAX, it's an overflow case
        # DO THIS:
        # mid = low + (high - low) // 2 ( Or u can use this to find mid everytime so that it doesn't overflow )

        
        # Check if middle element is our target
        if arr[mid] == target:
            return mid                     # Target found at index mid
        
        # Target is in left half, narrow search space
        elif arr[mid] > target:
            high = mid - 1                 # Eliminate right half
        
        # Target is in right half, narrow search space
        else:
            low = mid + 1                  # Eliminate left half
    
    return -1                              # Target not found


def findElementBinaryRecursive(arr: List[int], target: int) -> int:
    """
    Binary Search - Recursive Implementation - O(log n) time, O(log n) space
    Good for understanding recursion, but iterative is preferred in practice
    """
    n = len(arr)
    return binarySearchRecursive(arr, 0, n - 1, target)


def binarySearchRecursive(arr: List[int], low: int, high: int, target: int) -> int:
    """
    Helper function for recursive binary search
    """
    # Base case: search space is invalid
    if low > high:
        return -1                          # Target not found
    
    # Calculate middle index
    mid = (low + high) // 2
    
    # Target found at middle
    if arr[mid] == target:
        return mid
    
    # Search in right half
    elif target > arr[mid]:
        return binarySearchRecursive(arr, mid + 1, high, target)
    
    # Search in left half
    else:
        return binarySearchRecursive(arr, low, mid - 1, target)


# ==================== EDGE CASE HANDLERS ====================

def findElementBinaryRobust(arr: List[int], target: int) -> int:
    """
    Binary Search with comprehensive edge case handling
    """
    # Handle empty array
    if not arr:
        return -1
    
    n = len(arr)
    
    # Handle single element array
    if n == 1:
        return 0 if arr[0] == target else -1
    
    # Quick boundary checks (optional optimization)
    if target < arr[0] or target > arr[n-1]:
        return -1
    
    # Standard binary search
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


# ==================== TEST CASES ====================
def test_all_implementations():
    """Test all implementations with various cases"""
    
    test_cases = [
        ([1, 2, 4, 6, 8, 13, 16, 19], 6, 3),      # Normal case
        ([1, 2, 4, 6, 8, 13, 16, 19], 13, 5),     # Target in right half
        ([1, 2, 4, 6, 8, 13, 16, 19], 1, 0),      # Target at start
        ([1, 2, 4, 6, 8, 13, 16, 19], 19, 7),     # Target at end
        ([1, 2, 4, 6, 8, 13, 16, 19], 10, -1),    # Target not found
        ([5], 5, 0),                               # Single element found
        ([5], 3, -1),                              # Single element not found
        ([], 5, -1),                               # Empty array
        ([1, 3, 5, 7, 9], 0, -1),                 # Target smaller than all
        ([1, 3, 5, 7, 9], 10, -1),                # Target larger than all
    ]
    
    functions = [
        ("Linear Search", findElementLinear),
        ("Binary Iterative", findElementBinaryIterative),
        ("Binary Recursive", findElementBinaryRecursive),
        ("Binary Robust", findElementBinaryRobust),
    ]
    
    for arr, target, expected in test_cases:
        print(f"Array: {arr}, Target: {target}, Expected: {expected}")
        
        results_match = True
        for name, func in functions:
            result = func(arr, target)
            match = result == expected
            print(f"  {name}: {result} {'✓' if match else '✗'}")
            if not match:
                results_match = False
        
        print(f"  All implementations match: {'✓' if results_match else '✗'}")
        print("-" * 60)


# ==================== PERFORMANCE COMPARISON ====================
def performance_demo():
    """Demonstrate performance difference between linear and binary search"""
    import time
    
    # Create large sorted array
    large_arr = list(range(1, 1000001, 2))  # [1, 3, 5, 7, ..., 999999]
    target = 500001
    
    # Test linear search
    start_time = time.time()
    linear_result = findElementLinear(large_arr, target)
    linear_time = time.time() - start_time
    
    # Test binary search
    start_time = time.time()
    binary_result = findElementBinaryIterative(large_arr, target)
    binary_time = time.time() - start_time
    
    print(f"Array size: {len(large_arr):,}")
    print(f"Target: {target}")
    print(f"Linear Search: {linear_result} (Time: {linear_time:.6f}s)")
    print(f"Binary Search: {binary_result} (Time: {binary_time:.6f}s)")
    print(f"Binary search is {linear_time/binary_time:.1f}x faster!")


# ==================== FOLLOW-UPS ====================
"""
Potential Follow-up Questions:

1. **What if array contains duplicates?**
   - Find first occurrence: modify to continue searching left when found
   - Find last occurrence: modify to continue searching right when found
   - Find any occurrence: current solution works fine

2. **What if we need to find insertion point for target?**
   - Return the `low` index when target is not found
   - This gives the position where target should be inserted

3. **Can we handle rotated sorted arrays?**
   - Yes, but requires modification to handle the rotation point
   - Check which half is sorted before deciding direction

4. **What about searching in infinite/very large arrays?**
   - First find bounds using exponential search
   - Then apply binary search within those bounds

5. **Memory optimization for very large arrays?**
   - External sorting and binary search on disk
   - Use memory-mapped files for large datasets

6. **What if array is sorted in descending order?**
   - Modify comparison logic: if arr[mid] > target, search right half
   - Or reverse the array first (but this adds O(n) time)

7. **Handle floating point precision issues?**
   - Use epsilon-based comparison instead of exact equality
   - Define tolerance level for "close enough" matches

8. **Thread safety for concurrent searches?**
   - Binary search is naturally thread-safe for read operations
   - No shared state modification during search

9. **Can we optimize for repeated searches?**
   - Consider data structures like balanced BST or hash tables
   - Trade-off between search time and space complexity
"""

# ==================== BINARY SEARCH VARIANTS ====================

def findFirstOccurrence(arr: List[int], target: int) -> int:
    """Find the first occurrence of target in array with duplicates"""
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            result = mid                   # Store potential answer
            high = mid - 1                 # Continue searching left
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return result


def findInsertionPoint(arr: List[int], target: int) -> int:
    """Find the index where target should be inserted to maintain sorted order"""
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return low  # This is the insertion point


# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 4, 6, 8, 13, 16, 19]
    target = 6
    
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Linear Search Result: {findElementLinear(arr, target)}")
    print(f"Binary Search Result: {findElementBinaryIterative(arr, target)}")
    print(f"Recursive Binary Search Result: {findElementBinaryRecursive(arr, target)}")
    
    # Run comprehensive tests
    print("\n" + "="*60)
    print("RUNNING COMPREHENSIVE TESTS")
    print("="*60)
    test_all_implementations()
    
    # Performance demonstration
    print("\n" + "="*60)
    print("PERFORMANCE COMPARISON")
    print("="*60)
    performance_demo()