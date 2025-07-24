
from typing import List


"""
Problem: Split Array Largest Sum
Platform: LeetCode
Difficulty: Hard
Topics: Array, Binary Search
LINK: https://leetcode.com/problems/split-array-largest-sum/

Problem Statement:
Given an array `nums` which consists of non-negative integers and an integer `k`, you can split the array into `k` non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these `k` subarrays.

Example:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""


# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: An array of non-negative integers `nums` and an integer `k`.
- Output: The minimum possible value for the largest sum among the `k` subarrays.
- Constraints:
  - 1 <= nums.length <= 1000
  - 0 <= nums[i] <= 10^6
  - 1 <= k <= min(50, nums.length)
- Edge Cases:
  - If `k` is 1, the answer is the sum of all elements in the array.
  - If `k` is equal to the length of the array, the answer is the maximum element in the array.

APPROACH:
This problem is identical in structure to the "Allocate Minimum Pages" problem. We are asked to minimize a maximum value, which points to "Binary Search on Answer".

1.  **Define Search Space:** The answer (minimized largest sum) must lie in a specific range.
    -   The minimum possible value for the largest sum is `max(nums)`. This occurs when we split the array into `n` subarrays, where `n` is the length of the array.
    -   The maximum possible value is `sum(nums)`. This occurs when `k=1`, and one subarray contains all the elements.
    -   So, our search space for the answer is `[max(nums), sum(nums)]`.

2.  **Binary Search:** We can binary search on this range of possible answers.
    -   For each `mid` value (which represents a potential largest sum of a subarray), we need to check if it's possible to split the array into `k` or fewer subarrays.

3.  **Check Feasibility (`is_possible` function):**
    -   This function will take `mid` (max allowed sum) as input.
    -   It greedily creates subarrays. It counts how many subarrays are needed to partition the entire array such that no subarray's sum exceeds `mid`.
    -   Iterate through the numbers, summing them up for the current subarray. If adding the next number exceeds `mid`, we start a new subarray with that number and increment the subarray count.
    -   If the number of subarrays required is less than or equal to `k`, then this `mid` is a possible solution.

4.  **Adjust Search Space:**
    -   If `is_possible(mid)` is true, it means we might be able to do even better with a smaller largest sum. So, we try the left half of the search space: `high = mid - 1`.
    -   If `is_possible(mid)` is false, `mid` is too small. We need to allow larger sums for each subarray. So, we try the right half: `low = mid + 1`.

5.  **Result:** The final answer will be `low` (or the variable storing the last valid `mid`), as we are trying to find the smallest possible maximum.

TIME COMPLEXITY: O(N * log(sum(nums) - max(nums))) where N is the number of elements.
SPACE COMPLEXITY: O(1)
"""


# ==============================================================================
# HELPER FUNCTION
# ==============================================================================

def count_subarrays_for_max_sum(nums: List[int], max_sum_allowed: int) -> int:
    """
    Calculates the number of subarrays required to partition the array
    such that no subarray's sum exceeds `max_sum_allowed`.

    Args:
        nums: The array of numbers.
        max_sum_allowed: The maximum sum any single subarray can have.

    Returns:
        The total number of subarrays required for this partition.
    """
    n = len(nums)
    sum_of_current_subarray = 0
    total_subarrays_needed = 1

    for i in range(n):
        if sum_of_current_subarray + nums[i] <= max_sum_allowed:
            # Add current element to the same subarray
            sum_of_current_subarray += nums[i]
        else:
            # Start with a new subarray
            total_subarrays_needed += 1
            # Add the current element to the new subarray
            sum_of_current_subarray = nums[i]

    return total_subarrays_needed


# ==============================================================================
# OPTIMAL APPROACH (BINARY SEARCH)
# ==============================================================================

def splitArray(nums: List[int], k: int) -> int:
    """
    OPTIMAL APPROACH - Binary Search on the Answer.

    Intuition:
    The range of possible answers `[max(nums), sum(nums)]` is monotonic.
    If we can split the array with a maximum sum of `X`, we can definitely
    do it with `X+1`. This monotonicity allows us to use binary search to find
    the minimum possible value for this largest sum.

    Approach:
    1. Define the search space: `low = max(nums)`, `high = sum(nums)`.
    2. Use a while loop: `while low <= high`.
    3. Calculate `mid = low + (high - low) // 2`. This `mid` is our potential answer.
    4. Check if a partition is possible with `mid` as the max sum using the helper function.
       - `subarrays_needed = count_subarrays_for_max_sum(nums, mid)`
    5. If `subarrays_needed <= k`:
       - This `mid` is a possible answer. We try for an even smaller max sum.
       - Store `mid` as a potential answer and search in the left half: `high = mid - 1`.
    6. If `subarrays_needed > k`:
       - `mid` is too small. We need to allow larger sums.
       - Search in the right half: `low = mid + 1`.
    7. The loop terminates when `low` crosses `high`, and `low` will hold the minimum possible value.

    Time Complexity: O(N * log(sum(nums)))
    Space Complexity: O(1)
    """
    if not nums:
        return 0

    low = max(nums)
    high = sum(nums)
    ans = high

    while low <= high:
        mid = low + (high - low) // 2
        subarrays_needed = count_subarrays_for_max_sum(nums, mid)

        if subarrays_needed <= k:
            # This is a potential answer, try for a smaller one
            ans = mid
            high = mid - 1
        else:
            # Need to allow a larger sum, so increase the lower bound
            low = mid + 1

    return ans


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    nums = [7, 2, 5, 10, 8]
    k = 2
    print(f"Array: {nums}, k: {k}")
    
    # Optimal solution
    optimal_result = splitArray(nums, k)
    print(f"Optimal Result: {optimal_result}") # Expected: 18

    print("-" * 20)

    nums2 = [1, 2, 3, 4, 5]
    k2 = 2
    print(f"Array: {nums2}, k: {k2}")
    optimal_result2 = splitArray(nums2, k2)
    print(f"Optimal Result: {optimal_result2}") # Expected: 9
