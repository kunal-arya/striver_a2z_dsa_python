"""
Problem: Given an array of integers, move all the zeroes to the end of it 
         while maintaining the relative order of the non-zero elements.
         Note that you must do this in-place without making a copy of the array.

Platform: LeetCode
Difficulty: Easy
Topics: Array, Two Pointers
LINK: https://leetcode.com/problems/move-zeroes/
"""
from typing import List

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A list of integers `nums`.
- Output: The list `nums` modified in-place.
- Constraints:
    - Must be done in-place (no extra array).
    - The relative order of non-zero elements must be preserved.
- Edge Cases:
    - Empty array: `[]` -> `[]`
    - Array with all zeros: `[0, 0, 0]` -> `[0, 0, 0]`
    - Array with no zeros: `[1, 2, 3]` -> `[1, 2, 3]`
    - Array with mixed elements: `[0, 1, 0, 3, 12]` -> `[1, 3, 12, 0, 0]`

APPROACH:
- We need a way to shift non-zero elements to the front while keeping their order.
- A brute-force method might use extra space, which is not allowed.
- An optimal in-place solution can be achieved using a two-pointer technique.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH (Not in-place)
# ==============================================================================

def moveZeroesBrute(nums: List[int]) -> None:
    """
    BRUTE FORCE APPROACH - Uses an auxiliary array.
    
    Intuition:
    - Create a temporary list to store all non-zero elements from the original array.
    - This preserves their relative order.
    - Then, overwrite the original array with the elements from the temporary list.
    - Finally, fill the remaining spots in the original array with zeros.
    
    Approach:
    1. Create an empty list `temp`.
    2. Iterate through `nums` and append every non-zero element to `temp`.
    3. Get the number of non-zero elements, `nz_count = len(temp)`.
    4. Iterate from `0` to `nz_count - 1`, and copy `temp[i]` to `nums[i]`.
    5. Iterate from `nz_count` to the end of `nums`, and set `nums[i] = 0`.
    
    Args:
        nums: The list of integers to modify.
    
    Returns:
        None. The list is modified in-place (conceptually, though this implementation isn't truly in-place due to `temp`).
    
    Time Complexity: O(N) - We iterate through the array three times in total (once to build temp, once to copy back, once to fill zeros). This is O(N) + O(N) = O(2N) ~ O(N).
    Space Complexity: O(N) - In the worst case (no zeros), the `temp` array will be the same size as the input array. If we only count non-zero elements, it's O(X) where X is the count of non-zeros.
    """
    
    # STEP 1: Store non-zero elements in a temporary list
    temp = []
    for x in nums:
        if x != 0:
            temp.append(x)
    
    # STEP 2: Place non-zero elements back into the original array
    nz_count = len(temp)
    for i in range(nz_count):
        nums[i] = temp[i]
        
    # STEP 3: Fill the remaining part of the array with zeros
    for i in range(nz_count, len(nums)):
        nums[i] = 0

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH (Two Pointers)
# ==============================================================================

def moveZeroesOp(nums: List[int]) -> None:
    """
    OPTIMAL APPROACH - In-place modification using two pointers.
    
    Intuition:
    - The core idea is to place the next non-zero element at the first available "zero" spot.
    - We can use a pointer `j` to keep track of the position of the last found zero.
    - We iterate through the array with another pointer `i`. When we find a non-zero element at `nums[i]`, we swap it with the zero at `nums[j]`.
    
    Approach:
    1. Find the index of the first zero in the array. Let this be `j`.
    2. If no zero is found, the array is already in the desired state, so we can return.
    3. Iterate through the array with a pointer `i`, starting from `j + 1`.
    4. If `nums[i]` is a non-zero element, it means we have found a non-zero element that appears after a zero.
    5. Swap `nums[i]` with `nums[j]`.
    6. Increment `j` to point to the next position that should receive a non-zero element.
    
    Args:
        nums: The list of integers to modify in-place.
    
    Returns:
        None. The list is modified in-place.
    
    Time Complexity: O(N) - We traverse the array at most twice (once to find the first zero, and once to swap).
    Space Complexity: O(1) - The modification is done in-place with no extra space.
    """
    
    # STEP 1: Find the first zero. `j` will be its index.
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
            
    # If no zero is found, the array is already sorted.
    if j == -1:
        return
        
    # STEP 2: Iterate from j+1. If a non-zero element is found, swap it with the element at j.
    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            # After the swap, `nums[j]` is now a non-zero element and is in its correct final place.
            # We increment `j` to mark the next position that needs to be filled with a non-zero element.
            # This new `j` will always point to a zero.
            #
            # Why is this guaranteed?
            # Let's say our array is `[..., 0, 0, ..., non-zero, ...]`
            #                      ^j         ^i
            # The elements between j and i (`nums[j+1]...nums[i-1]`) must all be zeros.
            # If any of them were non-zero, the `i` loop would have stopped there earlier and swapped it.
            #
            # When we swap `nums[i]` and `nums[j]`, the zero from `nums[j]` moves to `nums[i]`.
            # The array becomes `[..., non-zero, 0, ..., 0, ...]`
            #                         ^j
            # By incrementing `j`, we move our boundary to the next position (`j+1`), which is guaranteed
            # to be one of the zeros from the `j` to `i` block.
            j += 1

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Test Case 1
    arr1_brute = [0, 1, 0, 3, 12]
    print(f"Original Array 1: {arr1_brute}")
    moveZeroesBrute(arr1_brute)
    print(f"Brute Force Result: {arr1_brute}")
    print("-" * 20)

    # Test Case 2
    arr1_op = [0, 1, 0, 3, 12]
    print(f"Original Array 2: {arr1_op}")
    moveZeroesOp(arr1_op)
    print(f"Optimal Result:     {arr1_op}")
    print("-" * 20)

    # Test Case 3 - All Zeros
    arr2 = [0, 0, 0, 0]
    print(f"Original Array 3: {arr2}")
    moveZeroesOp(arr2)
    print(f"Optimal Result:     {arr2}")
    print("-" * 20)

    # Test Case 4 - No Zeros
    arr3 = [1, 2, 3, 4, 5]
    print(f"Original Array 4: {arr3}")
    moveZeroesOp(arr3)
    print(f"Optimal Result:     {arr3}")
    print("-" * 20)
    
    # Test Case 5 - Zeros at the end
    arr4 = [1, 2, 0, 0]
    print(f"Original Array 5: {arr4}")
    moveZeroesOp(arr4)
    print(f"Optimal Result:     {arr4}")
    print("-" * 20)
