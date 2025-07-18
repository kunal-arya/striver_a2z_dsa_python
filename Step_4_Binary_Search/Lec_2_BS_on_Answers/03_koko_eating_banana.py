"""
DSA Problem Solution: Koko Eating Bananas
=========================================

Problem: Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Platform: LeetCode
Difficulty: Medium
Topics: Binary Search, Array
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: 
    - `piles`: A list of integers representing the number of bananas in each pile.
    - `h`: An integer representing the total hours Koko has to eat all the bananas.
- Output: The minimum integer `k` (eating speed) such that Koko can eat all bananas within `h` hours.
- Constraints:
    - `1 <= piles.length <= 10^4`
    - `piles.length <= h <= 10^9`
    - `1 <= piles[i] <= 10^9`
- Edge Cases:
    - The number of piles is equal to `h`. In this case, the minimum speed `k` must be the size of the largest pile.
    - The eating speed `k` can range from 1 to the maximum number of bananas in any single pile.

APPROACH:
The problem asks for the *minimum* speed `k`. This suggests that we are looking for an optimal value within a range of possible speeds. The possible speeds for `k` are from 1 (eating one banana per hour) to `max(piles)` (eating the largest pile in one hour). This range is sorted, which makes binary search an ideal approach.

1.  **Brute Force:** We can check every possible speed `k` from 1 up to a reasonable upper bound (like the maximum pile size). For each speed, we calculate the total time required to eat all bananas. The first speed `k` that allows Koko to finish within `h` hours is our answer.
2.  **Optimal (Binary Search):** Instead of a linear scan, we can use binary search on the range of possible speeds `[1, max(piles)]`. For a given speed `mid`, we calculate the total time.
    - If the time is within the `h` limit, it means `mid` is a possible speed, but there might be an even smaller speed that also works. So, we try to find a better answer in the lower half of the search space: `high = mid - 1`.
    - If the time exceeds `h`, the speed `mid` is too slow. We need to increase the speed, so we search in the upper half: `low = mid + 1`.
"""

# ==============================================================================
# HELPER FUNCTION
# ==============================================================================
import math

def timeToEat(arr, hourly):
    """
    Helper function to calculate the total time required to eat all bananas at a given speed.
    
    Args:
        arr (list[int]): The piles of bananas.
        hourly (int): The eating speed (bananas per hour).
    
    Returns:
        int: The total hours required.
    """
    totalTime = 0
    for i in range(len(arr)):
        totalTime += math.ceil(arr[i] / hourly)
    return totalTime

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def kokoBananaBrute(arr, hours):
    """
    BRUTE FORCE APPROACH - Linearly search for the minimum speed.
    
    Intuition:
    - The minimum possible speed is 1.
    - The maximum necessary speed is the size of the largest pile.
    - We can test each speed from 1 up to `max(arr)` and find the first one that works.
    
    Approach:
    1. Find the maximum pile size, `maxEl`. This is the upper bound for our search.
    2. Iterate from `hourlyRate = 1` to `maxEl`.
    3. For each `hourlyRate`, calculate the total time it would take to eat all bananas.
    4. If the `total_time` is less than or equal to the available `hours`, this is the minimum speed, so we return it.
    5. If the loop completes without finding a suitable speed, it means no solution is possible (though the problem constraints guarantee a solution).
    
    Args:
        arr (list[int]): The piles of bananas.
        hours (int): The total hours available.
    
    Returns:
        int: The minimum eating speed, or -1 if no solution is found.
    
    Time Complexity: O(max(piles) * len(piles)) - We iterate up to `max(piles)`, and for each speed, we iterate through all `len(piles)`.
    Space Complexity: O(1) - No extra space is used besides a few variables.
    """
    maxEl = max(arr)

    for hourlyRate in range(1, maxEl + 1):
        total_time = timeToEat(arr, hourlyRate)
        if total_time <= hours:
            return hourlyRate
    
    return -1

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH (BINARY SEARCH)
# ==============================================================================

def kokoBananaOp(arr, hours):
    """
    OPTIMAL APPROACH - Using Binary Search to find the minimum speed.
    
    Intuition:
    - The range of possible speeds is sorted, from `[1, max(piles)]`.
    - We can use binary search to efficiently find the minimum valid speed.
    - If a speed `k` works, any speed `k' > k` will also work. This monotonic property is key for binary search.
    
    Approach:
    1. Set up the search space for the speed `k`: `low = 1`, `high = max(piles)`.
    2. While `low <= high`:
        a. Calculate the middle speed: `mid = low + (high - low) // 2`.
        b. Calculate the total hours required to eat all bananas with speed `mid`.
        c. If `total_hours <= hours`, it means `mid` is a potential answer. We store it and try to find an even smaller speed in the left half: `ans = mid`, `high = mid - 1`.
        d. If `total_hours > hours`, the speed `mid` is too slow. We must increase it, so we search in the right half: `low = mid + 1`.
    3. The `ans` variable will hold the minimum speed found.
    
    Args:
        arr (list[int]): The piles of bananas.
        hours (int): The total hours available.
    
    Returns:
        int: The minimum eating speed.
    
    Time Complexity: O(log(max(piles)) * len(piles)) - Binary search runs in O(log(max(piles))) iterations, and in each, we calculate the time which takes O(len(piles)).
    Space Complexity: O(1) - Constant extra space.
    """
    maxEl = max(arr)
    low = 1
    high = maxEl

    while low <= high:
        mid = low + (high - low) // 2
        
        if mid == 0:
            low = mid + 1
            continue

        total_hours = timeToEat(arr, mid)

        if total_hours <= hours:
            high = mid - 1
        else:
            low = mid + 1
    
    return low

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    arr = [3, 6, 7, 11]
    h = 8
    
    print(f"Piles: {arr}, Hours: {h}")
    
    print("\n--- Brute Force ---")
    print(f"Minimum speed: {kokoBananaBrute(arr,h)}")

    print("\n--- Optimal (Binary Search) ---")
    print(f"Minimum speed: {kokoBananaOp(arr,h)}")