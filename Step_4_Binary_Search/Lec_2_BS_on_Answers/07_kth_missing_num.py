"""
Problem: Given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `k`. Return the `k`-th positive integer that is missing from this array.

Example 1:
Input: `arr = [2,3,4,7,11]`, `k = 5`
Output: `9`
Explanation: The missing positive integers are `[1,5,6,8,9,10,12,13,...]`. The 5th missing positive integer is 9.

Example 2:
Input: `arr = [1,2,3,4]`, `k = 2`
Output: `6`
Explanation: The missing positive integers are `[5,6,7,...]`. The 2nd missing positive integer is 6.

Platform: LeetCode
Difficulty: Easy/Medium
Topics: Array, Binary Search

LINK: https://leetcode.com/problems/kth-missing-positive-number/description/

"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input:
    - `arr`: A sorted array of positive integers.
    - `k`: An integer representing the k-th missing positive number to find.
- Output: The k-th missing positive integer.
- Constraints:
    - `1 <= arr.length <= 1000`
    - `1 <= arr[i] <= 1000`
    - `1 <= k <= 1000`
    - `arr[i] < arr[j]` for `1 <= i < j <= arr.length` (strictly increasing)
- Edge Cases:
    - `k` is very small (e.g., 1).
    - `k` is very large (e.g., larger than any number in `arr`).
    - The missing number is before the first element of `arr`.
    - The missing number is after the last element of `arr`.

APPROACH:
The problem asks for the k-th missing positive integer. Since the array is sorted, we can leverage this property.

For the optimal approach, we can use binary search. The key insight is to determine how many numbers are missing *before* a given element `arr[mid]`.

1.  **Count Missing Numbers:** For any element `arr[i]` in a 0-indexed array, if there were no missing numbers before it, `arr[i]` would ideally be `i + 1`. Therefore, the number of missing positive integers *before* `arr[i]` is `arr[i] - (i + 1)`.
2.  **Binary Search on Missing Count:** We can binary search on the `arr` array to find an index `mid` such that the number of missing elements before `arr[mid]` is less than `k`, but the number of missing elements before `arr[mid+1]` (if it exists) is greater than or equal to `k`.
    *   If `missing_count_at_mid < k`: This means the `k`-th missing number is either `arr[mid]` itself (if `k` is exactly `missing_count_at_mid + 1`) or further to the right. So, we need to search in the right half (`low = mid + 1`).
    *   If `missing_count_at_mid >= k`: This means the `k`-th missing number is before or at `arr[mid]`. So, we need to search in the left half (`high = mid - 1`).
3.  **Calculate the K-th Missing Number:** After the binary search, `low` will point to the index where the `k`-th missing number would be if we were to insert it.
    The number of missing elements *before* `arr[low]` (or before the position `low` if `low` is out of bounds) is `arr[low-1] - (low-1 + 1)` if `low > 0`, otherwise 0.
    The `k`-th missing number will be `low + k`.
    Let's verify this:
    - If `low` is the index where the binary search terminates, it means `arr[low-1]` (if `low > 0`) has `arr[low-1] - low` missing numbers before it.
    - We need `k` missing numbers. We already have `arr[low-1] - low` missing numbers.
    - So, we need `k - (arr[low-1] - low)` more missing numbers.
    - These missing numbers will be `arr[low-1] + 1, arr[low-1] + 2, ...`
    - The `k`-th missing number will be `arr[low-1] + (k - (arr[low-1] - low)) = arr[low-1] + k - arr[low-1] + low = k + low`.
    - If `low` is 0, it means `k` is smaller than `arr[0] - 1`. In this case, the missing numbers are `1, 2, ..., k`. So the `k`-th missing number is `k`. Our formula `low + k` (which is `0 + k`) still holds.

TIME COMPLEXITY: O(log N)
SPACE COMPLEXITY: O(1)
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def findKthBrute(arr, k):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - Iterate through the array `arr`. For each number `num` in `arr`, check if it's less than or equal to `k`.
    - If `num <= k`, it means `num` is present in the array, so it "consumes" one of the `k` missing numbers we are looking for. To compensate, we increment `k` by 1, effectively looking for the next missing number.
    - If `num > k`, it means `num` is greater than the current `k`. Since `arr` is sorted, all subsequent numbers will also be greater than `k`. At this point, `k` represents the `k`-th missing positive integer.
    
    Example Walkthrough: `arr = [2,3,4,7,11]`, `k = 5`
    
    Initial: `k = 5`
    
    1. `num = 2`: `2 <= 5` is True. `k` becomes `5 + 1 = 6`.
       (We were looking for the 5th missing. `1` is missing. `2` is present. So now we are effectively looking for the 5th missing *after* 2, which is the 6th overall if we consider 1 as the 1st missing.)
       Missing numbers so far: `[1]`
       Current `k` (target missing): `6`
    
    2. `num = 3`: `3 <= 6` is True. `k` becomes `6 + 1 = 7`.
       Missing numbers so far: `[1]`
       Current `k` (target missing): `7`
    
    3. `num = 4`: `4 <= 7` is True. `k` becomes `7 + 1 = 8`.
       Missing numbers so far: `[1]`
       Current `k` (target missing): `8`
    
    4. `num = 7`: `7 <= 8` is True. `k` becomes `8 + 1 = 9`.
       Missing numbers so far: `[1, 5, 6]` (5 and 6 are missing before 7)
       Current `k` (target missing): `9`
    
    5. `num = 11`: `11 <= 9` is False. Break the loop.
    
    Return `k` which is `9`.
    
    This approach works because `k` effectively tracks the value of the `k`-th missing number. Each time we encounter a number in `arr` that is less than or equal to our current `k` (meaning it's a number we would have counted as missing if it weren't present), we increment `k` to "skip" over it and continue searching for the next missing number.
    
    Args:
        arr: The input array.
        k: The k-th missing number to find.
    
    Returns:
        The k-th missing positive integer.
    
    Time Complexity: O(N) - In the worst case, we iterate through the entire `arr` array.
    Space Complexity: O(1)
    """
    for num in arr:
        if num <= k:
            k += 1
        else:
            break
    return k   

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (BINARY SEARCH)
# ==============================================================================

def findKthOp(arr, k):
    """
    OPTIMAL APPROACH - Most efficient solution possible using Binary Search.
    
    Intuition:
    - The core idea is to find an index `mid` in the array such that the number of missing elements *before* `arr[mid]` is less than `k`, but the number of missing elements *before* `arr[mid+1]` (if it exists) is greater than or equal to `k`.
    - The number of missing elements before `arr[i]` is `arr[i] - (i + 1)`. This is a monotonic function, allowing binary search.
    
    Approach:
    1.  Initialize `low = 0` and `high = n - 1` (where `n` is the length of `arr`).
    2.  Perform binary search:
        - Calculate `mid = low + (high - low) // 2`.
        - Calculate `missing_count = arr[mid] - (mid + 1)`. This tells us how many positive integers are missing before `arr[mid]`.
        - If `missing_count < k`: This means the `k`-th missing number is located *after* `arr[mid]` (or `arr[mid]` itself if `k` is exactly `missing_count + 1`). So, we need to search in the right half: `low = mid + 1`.
        - If `missing_count >= k`: This means the `k`-th missing number is located *before or at* `arr[mid]`. So, we need to search in the left half: `high = mid - 1`.
    3.  After the loop terminates, `low` will point to the index where the `k`-th missing number would be if we were to insert it.
    4.  The `k`-th missing number can be calculated as `low + k`.
        - Let's re-derive the formula:
            - When the loop terminates, `high` will be `low - 1`.
            - The number of missing elements up to `arr[high]` (or `arr[low-1]`) is `arr[high] - (high + 1)`.
            - We need `k` missing elements. We have already accounted for `arr[high] - (high + 1)` missing elements.
            - The remaining `k - (arr[high] - (high + 1))` missing elements will be after `arr[high]`.
            - So, the `k`-th missing number is `arr[high] + (k - (arr[high] - (high + 1)))`.
            - Simplifying this: `arr[high] + k - arr[high] + high + 1 = k + high + 1`.
            - Since `low = high + 1` at termination, the formula becomes `k + low`.
            - This formula also correctly handles the case where `k` is smaller than `arr[0] - 1` (i.e., `low` becomes 0). In this case, `0 + k = k`, which is correct.
    
    Args:
        arr: The input array.
        k: The k-th missing number to find.
    
    Returns:
        The k-th missing positive integer.
    
    Time Complexity: O(log N) - Due to binary search on the array.
    Space Complexity: O(1)
    """
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        missing = arr[mid] - (mid + 1) # Number of missing elements before arr[mid]

        if missing < k:
            low = mid + 1 # k-th missing is to the right of mid
        else:
            high = mid - 1 # k-th missing is to the left of or at mid

    # At the end of the loop, 'low' will be the index where the k-th missing number would be.
    # The number of missing elements before arr[low-1] (if low > 0) is arr[low-1] - (low-1 + 1).
    # The k-th missing number is arr[low-1] + (k - (arr[low-1] - (low-1 + 1)))
    # which simplifies to k + (low-1 + 1) = k + low.
    return low + k

# ==============================================================================
# MAIN SOLUTION FUNCTION
# ==============================================================================

def solve_problem(arr, k, approach="optimal"):
    """
    Main solution function that calls the appropriate approach.
    
    Args:
        arr: The input array.
        k: The k-th missing number to find.
        approach: "brute" or "optimal" (default)
    
    Returns:
        The k-th missing positive integer.
    """
    
    if approach == "brute":
        return findKthBrute(arr, k)
    elif approach == "optimal":
        return findKthOp(arr, k)
    else:
        raise ValueError("Approach must be 'brute' or 'optimal'")

# ==============================================================================
# TEST CASES
# ==============================================================================

def test_solution():
    """
    Test cases to verify both approaches work correctly.
    """
    
    print("TESTING ALL APPROACHES:")
    print("=" * 40)
    
    # TEST CASE 1: Example from problem description
    arr1 = [2,3,4,7,11]
    k1 = 5
    expected1 = 9
    
    print("\nTest 1 - Basic example:")
    for approach in ["brute", "optimal"]:
        result1 = solve_problem(arr1, k1, approach)
        assert result1 == expected1, f"Test 1 {approach} failed: expected {expected1}, got {result1}"
        print(f"✓ {approach.capitalize()} approach passed")
    
    # TEST CASE 2: Example from problem description
    arr2 = [1,2,3,4]
    k2 = 2
    expected2 = 6
    
    print("\nTest 2 - No missing numbers initially:")
    for approach in ["brute", "optimal"]:
        result2 = solve_problem(arr2, k2, approach)
        assert result2 == expected2, f"Test 2 {approach} failed: expected {expected2}, got {result2}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 3: Missing number before first element
    arr3 = [5,6,7]
    k3 = 3
    expected3 = 3 # Missing: 1, 2, 3, 4
    
    print("\nTest 3 - Missing before first element:")
    for approach in ["brute", "optimal"]:
        result3 = solve_problem(arr3, k3, approach)
        assert result3 == expected3, f"Test 3 {approach} failed: expected {expected3}, got {result3}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 4: Missing number after last element
    arr4 = [1,2,3]
    k4 = 1
    expected4 = 4 # Missing: 4, 5, ...
    
    print("\nTest 4 - Missing after last element:")
    for approach in ["brute", "optimal"]:
        result4 = solve_problem(arr4, k4, approach)
        assert result4 == expected4, f"Test 4 {approach} failed: expected {expected4}, got {result4}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 5: Single element array
    arr5 = [10]
    k5 = 5
    expected5 = 5 # Missing: 1,2,3,4,5,6,7,8,9
    
    print("\nTest 5 - Single element array:")
    for approach in ["brute", "optimal"]:
        result5 = solve_problem(arr5, k5, approach)
        assert result5 == expected5, f"Test 5 {approach} failed: expected {expected5}, got {result5}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 6: Large input performance test (only for optimal)
    print("\nTest 6 - Performance comparison (Optimal only):")
    large_arr = [i * 2 for i in range(1, 501)] # [2, 4, 6, ..., 1000]
    large_k = 250
    # Missing numbers are 1, 3, 5, ..., 499.
    # The 250th missing number will be 2 * 250 - 1 = 499.
    large_expected = 499
    
    import time
    # Brute force would be too slow for this, so only test optimal
    start_time = time.time()
    result_optimal = solve_problem(large_arr, large_k, "optimal")
    end_time = time.time()
    assert result_optimal == large_expected, f"Test 6 optimal failed: expected {large_expected}, got {result_optimal}"
    print(f"Optimal approach: {end_time - start_time:.4f} seconds")
    print(f"✓ Optimal approach passed for large input")
    
    print("\n🎉 All tests passed!")

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

TIME COMPLEXITY:
- Brute Force: O(N)
    - In the worst case, the loop iterates through all `N` elements of the `arr` array.
- Optimal (Binary Search): O(log N)
    - The binary search reduces the search space by half in each step, leading to logarithmic time complexity with respect to the length of the array `N`.

SPACE COMPLEXITY:
- Both Brute Force and Optimal: O(1)
    - No additional data structures are used that scale with input size beyond a few variables.

TRADE-OFFS:
- The brute force approach is simpler to understand and implement but less efficient for larger input arrays.
- The optimal approach using binary search is more complex to grasp initially but provides significantly better performance for larger inputs, making it the preferred solution for competitive programming.
"""

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Run detailed tests
    test_solution()
    
    # Example usage with default optimal approach
    arr_ex = [2,3,4,7,11]
    k_ex = 5
    result = solve_problem(arr_ex, k_ex) # Uses optimal by default
    print(f"\nFinal Result (Optimal for [2,3,4,7,11], k=5): {result}")
    
    # Example: Test specific approach
    brute_result = solve_problem(arr_ex, k_ex, "brute")
    print(f"Brute Force Result for [2,3,4,7,11], k=5: {brute_result}")
