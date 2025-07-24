
from typing import List


"""
Problem: The Painter's Partition Problem
Platform: GeeksforGeeks
Difficulty: Hard
Topics: Array, Binary Search
LINK: https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1

Problem Statement:
Given an array `arr` representing lengths of `n` boards and an integer `k` representing the number of painters.
The task is to find the minimum time to paint all boards under the condition that any painter can only paint continuous sections of boards.
A painter takes 1 unit of time to paint 1 unit of a board.

Example:
Input: arr = [10, 20, 30, 40], k = 2
Output: 60
Explanation:
Here we can divide the boards into 2 equal-sized partitions
[10, 20, 30] and [40]. The painter who paints the first three boards takes 60 units of time.
The second painter takes 40 units of time. The maximum of these is 60, which is the minimum possible.
"""


# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: An array of board lengths `arr` and an integer `k` for the number of painters.
- Output: The minimum time required to paint all boards.
- Constraints:
  - 1 <= k <= n <= 10^5
  - 1 <= arr[i] <= 10^5
- Edge Cases:
  - If `k` is greater than `n`, it's impossible to assign each painter a board. (Although constraints say k<=n)
  - If there is only one painter, they must paint all boards. The result is the sum of all board lengths.

APPROACH:
This problem is another variation of the "Allocate Minimum Pages" and "Split Array Largest Sum" problems. We need to minimize a maximum value (the time taken by the painter who works the longest), which suggests using "Binary Search on Answer".

1.  **Define Search Space:** The answer (minimum time) must lie in a specific range.
    -   The minimum possible time is `max(arr)`. This happens if one painter is assigned the longest board, and we have enough painters for other boards. No allocation can take less time than painting the longest single board.
    -   The maximum possible time is `sum(arr)`. This happens when `k=1`, and one painter has to paint all the boards.
    -   So, our search space for the answer is `[max(arr), sum(arr)]`.

2.  **Binary Search:** We can binary search on this range of possible answers.
    -   For each `mid` value (which represents a potential maximum time any painter can work), we check if it's possible to paint all boards with `k` painters.

3.  **Check Feasibility (`is_possible` function):**
    -   This function will take `mid` (max allowed time) as input.
    -   It greedily assigns boards to painters. It counts how many painters are needed to paint all boards without any painter working for more than `mid` time.
    -   Iterate through the boards, summing up their lengths for the current painter. If adding the next board exceeds `mid`, we assign that board to a new painter and increment the painter count.
    -   If the number of painters required is less than or equal to `k`, then this `mid` is a possible solution.

4.  **Adjust Search Space:**
    -   If `is_possible(mid)` is true, it means we might be able to finish even faster. So, we try the left half of the search space: `high = mid - 1`.
    -   If `is_possible(mid)` is false, `mid` is too small. We need to allow more time for each painter. So, we try the right half: `low = mid + 1`.

5.  **Result:** The final answer will be `low` (or the variable storing the last valid `mid`), as we are trying to find the smallest possible maximum time.

TIME COMPLEXITY: O(N * log(sum(arr) - max(arr))) where N is the number of boards.
SPACE COMPLEXITY: O(1)
"""


# ==============================================================================
# HELPER FUNCTION
# ==============================================================================

def count_painters_for_max_time(arr: List[int], max_time_allowed: int) -> int:
    """
    Calculates the number of painters required to paint all boards
    such that no painter works for more than `max_time_allowed`.

    Args:
        arr: The array of board lengths.
        max_time_allowed: The maximum time any single painter can work.

    Returns:
        The total number of painters required for this allocation.
    """
    n = len(arr)
    time_for_current_painter = 0
    total_painters_needed = 1

    for i in range(n):
        if time_for_current_painter + arr[i] <= max_time_allowed:
            # Assign current board to the same painter
            time_for_current_painter += arr[i]
        else:
            # Start with a new painter
            total_painters_needed += 1
            # Assign the current board to the new painter
            time_for_current_painter = arr[i]

    return total_painters_needed


# ==============================================================================
# OPTIMAL APPROACH (BINARY SEARCH)
# ==============================================================================

def paintersPartition(arr: List[int], k: int) -> int:
    """
    OPTIMAL APPROACH - Binary Search on the Answer.

    Intuition:
    The range of possible answers `[max(arr), sum(arr)]` is monotonic.
    If we can paint all boards with a maximum time of `X` per painter, we can definitely
    do it with `X+1`. This monotonicity allows us to use binary search to find
    the minimum possible value for this maximum time.

    Approach:
    1. Define the search space: `low = max(arr)`, `high = sum(arr)`.
    2. Use a while loop: `while low <= high`.
    3. Calculate `mid = low + (high - low) // 2`. This `mid` is our potential answer.
    4. Check if an allocation is possible with `mid` as the max time using the helper function.
       - `painters_needed = count_painters_for_max_time(arr, mid)`
    5. If `painters_needed <= k`:
       - This `mid` is a possible answer. We try for an even smaller max time.
       - Store `mid` as a potential answer and search in the left half: `high = mid - 1`.
    6. If `painters_needed > k`:
       - `mid` is too small. We need to allow more time per painter.
       - Search in the right half: `low = mid + 1`.
    7. The loop terminates when `low` crosses `high`, and `low` will hold the minimum possible value.

    Time Complexity: O(N * log(sum(arr)))
    Space Complexity: O(1)
    """
    if not arr:
        return 0

    low = max(arr)
    high = sum(arr)
    ans = high

    while low <= high:
        mid = low + (high - low) // 2
        painters_needed = count_painters_for_max_time(arr, mid)

        if painters_needed <= k:
            # This is a potential answer, try for a smaller one
            ans = mid
            high = mid - 1
        else:
            # Need to allow more time, so increase the lower bound
            low = mid + 1

    return ans


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    k = 2
    print(f"Array: {arr}, Painters: {k}")
    
    # Optimal solution
    optimal_result = paintersPartition(arr, k)
    print(f"Optimal Result: {optimal_result}") # Expected: 60

    print("-" * 20)

    arr2 = [5, 10, 30, 20, 15]
    k2 = 3
    print(f"Array: {arr2}, Painters: {k2}")
    optimal_result2 = paintersPartition(arr2, k2)
    print(f"Optimal Result: {optimal_result2}") # Expected: 35
