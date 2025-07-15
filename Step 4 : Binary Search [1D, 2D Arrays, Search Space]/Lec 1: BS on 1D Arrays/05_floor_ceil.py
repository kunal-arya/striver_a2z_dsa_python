"""
Problem: Floor and Ceil in a Sorted Array (Using Binary Search Bounds)

Given a sorted array and a target value, find:
- Floor: the greatest element ≤ target
- Ceil : the smallest element ≥ target

We'll use:
- Lower Bound: First index with element ≥ target → gives **ceil**
- Upper Bound: First index with element > target → floor is just before it

Return -1 if floor or ceil doesn't exist.
"""

# ------------------------------
# Observations:
# ------------------------------
# - Array is sorted in non-decreasing order
# - Lower Bound gives Ceil directly
# - Floor is element at (upper_bound - 1) if index is valid
# - Edge cases: target < min or > max must be handled carefully

# ------------------------------
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ------------------------------

from typing import List

def lowerBoundBinary(arr: List[int], target: int) -> int:
    """
    Lower Bound - First index where arr[i] >= target
    """
    n = len(arr)
    low = 0
    high = n - 1
    ans = n  # Default if no element ≥ target

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def upperBoundBinary(arr: List[int], target: int) -> int:
    """
    Upper Bound - First index where arr[i] > target
    """
    n = len(arr)
    low = 0
    high = n - 1
    ans = n  # Default if no element > target

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def find_floor(arr: List[int], target: int) -> int:
    """
    Finds the floor of the target using upper bound logic.
    Floor = arr[upper_bound_index - 1] if index > 0
    """
    idx = upperBoundBinary(arr, target)
    if idx == 0:
        return -1  # No element ≤ target
    return arr[idx - 1]


def find_ceil(arr: List[int], target: int) -> int:
    """
    Finds the ceil of the target using lower bound logic.
    Ceil = arr[lower_bound_index] if index < len(arr)
    """
    idx = lowerBoundBinary(arr, target)
    if idx == len(arr):
        return -1  # No element ≥ target
    return arr[idx]

# ------------------------------
# Dry Run Example:
# arr = [1, 3, 5, 7, 9], target = 6
# lower_bound = 3 → arr[3] = 7 → ceil = 7
# upper_bound = 3 → arr[2] = 5 → floor = 5
# ------------------------------

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    target = 6

    floor_val = find_floor(arr, target)
    ceil_val = find_ceil(arr, target)

    print(f"Array : {arr}")
    print(f"Target: {target}")
    print(f"Floor : {floor_val}")
    print(f"Ceil  : {ceil_val}")

# ------------------------------
# Follow-ups:
# ------------------------------
# - What if the array is unsorted? → Sort first (O(n log n)) then use same logic
# - How would you handle multiple queries efficiently? → Preprocessing or segment trees
# - Can you return the index instead of value? → Yes, use bounds directly
