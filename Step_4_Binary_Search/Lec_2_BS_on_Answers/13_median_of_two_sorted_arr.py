"""
Problem: Median of Two Sorted Arrays
Platform: LeetCode
Difficulty: Hard
Topics: Array, Binary Search
LINK: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: Two sorted arrays, `nums1` (size m) and `nums2` (size n).
- Output: The median of the combined, sorted array.
- Constraints:
  - The final time complexity must be O(log(m+n)).
  - `m` and `n` are between 0 and 1000.
  - `m + n` is between 1 and 2000.
- Median Definition:
  - If the total number of elements `(m+n)` is odd, the median is the single middle element.
  - If the total number of elements is even, the median is the average of the two middle elements.

APPROACH:
1.  **Brute Force:** Merge the two sorted arrays into a third array. Then find the median from this merged array based on its length.
2.  **Better:** Instead of creating a whole new array, we can simulate the merge process. We only need to keep track of the elements around the median position. We can use a counter and iterate until we reach the middle element(s).
3.  **Optimal:** The O(log(m+n)) requirement is a huge hint to use Binary Search. The idea is to partition both arrays into a "left part" and a "right part". We want to make a partition such that all elements in the combined left parts are less than or equal to all elements in the combined right parts, and the number of elements in the combined left part is equal to (or one more than) the combined right part. This is a very clever application of binary search on the possible partition positions.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def medianTwoArr(arr1, arr2):
    """
    BRUTE FORCE APPROACH - Merge and Find Median.

    Intuition:
    The most straightforward way to find the median of two sorted arrays is to first merge them into a single sorted array. Once we have this combined sorted array, finding the median is a simple calculation based on the array's length.

    Approach:
    1. Create a new array `arr3` to store the merged elements.
    2. Use two pointers, `i` for `arr1` and `j` for `arr2`.
    3. Compare `arr1[i]` and `arr2[j]` and append the smaller element to `arr3`. Increment the corresponding pointer.
    4. Continue until one of the arrays is fully traversed.
    5. Append the remaining elements from the other array to `arr3`.
    6. Calculate the total length `n = len(arr3)`.
    7. If `n` is odd, the median is `arr3[n//2]`.
    8. If `n` is even, the median is `(arr3[n//2 - 1] + arr3[n//2]) / 2`.

    Time Complexity: O(n1 + n2) - We have to iterate through both arrays once to merge them.
    Space Complexity: O(n1 + n2) - We create a new array to store all elements.
    """
    n1 = len(arr1)
    n2 = len(arr2)
    i, j = 0, 0
    arr3 = []

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < n1:
        arr3.append(arr1[i])
        i += 1

    while j < n2:
        arr3.append(arr2[j])
        j += 1

    n = n1 + n2

    if n % 2 == 0:
        return (arr3[n // 2] + arr3[(n // 2) - 1]) / 2.0
    else:
        return float(arr3[n // 2])

# ==============================================================================
# SOLUTION 2: BETTER APPROACH
# ==============================================================================

def medianTwoArrBetter(arr1, arr2):
    """
    BETTER APPROACH - Optimized Merge without Extra Space.

    Intuition:
    We don't need to store the entire merged array. We only need the element(s) at the median position(s). We can find these by keeping a counter while virtually merging the arrays.

    Approach:
    1. Get the total length `n = n1 + n2`.
    2. Identify the indices of the median elements. For an even `n`, they are `n//2 - 1` and `n//2`. For an odd `n`, it's `n//2`.
    3. Use two pointers, `i` for `arr1` and `j` for `arr2`, and a counter `cnt`.
    4. Iterate through the arrays as if merging them. In each step, increment `cnt`.
    5. When `cnt` reaches the median index (or indices), store the corresponding element(s).
    6. If `n` is odd, the element at index `n//2` is the median.
    7. If `n` is even, the average of elements at `n//2 - 1` and `n//2` is the median.

    Time Complexity: O(n1 + n2) - We still need to iterate up to the median element, which can be at the end in the worst case.
    Space Complexity: O(1) - We only use a few variables to store indices and values, not a whole new array.
    """
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    median_idx = n // 2
    prev_median_idx = median_idx - 1
    el_at_prev_median_idx = -1
    el_at_median_idx = -1
    i, j, cnt = 0, 0, 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if cnt == prev_median_idx: el_at_prev_median_idx = arr1[i]
            if cnt == median_idx: el_at_median_idx = arr1[i]
            i += 1
        else:
            if cnt == prev_median_idx: el_at_prev_median_idx = arr2[j]
            if cnt == median_idx: el_at_median_idx = arr2[j]
            j += 1
        cnt += 1

    while i < n1:
        if cnt == prev_median_idx: el_at_prev_median_idx = arr1[i]
        if cnt == median_idx: el_at_median_idx = arr1[i]
        i += 1
        cnt += 1

    while j < n2:
        if cnt == prev_median_idx: el_at_prev_median_idx = arr2[j]
        if cnt == median_idx: el_at_median_idx = arr2[j]
        j += 1
        cnt += 1

    if n % 2 == 0:
        return (el_at_prev_median_idx + el_at_median_idx) / 2.0
    else:
        return float(el_at_median_idx)

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (Binary Search)
# ==============================================================================

def medianTwoArrOp(a, b):
    """
    OPTIMAL APPROACH - Binary Search on Partitions.

    Intuition:
    The core idea is to partition the combined array into two halves, a 'left part' and a 'right part', where the number of elements is equal (or the left is one larger for odd totals). The median is then determined by the max element on the left and the min element on the right.
    We can achieve this by partitioning both arrays and ensuring `max(left_part) <= min(right_part)`.
    We perform a binary search on the smaller array to find the correct partition point (`cut1`). The partition point in the second array (`cut2`) is then determined automatically.

    Approach:
    1. Ensure the binary search is performed on the smaller array to optimize complexity. If `len(a) > len(b)`, swap them.
    2. The total number of elements needed in the combined left part is `left_len = (n1 + n2 + 1) // 2`.
    3. Binary search in the smaller array (let's say `a`) for a partition point `cut1`. The search space is `[0, n1]`.
    4. For a given `cut1`, the partition point in `b` is `cut2 = left_len - cut1`.
    5. From these cuts, determine the four boundary elements:
       - `l1`: max element of `a`'s left part (`a[cut1-1]`)
       - `r1`: min element of `a`'s right part (`a[cut1]`)
       - `l2`: max element of `b`'s left part (`b[cut2-1]`)
       - `r2`: min element of `b`'s right part (`b[cut2]`)
       (Handle edge cases where a cut is 0 or n).
    6. Check if the partition is correct: `l1 <= r2` and `l2 <= r1`.
       - If it is, we've found the median. If total length is odd, median is `max(l1, l2)`. If even, it's `(max(l1, l2) + min(r1, r2)) / 2`.
       - If `l1 > r2`, our `cut1` is too large, so we need to move left: `high = cut1 - 1`.
       - If `l2 > r1`, our `cut1` is too small, so we need to move right: `low = cut1 + 1`.

    Time Complexity: O(log(min(n1, n2))) - Binary search is on the smaller array.
    Space Complexity: O(1)
    """
    n1 = len(a)
    n2 = len(b)

    if n1 > n2:
        return medianTwoArrOp(b, a)

    n = n1 + n2
    low = 0
    high = n1
    no_of_el_need_on_left = (n1 + n2 + 1) // 2

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = no_of_el_need_on_left - cut1

        l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")

        if cut1 < n1: r1 = a[cut1]
        if cut2 < n2: r2 = b[cut2]
        if cut1 > 0: l1 = a[cut1 - 1]
        if cut2 > 0: l2 = b[cut2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return float(max(l1, l2))
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1

    return 0.0 # Should not be reached if inputs are valid

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    arr1 = [1, 2]
    arr2 = [3, 4]
    print("--- Test Case 1 ---")
    print(f"Arrays: {arr1}, {arr2}")
    print(f"Brute Force Result: {medianTwoArr(arr1, arr2)}")
    print(f"Better Result: {medianTwoArrBetter(arr1, arr2)}")
    print(f"Optimal Result: {medianTwoArrOp(arr1, arr2)}")
    print("\n")

    arr3 = [1, 3]
    arr4 = [2]
    print("--- Test Case 2 ---")
    print(f"Arrays: {arr3}, {arr4}")
    print(f"Brute Force Result: {medianTwoArr(arr3, arr4)}")
    print(f"Better Result: {medianTwoArrBetter(arr3, arr4)}")
    print(f"Optimal Result: {medianTwoArrOp(arr3, arr4)}")