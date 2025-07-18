"""
Problem: You are given an integer array `bloomDay`, an integer `m` and an integer `k`. You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden. The garden consists of `n` flowers, the `ith` flower will bloom in the `bloomDay[i]` and then can be used in exactly one bouquet. Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible to make `m` bouquets return -1.
Platform: LeetCode (Commonly found on platforms like LeetCode)
Difficulty: Medium
Topics: Array, Binary Search, Greedy
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input:
    - `bloomDay`: An array of integers where `bloomDay[i]` is the day the `i`-th flower blooms.
    - `m`: The target number of bouquets to make.
    - `k`: The number of adjacent flowers required for one bouquet.
- Output: The minimum number of days required to make `m` bouquets. Return -1 if impossible.
- Constraints:
    - `bloomDay.length == n`
    - `1 <= n <= 10^5`
    - `1 <= bloomDay[i] <= 10^9`
    - `1 <= m <= 10^6`
    - `1 <= k <= n`
- Edge Cases:
    - If `m * k > n` (total flowers needed exceeds available flowers), it's impossible, return -1.
    - All flowers bloom on the same day.
    - `k = 1` (each bloomed flower can form a bouquet).

APPROACH:
The problem asks for the minimum number of days, which suggests a search problem. The `possible` function (described below) has a monotonic property: if `X` days are sufficient to make `m` bouquets, then any day `Y > X` will also be sufficient. This monotonicity allows us to use binary search on the range of possible days.

1.  **Check Feasibility:** First, determine if it's even possible to make `m` bouquets. If the total number of flowers required (`m * k`) is greater than the total number of available flowers (`n`), return -1.
2.  **Define Search Space:** The minimum possible day is the minimum value in `bloomDay`, and the maximum possible day is the maximum value in `bloomDay`. This range forms our search space for binary search.
3.  **Binary Search on Days:**
    *   For a given `mid` day, check if it's `possible` to make `m` bouquets.
    *   If `possible(mid)` is true, it means `mid` days might be the answer, or we might find an even smaller day. So, we try to search in the left half (`high = mid - 1`).
    *   If `possible(mid)` is false, it means `mid` days are not enough. We need more days, so we search in the right half (`low = mid + 1`).
4.  **Helper Function `possible(arr, day, m, k)`:** This function simulates the process for a given `day`. It iterates through the `bloomDay` array, counting consecutive flowers that have bloomed by `day`. For every `k` consecutive bloomed flowers, it forms a bouquet. It returns `True` if `m` or more bouquets can be formed, `False` otherwise.

TIME COMPLEXITY: O(N * log(MaxDay - MinDay))
SPACE COMPLEXITY: O(1)
"""

# ==============================================================================
# HELPER FUNCTION
# ==============================================================================

def possible(arr, day, m , k) -> bool:
    """
    Checks if it's possible to make 'm' bouquets by 'day'.

    Args:
        arr: The bloomDay array.
        day: The current day to check.
        m: The required number of bouquets.
        k: The number of adjacent flowers per bouquet.

    Returns:
        True if 'm' bouquets can be made, False otherwise.
    """
    n = len(arr)
    count = 0  # Counts consecutive bloomed flowers
    no_of_b = 0  # Counts total bouquets made

    for i in range(n):
        # If Flower is Bloomed by 'day'
        if arr[i] <= day:
            count += 1
        else:
            # If a flower hasn't bloomed, reset consecutive count
            # and add bouquets from previous consecutive bloomed flowers
            no_of_b += (count // k)
            count = 0
    
    # Add bouquets from any remaining consecutive bloomed flowers at the end
    no_of_b += count // k

    return no_of_b >= m

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def minDaysBrute(arr, m, k) -> int:
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - The minimum number of days must be one of the bloom days. We can iterate through all possible days from the earliest bloom day to the latest bloom day and check if `m` bouquets can be formed.
    - This approach works by checking every single day in the possible range, which is inefficient if the range of bloom days is very large.
    
    Approach:
    1.  Calculate `total_flowers_needed = m * k`. If `total_flowers_needed > n` (total flowers available), return -1 as it's impossible.
    2.  Find the minimum (`minEl`) and maximum (`maxEl`) bloom days in the `arr`. These define the search range for days.
    3.  Iterate `day` from `minEl` to `maxEl` (inclusive).
    4.  For each `day`, call the `possible` helper function.
    5.  If `possible(arr, day, m, k)` returns `True`, then `day` is the first day in this linear scan that satisfies the condition, so it's the minimum. Return `day`.
    6.  If the loop completes without finding a suitable day, it implies no day in the range works, so return -1. (This case should ideally be covered by the initial `m * k > n` check if the problem guarantees a solution exists within the range if `m * k <= n`).
    
    Args:
        arr: The bloomDay array.
        m: The required number of bouquets.
        k: The number of adjacent flowers per bouquet.
    
    Returns:
        The minimum number of days, or -1 if impossible.
    
    Time Complexity: O((MaxDay - MinDay + 1) * N)
        - `(MaxDay - MinDay + 1)` is the range of days we iterate through. In the worst case, `MaxDay` can be `10^9`, making this very slow.
        - `N` is the length of `bloomDay`, due to the `possible` function iterating through the array.
    Space Complexity: O(1)
    """
    n = len(arr)
    if m * k > n:
        return -1
    
    minEl = min(arr)
    maxEl = max(arr)

    for day in range(minEl, maxEl + 1):
        if possible(arr, day, m, k):
            return day
        
    return -1

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (BINARY SEARCH ON ANSWER)
# ==============================================================================

def minDaysOp(arr, m , k) -> int:
    """
    OPTIMAL APPROACH - Most efficient solution possible using Binary Search.
    
    Intuition:
    - The problem asks for the minimum value (minimum days) that satisfies a certain condition (can make `m` bouquets). This is a classic scenario for binary search on the answer space.
    - The `possible` function exhibits monotonicity: if `X` days are enough, then `X+1` days are also enough. This property allows binary search.
    
    Approach:
    1.  Calculate `total_flowers_needed = m * k`. If `total_flowers_needed > n` (total flowers available), return -1 as it's impossible.
    2.  Define the search space for the binary search:
        - `low`: The minimum possible day is `min(arr)`.
        - `high`: The maximum possible day is `max(arr)`.
    3.  Initialize `ans = -1` (or `high` as a potential answer, depending on binary search template).
    4.  Perform binary search within the `[low, high]` range:
        - Calculate `mid = low + (high - low) // 2`.
        - Call the `possible` helper function: `is_possible = possible(arr, mid, m, k)`.
        - If `is_possible` is `True`: It means `mid` days are sufficient. This `mid` could be our answer, or there might be an even smaller day that also works. So, we store `mid` as a potential answer and try to find a smaller day by setting `high = mid - 1`.
        - If `is_possible` is `False`: It means `mid` days are not enough. We need more days. So, we discard `mid` and the left half (since they would also be insufficient) and narrow our search to the right half by setting `low = mid + 1`.
    5.  The loop continues until `low > high`. At the end, `low` will hold the minimum number of days for which `possible` is `True`. This is because `low` always moves to the first "true" boundary, while `high` moves to the last "false" boundary.
    
    Args:
        arr: The bloomDay array.
        m: The required number of bouquets.
        k: The number of adjacent flowers per bouquet.
    
    Returns:
        The minimum number of days, or -1 if impossible.
    
    Time Complexity: O(N * log(MaxDay - MinDay))
        - `log(MaxDay - MinDay)` comes from the binary search iterations.
        - `N` comes from the `possible` function, which iterates through the `bloomDay` array.
    Space Complexity: O(1)
    """
    n = len(arr)
    if m * k > n:
        return -1
        
    low = min(arr)
    high = max(arr)
    ans = -1 # Initialize ans, though 'low' will hold the answer at the end

    while low <= high:
        mid = low + (high - low) // 2

        if possible(arr, mid, m, k):
            ans = mid # Store potential answer
            high = mid - 1 # Try to find a smaller day
        else:
            low = mid + 1 # Need more days

    return low # 'low' will be the first day for which 'possible' is True

"""
# AI please Explain why in above Optimal Solution ans is low
# b/c low start from the range of not possible senarios and high start from possible senerios
# at the end low will reach to min possible senarios and high will reach max not possible senarios
# this concept can be applied many places I guess, please explain this concept very articulate manner
# plus if possible make some diagrams etc etc in python comments only.

Explanation of Binary Search Logic (Why `low` is the answer):

This specific binary search pattern is used to find the *minimum value `X`* for which a certain `condition(X)` is `True`.

Let's define our `condition(day)` as `possible(arr, day, m, k)`. We are looking for the smallest `day` such that `possible(arr, day, m, k)` is `True`.

The search space is `[low, high]`.
- `low` represents the lower bound of our search space.
- `high` represents the upper bound of our search space.

Inside the `while low <= high` loop:
1.  We calculate `mid = low + (high - low) // 2`.
2.  We check `if possible(arr, mid, m, k):`
    *   **If `True`:** This means `mid` days are sufficient. Since we are looking for the *minimum* such day, `mid` is a *potential* answer. We store it (e.g., in `ans = mid`) and then try to find an even smaller day that also satisfies the condition. To do this, we narrow our search to the left half by setting `high = mid - 1`.
        ```
        [ F F F T T T T ]  <- possible(day)
          ^       ^
          low     mid (possible)
                  ans = mid
                  high = mid - 1
        Search next in [low, mid-1]
        ```
    *   **If `False`:** This means `mid` days are *not* sufficient. We need more days. So, we discard `mid` and everything to its left (since they would also be insufficient) and narrow our search to the right half by setting `low = mid + 1`.
        ```
        [ F F F T T T T ]  <- possible(day)
          ^   ^
          low mid (not possible)
              low = mid + 1
        Search next in [mid+1, high]
        ```

**How `low` becomes the answer:**

The loop continues until `low > high`. 
When this condition is met, 
`low` will point to the first element that satisfies the `possible` condition, 
and `high` will point to the last element that *does not* satisfy the `possible` condition.

Consider the moment just before the loop terminates:
-   `low` is pointing to a value `X`.
-   `high` is pointing to a value `X-1`.
-   At this point, `possible(arr, X-1, m, k)` was `False` (which caused `low` to become `X`).
-   And `possible(arr, X, m, k)` was `True` (which caused `high` to become `X-1`).

Therefore, `low` ends up being the smallest `day` for which `possible(arr, day, m, k)` is `True`.

Example Trace: `bloomDay = [1,10,3,10,2], m = 3, k = 1`
Search space: `[1, 10]` (MinDay=1, MaxDay=10)

| Iteration   | low | high | mid | possible(mid)  | Action                      | ans |
|-------------|-----|------|-----|----------------|-----------------------------|-----|
| Initial     | 1   | 10   | -   | -              | -                           | -1  |
| 1           | 1   | 10   | 5   | True           | ans = 5, high = 4           | 5   |
| 2           | 1   | 4    | 2   | False          | low = 3                     | 5   |
| 3           | 3   | 4    | 3   | True           | ans = 3, high = 2           | 3   |
| Loop ends   | 3   | 2    | -   | -              | low > high (stop loop)      | 3   |

Final `low` is 3, which is the correct minimum day.
"""

# ==============================================================================
# MAIN SOLUTION FUNCTION
# ==============================================================================

def solve_problem(bloomDay, m, k, approach="optimal"):
    """
    Main solution function that calls the appropriate approach.
    
    Args:
        bloomDay: The bloomDay array.
        m: The required number of bouquets.
        k: The number of adjacent flowers per bouquet.
        approach: "brute" or "optimal" (default)
    
    Returns:
        The minimum number of days, or -1 if impossible.
    """
    
    if approach == "brute":
        return minDaysBrute(bloomDay, m, k)
    elif approach == "optimal":
        return minDaysOp(bloomDay, m, k)
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
    bloomDay1 = [1,10,3,10,2]
    m1 = 3
    k1 = 1
    expected1 = 3
    
    print("Test 1 - Basic example:")
    for approach in ["brute", "optimal"]:
        result1 = solve_problem(bloomDay1, m1, k1, approach)
        assert result1 == expected1, f"Test 1 {approach} failed: expected {expected1}, got {result1}"
        print(f"✓ {approach.capitalize()} approach passed")
    
    # TEST CASE 2: Example from problem description (impossible)
    bloomDay2 = [1,10,3,10,2]
    m2 = 3
    k2 = 2
    expected2 = -1
    
    print("Test 2 - Impossible case:")
    for approach in ["brute", "optimal"]:
        result2 = solve_problem(bloomDay2, m2, k2, approach)
        assert result2 == expected2, f"Test 2 {approach} failed: expected {expected2}, got {result2}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 3: Example from problem description
    bloomDay3 = [7,7,7,7,12,7,7]
    m3 = 2
    k3 = 3
    expected3 = 12
    
    print("Test 3 - Another example:")
    for approach in ["brute", "optimal"]:
        result3 = solve_problem(bloomDay3, m3, k3, approach)
        assert result3 == expected3, f"Test 3 {approach} failed: expected {expected3}, got {result3}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 4: All flowers bloom on the same day
    bloomDay4 = [5,5,5,5,5,5,5,5,5,5]
    m4 = 2
    k4 = 3
    expected4 = 5
    
    print("Test 4 - All flowers bloom same day:")
    for approach in ["brute", "optimal"]:
        result4 = solve_problem(bloomDay4, m4, k4, approach)
        assert result4 == expected4, f"Test 4 {approach} failed: expected {expected4}, got {result4}"
        print(f"✓ {approach.capitalize()} approach passed")

    # TEST CASE 5: Large input performance test (only for optimal)
    print("Test 5 - Performance comparison (Optimal only):")
    large_bloomDay = [i for i in range(1, 100001)] # 1 to 10^5
    large_m = 1000
    large_k = 10
    # Expected: 1000 * 10 = 10000 flowers needed.
    # The 10000th flower blooms on day 10000.
    large_expected = 10000 
    
    import time
    # Brute force would be too slow for this, so only test optimal
    start_time = time.time()
    result_optimal = solve_problem(large_bloomDay, large_m, large_k, "optimal")
    end_time = time.time()
    assert result_optimal == large_expected, f"Test 5 optimal failed: expected {large_expected}, got {result_optimal}"
    print(f"Optimal approach: {end_time - start_time:.4f} seconds")
    print(f"✓ Optimal approach passed for large input")
    
    print("🎉 All tests passed!")

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

TIME COMPLEXITY:
- Brute Force: O((MaxDay - MinDay + 1) * N)
    - `MaxDay - MinDay + 1`: The range of days to iterate through. In the worst case, `bloomDay[i]` can be up to `10^9`, making this range very large.
    - `N`: The length of the `bloomDay` array, which is traversed in the `possible` helper function.
- Optimal (Binary Search): O(N * log(MaxDay - MinDay))
    - `log(MaxDay - MinDay)`: The number of iterations in the binary search. The search space is the range of days.
    - `N`: The length of the `bloomDay` array, traversed in each call to the `possible` helper function.
    - This is significantly more efficient than brute force, especially when the range of bloom days is large.

SPACE COMPLEXITY:
- Both Brute Force and Optimal: O(1)
    - No additional data structures are used that scale with input size beyond a few variables.

TRADE-OFFS:
- The brute force approach is simple to understand but impractical for large bloom day ranges due to its linear scan of days.
- The optimal approach uses binary search to efficiently narrow down the search space for days, making it suitable for large bloom day values. 
The trade-off is a slightly more complex algorithm to implement due to the binary search logic.
"""

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Run detailed tests
    test_solution()
    
    # Example usage with default optimal approach
    arr_ex = [1,10,3,10,2]
    m_ex = 3
    k_ex = 1
    result = solve_problem(arr_ex, m_ex, k_ex) # Uses optimal by default
    print(f"Final Result (Optimal for [1,10,3,10,2], m=3, k=1): {result}")
    
    # Example: Test specific approach
    brute_result = solve_problem(arr_ex, m_ex, k_ex, "brute")
    print(f"Brute Force Result for [1,10,3,10,2], m=3, k=1: {brute_result}")