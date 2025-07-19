"""
Problem: Aggressive Cows
Platform: GeeksforGeeks, Coding Ninjas
Difficulty: Medium
Topics: Binary Search, Arrays
LINK: https://www.geeksforgeeks.org/problems/aggressive-cows/1
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: An array `stalls[]` of integers representing stall positions and an integer `k` (number of cows).
- Output: The largest possible minimum distance between any two cows.
- Constraints: `stalls.size()` is between 2 and 10^6, `stalls[i]` is between 0 and 10^8, `k` is between 2 and `stalls.size()`. The input array can be unsorted.
- Edge Cases: 
    - `k = 2`: The answer is simply the distance between the first and last stall after sorting.
    - `k = n`: The answer is the minimum distance between any two adjacent stalls after sorting.

APPROACH:
The problem asks to "maximize the minimum distance". This structure is a classic indicator for "Binary Search on Answer".
The range of possible answers for the minimum distance is from 1 to (max_stall_position - min_stall_position).
We can binary search on this answer range. For any given distance `d`, we can check if it's possible to place `k` cows with at least that distance `d` apart.

- If we can place `k` cows with distance `d`, it means `d` is a possible answer. We should try for an even larger minimum distance, so we search in the range `[d+1, high]`.
- If we cannot place `k` cows, the distance `d` is too large. We need to try a smaller distance, so we search in the range `[low, d-1]`.

This process continues until `low` crosses `high`. The last valid distance we found is our answer.
"""

from typing import List

# =============================================================================
# HELPER FUNCTION
# =============================================================================

def canWePlace(stalls: List[int], dist: int, cows: int) -> bool:
    """
    Checks if it's possible to place a given number of cows in the stalls
    such that the minimum distance between any two is at least `dist`.

    Intuition:
    - This is a greedy approach. To fit as many cows as possible for a given distance,
      we should place them as far to the left as possible.
    - Place the first cow at the first stall `stalls[0]`.
    - Iterate through the remaining stalls and place the next cow as soon as the
      distance from the last placed cow is >= `dist`.

    Args:
        stalls: Sorted list of stall positions.
        dist: The minimum required distance between cows.
        cows: The number of cows to place.

    Returns:
        True if it's possible to place all cows, False otherwise.
    
    Time Complexity: O(N), where N is the number of stalls.
    Space Complexity: O(1).
    """
    count_cows = 1
    last_cow_placed_at = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last_cow_placed_at >= dist:
            count_cows += 1
            last_cow_placed_at = stalls[i]
    
    return count_cows >= cows

# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def aggressiveCowsBrute(stalls: List[int], k: int) -> int:
    """
    BRUTE FORCE APPROACH

    Intuition:
    - The minimum possible answer is 1.
    - The maximum possible answer is the distance between the first and last stall.
    - We can check every possible integer distance from 1 up to the maximum possible distance.
    - For each distance `d`, we check if we can place `k` cows.
    - The largest distance `d` for which we can place the cows is our answer.

    Approach:
    1. Sort the `stalls` array.
    2. Iterate `d` from 1 to `stalls[n-1] - stalls[0]`.
    3. In each iteration, call `canWePlace(stalls, d, k)`.
    4. If `canWePlace` returns False, it means `d` is too large, and any distance greater than `d` will also be too large. So, the answer must be `d-1`.
    
    Args:
        stalls: List of stall positions.
        k: Number of cows.

    Returns:
        The largest minimum distance.

    Time Complexity: O(N*logN + (max_dist - min_dist) * N). Sorting takes O(N*logN). The loop runs up to `max_dist` times, and `canWePlace` is O(N). This can be very slow if the stall positions are far apart.
    Space Complexity: O(1) (if sorting is done in-place).
    """
    stalls.sort()
    n = len(stalls)
    limit = stalls[n - 1] - stalls[0]
    
    for dist in range(1, limit + 1):
        if not canWePlace(stalls, dist, k):
            return dist - 1
    return limit

# =============================================================================
# SOLUTION 2: OPTIMAL APPROACH (BINARY SEARCH)
# =============================================================================

def aggressiveCowsOp(stalls: List[int], k: int) -> int:
    """
    OPTIMAL APPROACH - Using Binary Search on the answer space.

    Intuition:
    - Instead of linearly checking every possible distance (1, 2, 3, ...), we can use binary search to find the optimal distance much faster.
    - The range of possible answers (distances) is monotonic. If we can place cows with distance `d`, we can also place them with any distance smaller than `d`. If we cannot place them with distance `d`, we surely cannot place them with any distance larger than `d`.
    - This monotonicity allows us to use binary search on the answer space.

    Approach:
    1. Sort the `stalls` array.
    2. Define the search space for the answer: `low = 1`, `high = stalls[n-1] - stalls[0]`.
    3. While `low <= high`:
        a. Calculate `mid = low + (high - low) // 2`.
        b. Check if it's possible to place `k` cows with a minimum distance of `mid` using `canWePlace(stalls, mid, k)`.
        c. If `canWePlace` is True, it means `mid` is a possible answer. We try for a larger distance, so we store `mid` and set `low = mid + 1`.
        d. If `canWePlace` is False, `mid` is too large. We must try a smaller distance, so we set `high = mid - 1`.
    4. The final answer is the last `mid` for which `canWePlace` was true, which is stored in `high` at the end of the loop.

    Args:
        stalls: List of stall positions.
        k: Number of cows.

    Returns:
        The largest minimum distance.

    Time Complexity: O(N*logN + N*log(max_dist)). Sorting is O(N*logN). The binary search performs log(max_dist) iterations, and each calls `canWePlace` which is O(N).
    Space Complexity: O(1) (if sorting is done in-place).
    """
    stalls.sort()
    n = len(stalls)
    low = 1
    high = stalls[n - 1] - stalls[0]
    ans = 0

    while low <= high:
        mid = low + (high - low) // 2
        if canWePlace(stalls, mid, k):
            ans = mid  # This distance is possible, try for a larger one
            low = mid + 1
        else:
            high = mid - 1 # This distance is not possible, try a smaller one
            
    return ans

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # TEST CASE 1
    stalls1 = [1, 2, 4, 8, 9]
    k1 = 3
    print(f"Test Case 1: Stalls={stalls1}, Cows={k1}")
    print("Brute Force Output:", aggressiveCowsBrute(stalls1, k1))
    print("Optimal Output:    ", aggressiveCowsOp(stalls1, k1))
    print("-" * 30)

    # TEST CASE 2
    stalls2 = [10, 1, 2, 7, 5]
    k2 = 3
    print(f"Test Case 2: Stalls={stalls2}, Cows={k2}")
    print("Brute Force Output:", aggressiveCowsBrute(stalls2, k2))
    print("Optimal Output:    ", aggressiveCowsOp(stalls2, k2))
    print("-" * 30)

    # TEST CASE 3
    stalls3 = [2, 12, 11, 3, 26, 7]
    k3 = 5
    print(f"Test Case 3: Stalls={stalls3}, Cows={k3}")
    print("Brute Force Output:", aggressiveCowsBrute(stalls3, k3))
    print("Optimal Output:    ", aggressiveCowsOp(stalls3, k3))
    print("-" * 30)
    
    # TEST CASE 4: k = 2
    stalls4 = [1, 10, 20, 30, 100]
    k4 = 2
    print(f"Test Case 4: Stalls={stalls4}, Cows={k4}")
    print("Brute Force Output:", aggressiveCowsBrute(stalls4, k4))
    print("Optimal Output:    ", aggressiveCowsOp(stalls4, k4))
    print("-" * 30)
