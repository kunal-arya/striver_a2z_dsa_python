"""
Lower Bound & Upper Bound - Complete Solution with Documentation

Problem Source: STL equivalent functions / Binary Search variants
"""

from typing import List

# ==================== PROBLEM STATEMENT ====================
"""
Lower Bound: Find the first position where we can insert target such that array remains sorted.
             In other words, find the first element that is >= target.

Upper Bound: Find the position after the last occurrence of target.
             In other words, find the first element that is > target.

Both return the index where target should be inserted to maintain sorted order.
"""

# ==================== LOWER BOUND vs UPPER BOUND EXPLANATION ====================
"""
KEY DIFFERENCES:

Lower Bound (arr[i] >= target):
- Finds the first element that is greater than or equal to target
- If target exists, returns index of first occurrence
- If target doesn't exist, returns insertion point

Upper Bound (arr[i] > target):
- Finds the first element that is strictly greater than target
- If target exists, returns index after last occurrence
- If target doesn't exist, returns insertion point

VISUAL EXAMPLE:
Array: [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
Index:  0  1  2  3  4  5  6   7   8   9

For target = 3:
- Lower Bound = 2 (first occurrence of 3)
- Upper Bound = 4 (first element > 3, which is 5)

For target = 4 (doesn't exist):
- Lower Bound = 4 (first element >= 4, which is 5)
- Upper Bound = 4 (first element > 4, which is 5)

For target = 12 (larger than all):
- Lower Bound = 10 (end of array)
- Upper Bound = 10 (end of array)

PRACTICAL USES:
- Count occurrences: upper_bound - lower_bound
- Range queries in sorted arrays
- Finding insertion points for duplicates
- Implementing binary search variants
"""

# ==================== OBSERVATIONS ====================
"""
Key Constraints & Edge Cases:
1. Array must be sorted (ascending order)
2. Array can contain duplicates
3. Target may or may not exist in array
4. Both functions return valid insertion points (0 to n)
5. When target > all elements, both return n (array length)
6. When target < all elements, both return 0

Patterns Noticed:
- Lower bound uses >= comparison
- Upper bound uses > comparison  
- Both use similar binary search template
- Answer initialization is crucial (default to n)
- Always move towards finding the "first" occurrence of condition
"""

# ==================== INTUITION ====================
"""
Key Insights:

Lower Bound Intuition:
- We want the leftmost position where arr[i] >= target
- When arr[mid] >= target, this could be our answer, but check left for earlier position
- When arr[mid] < target, target must be to the right

Upper Bound Intuition:  
- We want the leftmost position where arr[i] > target
- When arr[mid] > target, this could be our answer, but check left for earlier position
- When arr[mid] <= target, we need to go right to find something > target

Both use "store and search" pattern - store potential answer and keep searching for better one.
"""

# ==================== DRY RUN ====================
"""
LOWER BOUND Example: arr = [1,2,3,3,5,8,8,10,10,11], target = 9

Initial: low=0, high=9, ans=10

Iteration 1:
mid = (0+9)//2 = 4, arr[4]=5
5 >= 9? No → low = 5

Iteration 2:
low=5, high=9, mid=(5+9)//2=7, arr[7]=10
10 >= 9? Yes → ans=7, high=6

Iteration 3:
low=5, high=6, mid=(5+6)//2=5, arr[5]=8
8 >= 9? No → low=6

Iteration 4:
low=6, high=6, mid=6, arr[6]=8
8 >= 9? No → low=7

low > high, return ans=7

UPPER BOUND Example: arr = [1,2,3,3,5,8,8,10,10,11], target = 3

Initial: low=0, high=9, ans=10

Iteration 1:
mid=4, arr[4]=5
5 > 3? Yes → ans=4, high=3

Iteration 2:
low=0, high=3, mid=1, arr[1]=2
2 > 3? No → low=2

Iteration 3:
low=2, high=3, mid=2, arr[2]=3
3 > 3? No → low=3

Iteration 4:
low=3, high=3, mid=3, arr[3]=3
3 > 3? No → low=4

low > high, return ans=4
"""

# ==================== APPROACH ====================
"""
Algorithm: Modified Binary Search with "Store and Search" Pattern

Lower Bound Algorithm:
1. Initialize low=0, high=n-1, ans=n
2. While low <= high:
   - Calculate mid = (low + high) // 2
   - If arr[mid] >= target: store ans=mid, search left (high=mid-1)
   - Else: search right (low=mid+1)
3. Return ans

Upper Bound Algorithm:
1. Initialize low=0, high=n-1, ans=n
2. While low <= high:
   - Calculate mid = (low + high) // 2
   - If arr[mid] > target: store ans=mid, search left (high=mid-1)
   - Else: search right (low=mid+1)
3. Return ans

Key Pattern: When condition is met, store answer and continue searching for better (leftward) position.
"""

# ==================== TIME & SPACE COMPLEXITY ====================
"""
Both Lower and Upper Bound:

Binary Search Approach:
- Time Complexity: O(log n) - Search space halves each iteration
- Space Complexity: O(1) - Only using constant extra variables

Linear Search Approach:
- Time Complexity: O(n) - May need to check every element
- Space Complexity: O(1) - Only using constant extra variables

The binary search approach is significantly more efficient for large arrays.
"""

# ==================== SOLUTION IMPLEMENTATIONS ====================

def lowerBoundLinear(arr: List[int], target: int) -> int:
    """
    Lower Bound - Linear Search - O(n) time
    Find first element >= target
    """
    n = len(arr)
    
    # Check each element sequentially
    for i in range(n):
        if arr[i] >= target:               # First element >= target
            return i
    
    return n                               # Target > all elements


def lowerBoundBinary(arr: List[int], target: int) -> int:
    """
    Lower Bound - Binary Search - O(log n) time
    Find first element >= target using binary search
    """
    n = len(arr)
    low = 0
    high = n - 1
    ans = n                                # Default: insertion at end
    
    while low <= high:
        # Calculate mid (prevents integer overflow)
        mid = low + (high - low) // 2
        
        # If current element >= target, it's a potential answer
        if arr[mid] >= target:
            ans = mid                      # Store potential answer
            high = mid - 1                 # Search left for earlier position
        else:
            low = mid + 1                  # Search right
    
    return ans


def upperBoundLinear(arr: List[int], target: int) -> int:
    """
    Upper Bound - Linear Search - O(n) time
    Find first element > target
    """
    n = len(arr)
    
    # Check each element sequentially
    for i in range(n):
        if arr[i] > target:                # First element > target
            return i
    
    return n                               # Target >= all elements


def upperBoundBinary(arr: List[int], target: int) -> int:
    """
    Upper Bound - Binary Search - O(log n) time
    Find first element > target using binary search
    """
    n = len(arr)
    low = 0
    high = n - 1
    ans = n                                # Default: insertion at end
    
    while low <= high:
        # Calculate mid (prevents integer overflow)
        mid = low + (high - low) // 2
        
        # If current element > target, it's a potential answer
        if arr[mid] > target:
            ans = mid                      # Store potential answer
            high = mid - 1                 # Search left for earlier position
        else:
            low = mid + 1                  # Search right
    
    return ans


# ==================== PRACTICAL APPLICATIONS ====================

def countOccurrences(arr: List[int], target: int) -> int:
    """
    Count occurrences of target in sorted array
    Uses: upper_bound - lower_bound
    """
    lower = lowerBoundBinary(arr, target)
    upper = upperBoundBinary(arr, target)
    
    # If lower bound is at end or doesn't match target, count is 0
    if lower == len(arr) or arr[lower] != target:
        return 0
    
    return upper - lower


def findFirstLastOccurrence(arr: List[int], target: int) -> tuple:
    """
    Find first and last occurrence of target
    Returns (-1, -1) if target doesn't exist
    """
    lower = lowerBoundBinary(arr, target)
    
    # Target doesn't exist
    if lower == len(arr) or arr[lower] != target:
        return (-1, -1)
    
    upper = upperBoundBinary(arr, target)
    return (lower, upper - 1)              # upper-1 is last occurrence


def insertInSortedArray(arr: List[int], target: int) -> List[int]:
    """
    Insert target in sorted array maintaining order
    """
    pos = lowerBoundBinary(arr, target)
    arr.insert(pos, target)
    return arr


def findRange(arr: List[int], target: int) -> List[int]:
    """
    LeetCode 34: Find First and Last Position of Element in Sorted Array
    """
    first, last = findFirstLastOccurrence(arr, target)
    return [first, last]


# ==================== COMPREHENSIVE EXAMPLES ====================

def demonstrateWithExamples():
    """
    Demonstrate lower and upper bound with comprehensive examples
    """
    arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
    print(f"Array: {arr}")
    print(f"Index: {list(range(len(arr)))}")
    print("-" * 50)
    
    test_targets = [0, 1, 3, 4, 8, 11, 12]
    
    for target in test_targets:
        lower = lowerBoundBinary(arr, target)
        upper = upperBoundBinary(arr, target)
        count = countOccurrences(arr, target)
        
        print(f"Target: {target}")
        print(f"  Lower Bound: {lower}")
        print(f"  Upper Bound: {upper}")
        print(f"  Count: {count}")
        
        if lower < len(arr):
            print(f"  Element at lower bound: {arr[lower]}")
        if upper < len(arr):
            print(f"  Element at upper bound: {arr[upper]}")
        else:
            print(f"  Upper bound points to end of array")
        print("-" * 30)


# ==================== TEST CASES ====================

def test_all_implementations():
    """Test all implementations with various cases"""
    
    test_cases = [
        # (array, target, expected_lower, expected_upper)
        ([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 3, 2, 4),      # Target exists (multiple)
        ([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 9, 7, 7),      # Target doesn't exist (middle)
        ([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 0, 0, 0),      # Target < all elements
        ([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 12, 10, 10),   # Target > all elements
        ([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 1, 0, 1),      # Target at start
        ([1, 2, 3, 3, 5, 8, 8, 10, 10, 11], 11, 9, 10),    # Target at end
        ([5, 5, 5, 5, 5], 5, 0, 5),                         # All elements same
        ([1, 3, 5, 7, 9], 6, 3, 3),                         # Target in gap
        ([1], 1, 0, 1),                                      # Single element (match)
        ([1], 2, 1, 1),                                      # Single element (no match)
        ([], 5, 0, 0),                                       # Empty array
    ]
    
    for arr, target, exp_lower, exp_upper in test_cases:
        print(f"Array: {arr}, Target: {target}")
        
        # Test lower bound
        lower_linear = lowerBoundLinear(arr, target)
        lower_binary = lowerBoundBinary(arr, target)
        
        # Test upper bound
        upper_linear = upperBoundLinear(arr, target)
        upper_binary = upperBoundBinary(arr, target)
        
        # Verify results
        lower_match = lower_linear == lower_binary == exp_lower
        upper_match = upper_linear == upper_binary == exp_upper
        
        print(f"  Lower Bound: Linear={lower_linear}, Binary={lower_binary}, Expected={exp_lower} {'✓' if lower_match else '✗'}")
        print(f"  Upper Bound: Linear={upper_linear}, Binary={upper_binary}, Expected={exp_upper} {'✓' if upper_match else '✗'}")
        print(f"  Count: {countOccurrences(arr, target)}")
        print("-" * 60)


# ==================== FOLLOW-UPS ====================
"""
Potential Follow-up Questions:

1. **How to handle duplicates efficiently?**
   - Lower/Upper bound naturally handle duplicates
   - Count occurrences: upper_bound - lower_bound

2. **Can we find exact range of target occurrences?**
   - First occurrence: lower_bound
   - Last occurrence: upper_bound - 1

3. **What if array is sorted in descending order?**
   - Modify comparison logic or reverse array first
   - Lower bound becomes: first element <= target
   - Upper bound becomes: first element < target

4. **Memory-efficient implementation for large arrays?**
   - Current implementation is already O(1) space
   - For external arrays, use memory-mapped files

5. **Thread-safe implementation?**
   - Binary search is naturally thread-safe for read operations
   - No shared state modification during search

6. **What about floating-point arrays?**
   - Need epsilon-based comparison for floating-point precision
   - Define tolerance for "equal" comparisons

7. **Can we optimize for repeated queries?**
   - Build index structure (B-tree, segment tree)
   - Trade space for faster query time

8. **How to handle custom comparison functions?**
   - Pass comparator function as parameter
   - Useful for complex objects or custom sorting

9. **What about rotated sorted arrays?**
   - Need to modify approach to handle rotation point
   - Find rotation point first, then apply bounds

10. **Implementation in other languages?**
    - C++: std::lower_bound, std::upper_bound
    - Java: Collections.binarySearch with modifications
    - Python: bisect.bisect_left, bisect.bisect_right
"""

# ==================== BUILT-IN ALTERNATIVES ====================
"""
Python Built-in Equivalents:
- bisect.bisect_left(arr, target) ≡ lowerBoundBinary(arr, target)
- bisect.bisect_right(arr, target) ≡ upperBoundBinary(arr, target)

Example:
import bisect
arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
target = 3
lower = bisect.bisect_left(arr, target)   # 2
upper = bisect.bisect_right(arr, target)  # 4

However, implementing from scratch is important for:
- Interview preparation
- Understanding the underlying algorithm
- Customization for specific needs
- Language-independent knowledge
"""

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    # Example usage
    arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
    target = 9
    
    print("LOWER BOUND & UPPER BOUND DEMONSTRATION")
    print("=" * 60)
    
    print(f"Array: {arr}")
    print(f"Target: {target}")
    print(f"Lower Bound: {lowerBoundBinary(arr, target)}")
    print(f"Upper Bound: {upperBoundBinary(arr, target)}")
    print(f"Count of {target}: {countOccurrences(arr, target)}")
    
    # Comprehensive examples
    print("\n" + "=" * 60)
    print("COMPREHENSIVE EXAMPLES")
    print("=" * 60)
    demonstrateWithExamples()
    
    # Run all tests
    print("\n" + "=" * 60)
    print("RUNNING COMPREHENSIVE TESTS")
    print("=" * 60)
    test_all_implementations()