# -----------------------------------------------
# Maximum Ascending Subarray Sum
# Link: https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
# -----------------------------------------------

# Intuition:
# We want to find the maximum sum of a subarray where every next element is bigger than previous one.
# If arr[i] > arr[i-1], we continue adding to current subarray sum.
# Else, we restart subarray from arr[i].
# Track the maximum sum while doing this.

def max_sub(arr, n):
    if n <= 0:
        return 0
    if n == 1:
        return arr[0]
    
    total_sum = arr[0]   # Current ascending subarray sum
    max_sum = arr[0]     # Max among all ascending subarrays

    for i in range(1, n):
        if arr[i - 1] < arr[i]:
            total_sum += arr[i]  # Continue ascending subarray
        else:
            total_sum = arr[i]   # Restart subarray from current element
        max_sum = max(max_sum, total_sum)
    
    return max_sum

# Example usage:
arr = [10, 20, 30, 5, 10, 50]
print("Largest ascending subarray sum:", max_sub(arr, len(arr)))

# -----------------------------------------------
# Time Complexity: O(n)
# - Single pass through array.
# Space Complexity: O(1)
# - Only using few extra variables.
# -----------------------------------------------


# -----------------------------------------------
# Check if Array is Sorted and Rotated
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
# -----------------------------------------------

# Helper function to check if an array is sorted (non-decreasing)
def is_sorted(arr, n):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Brute Force Approach:
# Try all possible rotations and check if any rotation gives sorted array.

def arr_sorted_b(arr, n):
    if n <= 1:
        return True
    
    if is_sorted(arr, n):
        return True
    
    for i in range(1, n):
        new_arr = arr[i:n] + arr[:i]   # Rotate at index i
        if is_sorted(new_arr, n):
            return True
        
    return False

# Example usage:
arr = [5, 1, 3, 4]
print("Array Sorted Brute Force:", arr_sorted_b(arr, len(arr)))

# -----------------------------------------------
# Time Complexity: O(n^2)
# - For each rotation (n rotations), checking if sorted (O(n) each time).
# Space Complexity: O(n)
# - Because creating a new rotated array.
# -----------------------------------------------


# ---------------------------------------------------------
# Problem: Check if Array is Sorted and Rotated
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# ---------------------------------------------------------

# Intuition:
# - We want to check if the array is sorted (non-decreasing) after any rotation (including 0 rotation).
# - A rotation moves the start of the sorted array to somewhere else.
# - We simulate rotating the array by using modulo (%) and checking subarrays.
# 
# Approach in this code:
# - Loop through the array twice (simulate full rotation).
# - Maintain a 'count' of consecutive non-decreasing elements.
# - If count becomes equal to n (full array length), it means the array is sorted and rotated properly.

def arr_sorted_op(arr, n):
    n = len(arr)

    if n <= 1:
        return True  # 0 or 1 element is always sorted
    
    count = 1  # To keep track of consecutive non-decreasing elements

    for idx in range(1, 2 * n):
        i = idx % n  # Circular indexing using modulo to simulate rotation

        if arr[i - 1] <= arr[i]:
            count += 1  # Non-decreasing, extend the streak
        else:
            count = 1   # Break in order, reset streak to 1
        
        if count == n:
            return True  # Full array is non-decreasing in some rotation
    
    return False  # No full sorted rotation found

# Example usage:
arr = [5, 1, 3, 4]
print("Array Sorted Optimised Approach:", arr_sorted_op(arr, len(arr)))

# ---------------------------------------------------------
# Time Complexity: O(n)
# - We loop at most 2n times but each element is accessed in O(1).
# - So overall O(n).
#
# Space Complexity: O(1)
# - Only using count and loop variables. No extra space proportional to input size.
# ---------------------------------------------------------