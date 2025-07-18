"""
Maximum Product Subarray - Complete Solution with Documentation

Author: [Your Name]
Date: [Current Date]
Problem Source: LeetCode #152 / Similar DSA Problem
"""

from typing import List

# ==================== PROBLEM STATEMENT ====================
"""
Problem: Find the maximum product of a contiguous subarray within a given array of integers.
Given an array of integers, return the maximum product that can be obtained from any subarray.
"""

# ==================== OBSERVATIONS ====================
"""
Key Constraints & Edge Cases:
1. Array can contain positive, negative, and zero values
2. At least one element is guaranteed (n >= 1)
3. Negative numbers: Even count → positive product, Odd count → one must be excluded
4. Zero acts as a "reset" point, breaking the subarray into separate parts
5. Maximum subarray length can be the entire array
6. Single element arrays return that element as the answer

Patterns Noticed:
- Two negatives make a positive, so even negatives are good
- Odd negatives require excluding one negative for maximum product
- Zeros split the problem into independent subproblems
"""

# ==================== INTUITION ====================
"""
Key Insight: 
The optimal approach uses prefix and suffix products simultaneously.
- If we have odd negatives, either prefix or suffix will give us the maximum
- Prefix excludes the last negative, suffix excludes the first negative
- Zeros reset both prefix and suffix to 1, naturally handling the "split" case
- We track the maximum of both prefix and suffix at each step

This eliminates the need to explicitly handle different cases (odd/even negatives, zeros)
"""

# ==================== DRY RUN ====================
"""
Example: arr = [2, 3, -2, 4]

Step-by-step execution:
i=0: prefix=1*2=2, suffix=1*4=4, maxi=max(-inf, max(2,4))=4
i=1: prefix=2*3=6, suffix=4*(-2)=-8, maxi=max(4, max(6,-8))=6  
i=2: prefix=6*(-2)=-12, suffix=-8*3=-24, maxi=max(6, max(-12,-24))=6
i=3: prefix=-12*4=-48, suffix=-24*2=-48, maxi=max(6, max(-48,-48))=6

Result: 6 (subarray [2,3])
"""

# ==================== APPROACH ====================
"""
Algorithm: Two-Pointer Prefix-Suffix Technique
1. Maintain two running products: prefix (left-to-right) and suffix (right-to-left)
2. Reset to 1 whenever we encounter a zero
3. Track maximum of both products at each step
4. Return the overall maximum found

This approach handles all edge cases naturally without explicit conditionals.
"""

# ==================== TIME & SPACE COMPLEXITY ====================
"""
Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Only using constant extra space for variables

Comparison with other approaches:
- Brute Force: O(n³) time, O(1) space
- Better Brute: O(n²) time, O(1) space  
- Optimal: O(n) time, O(1) space
"""

# ==================== SOLUTION IMPLEMENTATIONS ====================

def maxProductSubArrayBrute(arr: List[int]) -> int:
    """
    Brute Force Approach - O(n³) time complexity
    Check all possible subarrays by generating them explicitly
    """
    n = len(arr)
    maxProduct = float('-inf')  # Handle negative numbers correctly
    
    # Generate all possible subarrays
    for i in range(n):                    # Start index
        for j in range(i, n):             # End index
            product = 1
            # Calculate product of subarray from i to j
            for k in range(i, j + 1):     # Elements in current subarray
                product *= arr[k]
            
            maxProduct = max(product, maxProduct)
    
    return maxProduct


def maxProductSubArrayBetter(arr: List[int]) -> int:
    """
    Better Approach - O(n²) time complexity
    Optimize by calculating product incrementally instead of recalculating
    """
    n = len(arr)
    maxProduct = float('-inf')  # Handle negative numbers correctly
    
    # For each starting position
    for i in range(n):
        product = 1
        # Extend the subarray from position i
        for j in range(i, n):
            product *= arr[j]              # Incremental product calculation
            maxProduct = max(maxProduct, product)
    
    return maxProduct


def maxProductSubArrayOptimal(arr: List[int]) -> int:
    """
    Optimal Approach - O(n) time, O(1) space
    Uses prefix-suffix technique to handle all cases efficiently
    """
    n = len(arr)
    prefix = 1      # Left-to-right running product
    suffix = 1      # Right-to-left running product
    maxi = float('-inf')
    
    for i in range(n):
        # Reset to 1 if we hit zero (natural subarray break)
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        
        # Calculate running products from both ends
        prefix *= arr[i]                   # Forward direction
        suffix *= arr[n - 1 - i]          # Backward direction
        
        # Track maximum of both products
        maxi = max(maxi, max(prefix, suffix))
    
    return maxi


# ==================== TEST CASES ====================
def test_solutions():
    """Test all implementations with various cases"""
    
    test_cases = [
        [2, 3, -2, 4],      # Mixed positive/negative
        [-2, 0, -1],        # Contains zero
        [-2, -3, -4],       # All negative (odd count)
        [1, 2, 3, 4],       # All positive
        [0, 0, 0],          # All zeros
        [5],                # Single element
        [-1, -2, -3, -4],   # All negative (even count)
    ]
    
    for arr in test_cases:
        brute_result = maxProductSubArrayBrute(arr)
        better_result = maxProductSubArrayBetter(arr)
        optimal_result = maxProductSubArrayOptimal(arr)
        
        print(f"Array: {arr}")
        print(f"Brute: {brute_result}, Better: {better_result}, Optimal: {optimal_result}")
        print(f"All match: {brute_result == better_result == optimal_result}")
        print("-" * 50)


# ==================== FOLLOW-UPS ====================
"""
Potential Follow-up Questions:

1. **Can we optimize further?** 
   - Current solution is already O(n) time and O(1) space, which is optimal
   - No further optimization possible for this problem

2. **What if we need to return the actual subarray?**
   - Modify to track start and end indices when maximum is updated
   - Requires O(1) extra space for index tracking

3. **Handle empty array?**
   - Add edge case check: if not arr: return 0 (or handle as per requirements)

4. **What about integer overflow?**
   - In languages like Java/C++, consider using long or BigInteger
   - Python handles big integers automatically

5. **Variation: Maximum Product of K-length Subarray?**
   - Use sliding window technique with product calculation
   - Handle zeros differently (skip or break window)

6. **Can we solve using dynamic programming?**
   - Yes, track max_ending_here and min_ending_here (for negative handling)
   - Similar time complexity but different approach

7. **What if array is very large and doesn't fit in memory?**
   - Stream processing: read chunks and maintain running calculations
   - May need to handle edge cases where optimal subarray spans chunks
"""

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    # Example usage
    arr = [2, 3, -2, 4]
    print(f"Input: {arr}")
    print(f"Maximum Product Subarray: {maxProductSubArrayOptimal(arr)}")
    
    # Run comprehensive tests
    print("\n" + "="*50)
    print("RUNNING COMPREHENSIVE TESTS")
    print("="*50)
    test_solutions()