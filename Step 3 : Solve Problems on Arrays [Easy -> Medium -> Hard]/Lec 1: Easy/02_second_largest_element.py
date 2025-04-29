# Find Second Largest Element in an Array
# ----------------------------------------

# Time Complexity:
# - O(N) --> We are traversing the array once
# Space Complexity:
# - O(1) --> Constant extra space

# Approach:
# 1. Initialize two variables: largest and second largest to -1 (or a minimum possible value).
# 2. Traverse the array:
#    - If current element > largest:
#         - Update second largest to largest
#         - Update largest to current element
#    - Else if current element < largest and > second largest:
#         - Update second largest
# 3. Return the second largest element.

# Tips:
# Keep track of both the largest and the second largest separately.

# Update second largest only when needed — not blindly.

# Think about the update order: when you find a new maximum, previous maximum becomes second largest.


def secLargest(arr, n):
    # Edge case: if array has 0 or 1 element, no second largest
    if n <= 1:
        return -1

    largest = -1
    sec_largest = -1

    for i in range(n):
        # If current element is greater than largest,
        # update second largest and largest
        if arr[i] > largest:
            largest, sec_largest = arr[i], largest

        # If current element is smaller than largest but greater than second largest,
        # update second largest
        elif arr[i] < largest and arr[i] > sec_largest:
            sec_largest = arr[i]
        
    return sec_largest


# Driver Code
arr = [64, 34, 25, 12, 22, 11, 90]
print("Second Largest Element:", secLargest(arr, len(arr)))
