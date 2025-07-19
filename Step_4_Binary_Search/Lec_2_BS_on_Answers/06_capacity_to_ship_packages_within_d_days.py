"""
DSA Problem Solution Template
============================

Problem: A conveyor belt has packages that must be shipped from one port to another within 
`days` days. The `i`-th package on the conveyor belt has a weight of `weights[i]`. 
Each day, we load the ship with packages on the conveyor belt (in the order given by `weights`). 
We may not load more weight than the maximum weight capacity of the ship. Return the least 
weight capacity of the ship that will result in all the packages on the conveyor belt being 
shipped within `days` days.

Platform: LeetCode
Difficulty: Medium
Topics: Array, Binary Search
LINK: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input:
    - `weights`: An array of integers representing the weights of packages.
    - `days`: The maximum number of days to ship all packages.
- Output: The least weight capacity of the ship required to ship all packages within `days` days.
- Constraints:
    - `1 <= days <= weights.length <= 5 * 10^4`
    - `1 <= weights[i] <= 500`
- Edge Cases:
    - The minimum possible capacity is the maximum weight of a single package (since each package must be shipped individually).
    - The maximum possible capacity is the sum of all package weights (all packages shipped in one day).
    - Packages must be shipped in the given order.

APPROACH:
This problem asks for the "least weight capacity" that satisfies a condition (shipping within `days` days). 
This is a classic "search for the minimum value that satisfies a property" problem, which is a strong indicator for binary search. 
The property we are looking for is that `days_required(capacity) <= days`. 
This property is monotonic: if a `capacity` works, any `capacity` greater than it will also work (because a larger capacity means fewer days required).

1.  **Define Search Space:**
    *   The smallest possible ship capacity (`low`) must be at least the maximum weight of any single package (`max(weights)`), because we cannot split packages.
    *   The largest possible ship capacity (`high`) is the sum of all package weights (`sum(weights)`), which would allow all packages to be shipped in one day.
    *   So, our search space for the `capacity` is `[max(weights), sum(weights)]`.
2.  **Binary Search on Capacity:**
    *   For a given `mid` (which represents a potential `capacity`), calculate the `days_required` to ship all packages with this `capacity` using the `daysReq` helper function.
    *   If `days_required <= days`: This `mid` capacity is sufficient. Since we want the *least* such capacity, we try to find an even smaller one by searching in the left half (`high = mid - 1`). We store `mid` as a potential answer.
    *   If `days_required > days`: This `mid` capacity is too small (it requires too many days). We need a larger capacity, so we search in the right half (`low = mid + 1`).
3.  **Helper Function `daysReq(arr, capacity)`:** This function simulates the shipping process for a given `capacity` and returns the number of days required. It iterates through the `weights` array, accumulating the `load` for the current day. If adding the next package exceeds the `capacity`, a new day is started, and the current package becomes the `load` for the new day.

TIME COMPLEXITY: O(N * log(SumOfWeights - MaxWeight))
SPACE COMPLEXITY: O(1)
"""

# ==============================================================================
# HELPER FUNCTION
# ==============================================================================

def daysReq(arr, capacity):
    """
    Calculates the number of days required to ship all packages with a given capacity.

    Args:
        arr: The array of package weights.
        capacity: The maximum weight capacity of the ship.

    Returns:
        The number of days required.
    """
    load = 0
    days = 1
    for weight in arr:
        # If adding the current package exceeds capacity, start a new day
        if load + weight > capacity:
            days += 1
            load = weight # Current package starts a new day's load
        else:
            load += weight # Add package to current day's load
    return days

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def leastCapacityBrute(arr, days):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - Iterate through all possible ship capacities, starting from the minimum possible (max individual package weight) up to the maximum possible (sum of all package weights).
    - For each capacity, calculate the number of days required to ship all packages.
    - The first capacity that allows shipping within the given `days` will be the least capacity.
    
    Approach:
    1.  Determine the range of possible capacities:
        - `low`: `max(arr)` (maximum individual package weight).
        - `high`: `sum(arr)` (total weight of all packages).
    2.  Iterate `capacity` from `low` to `high` (inclusive).
    3.  For each `capacity`, call the `daysReq` helper function to find out how many days it would take.
    4.  If `daysReq(arr, capacity) <= days`, then this `capacity` is the smallest one found so far that satisfies the condition. Return `capacity`.
    5.  The problem guarantees an answer, so the loop will always find one.
    
    Args:
        arr: The array of package weights.
        days: The maximum number of days allowed.
    
    Returns:
        The least weight capacity of the ship.
    
    Time Complexity: O((SumOfWeights - MaxWeight) * N)
        - `(SumOfWeights - MaxWeight)`: The range of capacities to iterate through. `SumOfWeights` can be up to `5 * 10^4 * 500 = 2.5 * 10^7`.
        - `N`: The length of `weights` array, due to the `daysReq` function iterating through the array.
    Space Complexity: O(1)
    """
    low = max(arr)
    high = sum(arr)

    for capacity in range(low, high + 1):
        if daysReq(arr, capacity) <= days:
            return capacity
        
    return -1 # Should not be reached due to problem constraints

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (BINARY SEARCH ON ANSWER)
# ==============================================================================

def leastCapacityOp(arr, days):
    """
    OPTIMAL APPROACH - Most efficient solution possible using Binary Search.
    
    Intuition:
    - The problem asks for the minimum `capacity` that satisfies a condition (`days_required <= days`). The condition is monotonic with respect to `capacity`. This allows us to use binary search on the range of possible capacities.
    
    Approach:
    1.  Define the search space for the binary search:
        - `low`: The minimum possible capacity is `max(arr)`.
        - `high`: The maximum possible capacity is `sum(arr)`.
    2.  Perform binary search within the `[low, high]` range:
        - Calculate `mid = low + (high - low) // 2`.
        - Call the `daysReq` helper function: `days_required = daysReq(arr, mid)`.
        - If `days_required <= days`: It means `mid` capacity is sufficient. Since we want the *least* such capacity, we try to find an even smaller one by searching in the left half (`high = mid - 1`).
        - If `days_required > days`: It means `mid` capacity is too small (it requires too many days). We need a larger capacity. So, we discard `mid` and everything to its left and narrow our search to the right half by setting `low = mid + 1`.
    3.  The loop continues until `low > high`. At the end, `low` will hold the smallest capacity for which `daysReq` is `True`.
    
    Args:
        arr: The array of package weights.
        days: The maximum number of days allowed.
    
    Returns:
        The least weight capacity of the ship.
    
    Time Complexity: O(N * log(SumOfWeights - MaxWeight))
        - `log(SumOfWeights - MaxWeight)`: The number of iterations in the binary search. The search space for capacity is from `max(weights)` to `sum(weights)`.
        - `N`: The length of the `weights` array, traversed in each call to the `daysReq` helper function.
    Space Complexity: O(1)
    """
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = low + (high - low) // 2

        days_required = daysReq(arr, mid)

        if days_required <= days:
            high = mid - 1 # mid is a possible answer, try smaller
        else:
            low = mid + 1 # mid is too small, need larger

    return low # 'low' will be the smallest capacity that satisfies the condition

# ==============================================================================
# MAIN SOLUTION FUNCTION
# ==============================================================================

def solve_problem(weights, days, approach="optimal"):
    """
    Main solution function that calls the appropriate approach.
    
    Args:
        weights: The array of package weights.
        days: The maximum number of days allowed.
        approach: "brute" or "optimal" (default)
    
    Returns:
        The least weight capacity of the ship.
    """
    
    if approach == "brute":
        return leastCapacityBrute(weights, days)
    elif approach == "optimal":
        return leastCapacityOp(weights, days)
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
    weights1 = [1,2,3,4,5,6,7,8,9,10]
    days1 = 5
    expected1 = 15
    
    print("Test 1 - Basic example:")
    for approach in ["brute", "optimal"]:
        result1 = solve_problem(weights1, days1, approach)
        assert result1 == expected1, f"Test 1 {approach} failed: expected {expected1}, got {result1}"
        print(f"✓ {approach.capitalize()} approach passed")
    
    # TEST CASE 2: Example from problem description
    weights2 = [3,2,2,4,1,4]
    days2 = 3
    expected2 = 6
    
    print("Test 2 - Another example:")
    for approach in ["brute", "optimal"]:
        result2 = solve_problem(weights2, days2, approach)
        assert result2 == expected2, f"Test 2 {approach} failed: expected {expected2}, got {result2}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 3: Example from problem description
    weights3 = [1,2,3,1,1]
    days3 = 4
    expected3 = 3
    
    print("Test 3 - Third example:")
    for approach in ["brute", "optimal"]:
        result3 = solve_problem(weights3, days3, approach)
        assert result3 == expected3, f"Test 3 {approach} failed: expected {expected3}, got {result3}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 4: All packages shipped in one day
    weights4 = [10, 20, 30]
    days4 = 1
    expected4 = 60
    
    print("Test 4 - All packages in one day:")
    for approach in ["brute", "optimal"]:
        result4 = solve_problem(weights4, days4, approach)
        assert result4 == expected4, f"Test 4 {approach} failed: expected {expected4}, got {result4}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 5: Each package shipped in its own day
    weights5 = [10, 20, 30]
    days5 = 3
    expected5 = 30
    
    print("Test 5 - Each package in its own day:")
    for approach in ["brute", "optimal"]:
        result5 = solve_problem(weights5, days5, approach)
        assert result5 == expected5, f"Test 5 {approach} failed: expected {expected5}, got {result5}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 6: Large input performance test (only for optimal)
    print("Test 6 - Performance comparison (Optimal only):")
    large_weights = [500] * (5 * 10**4) # 50000 packages, each 500 weight
    large_days = 1000 # Ship in 1000 days
    # Expected: (50000 * 500) / 1000 = 25000
    # More precisely, 50000 packages / 1000 days = 50 packages per day.
    # 50 packages * 500 weight/package = 25000 capacity
    large_expected = 25000 
    
    import time
    # Brute force would be too slow for this, so only test optimal
    start_time = time.time()
    result_optimal = solve_problem(large_weights, large_days, "optimal")
    end_time = time.time()
    assert result_optimal == large_expected, f"Test 6 optimal failed: expected {large_expected}, got {result_optimal}"
    print(f"Optimal approach: {end_time - start_time:.4f} seconds")
    print(f"✓ Optimal approach passed for large input")
    
    print("🎉 All tests passed!")

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

TIME COMPLEXITY:
- Brute Force: O((SumOfWeights - MaxWeight) * N)
    - `(SumOfWeights - MaxWeight)`: The range of capacities to iterate through. In the worst case, `SumOfWeights` can be up to `5 * 10^4 * 500 = 2.5 * 10^7`.
    - `N`: The length of the `weights` array (up to `5 * 10^4`), traversed in each call to `daysReq`.
    - This approach is too slow for the given constraints.
- Optimal (Binary Search): O(N * log(SumOfWeights - MaxWeight))
    - `log(SumOfWeights - MaxWeight)`: The number of iterations in the binary search. The search space for capacity is from `max(weights)` to `sum(weights)`.
    - `N`: The length of the `weights` array, traversed in each call to the `daysReq` helper function.
    - This is significantly more efficient and suitable for the given constraints.

SPACE COMPLEXITY:
- Both Brute Force and Optimal: O(1)
    - No additional data structures are used that scale with input size beyond a few variables.

TRADE-OFFS:
- The brute force approach is simple to understand but highly inefficient for large inputs.
- The optimal approach uses binary search to efficiently find the minimum capacity, making it feasible for the given constraints. The trade-off is a slightly more complex algorithm to implement.
"""

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Run detailed tests
    test_solution()
    
    # Example usage with default optimal approach
    weights_ex = [1,2,3,4,5,6,7,8,9,10]
    days_ex = 5
    result = solve_problem(weights_ex, days_ex) # Uses optimal by default
    print(f"Final Result (Optimal for [1..10], days=5): {result}")
    
    # Example: Test specific approach
    brute_result = solve_problem(weights_ex, days_ex, "brute")
    print(f"Brute Force Result for [1..10], days=5: {brute_result}")
