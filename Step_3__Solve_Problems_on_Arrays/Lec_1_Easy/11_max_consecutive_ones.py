from typing import List

# -------------------------------------------------------
# PROBLEM: MAXIMUM CONSECUTIVE ONES
# -------------------------------------------------------
# Given a binary array (only 0s and 1s), return the length of the
# longest sequence of consecutive 1s.
#
# Example:
#   Input:  [0,0,1,1,1,0,1,1,0,1]
#   Output: 3
#   (The longest streak of 1s is from index 2 to 4: [1,1,1])
#
# Constraints:
# - Only 0 and 1 are present in the array
# - Must be solved in a single pass (O(n) time)

# -------------------------------------------------------
# INTUITION:
# -------------------------------------------------------
# - Traverse the array while maintaining a counter (`count`) for the
#   current streak of 1s.
# - Whenever we see a 1 → increase `count`.
# - Whenever we see a 0 → reset `count` to 0 (streak broken).
# - At every step, track the maximum of all `count` values in `res`.

# -------------------------------------------------------
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)
# -------------------------------------------------------

def max_consecutive_ones(arr: List[int]) -> int:
    count, res = 0, 0  # count: current streak, res: max streak

    for num in arr:
        if num == 1:
            count += 1
            res = max(res, count)  # update max streak
        else:
            count = 0  # reset if 0 encountered
    
    return res

# -------------------------------------------------------
# VISUAL DRY RUN:
# -------------------------------------------------------
# Input: [0, 0, 1, 1, 1, 0, 1, 1, 0, 1]
#
# Step-by-step:
# i = 0 → 0 → count = 0, res = 0
# i = 1 → 0 → count = 0, res = 0
# i = 2 → 1 → count = 1, res = 1
# i = 3 → 1 → count = 2, res = 2
# i = 4 → 1 → count = 3, res = 3
# i = 5 → 0 → count
