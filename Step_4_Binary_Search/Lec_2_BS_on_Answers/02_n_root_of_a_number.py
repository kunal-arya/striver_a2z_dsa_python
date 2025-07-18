"""
DSA Problem Solution: Find Nth Root of a Number
================================================

Problem: Given two positive integers n and m, find the nth root of m.
Platform: Striver's A2Z DSA Course
Difficulty: Easy
Topics: Binary Search
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: Two integers, `n` (the root) and `m` (the number).
- Output: The integer `r` such that `r^n = m`. If no such integer exists, return -1.
- Constraints: `n > 0`, `m > 0`.
- Edge Cases: 
    - When `m` is a perfect nth power.
    - When `m` is not a perfect nth power.
    - `n=1` (the root is `m` itself).
    - `m=1` (the root is `1`).

APPROACH:
The problem asks for an integer `r` where `r^n = m`. This means we are searching for `r` in the range from 1 to `m`.

1. Brute Force: We can iterate from 1 up to `m` and for each number `i`, check if `i^n == m`.
2. Optimal (Binary Search): Since the search space `[1, m]` is sorted, we can use binary search to find the root `r` more efficiently. For a given `mid` value, if `mid^n > m`, we search in the lower half. If `mid^n < m`, we search in the upper half.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def nRootBrute(n, m):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - We test every integer `i` from 1 up to `m`.
    - For each integer `i`, we calculate `i` to the power of `n`.
    - If `i^n` equals `m`, we have found the root.
    - If we iterate through all numbers up to `m` without finding a root, no integer root exists.
    
    Approach:
    1. Loop from `i = 1` to `m`.
    2. In each iteration, calculate `power = i^n`.
    3. If `power == m`, return `i`.
    4. If the loop finishes without finding a root, return -1.
    
    Args:
        n (int): The root degree.
        m (int): The number to find the root of.
    
    Returns:
        int: The nth root of m, or -1 if it's not an integer.
    
    Time Complexity: O(m * log n) - The loop runs `m` times, and `i^n` takes O(log n) time.
    Space Complexity: O(1) - No extra space is used.
    """
    
    for i in range(1, m + 1):
        # Check if i^n equals m
        if i ** n == m:
            return i
        # Optimization: if i^n exceeds m, no need to check further
        if i ** n > m:
            break
            
    return -1

# ==============================================================================
# SOLUTION 2: OPTIMAL APPROACH (BINARY SEARCH)
# ==============================================================================

def nRootOp(n, m):
    """
    OPTIMAL APPROACH - Using Binary Search for efficiency.
    
    Intuition:
    - The possible integer roots are in a sorted range from 1 to `m`.
    - We can use binary search to efficiently find the target root.
    - For any chosen number `mid` in the range, if `mid^n` is greater than `m`, the actual root must be smaller, so we search the left half.
    - If `mid^n` is less than `m`, the root must be larger, so we search the right half.
    
    Approach:
    1. Initialize `low = 1` and `high = m`.
    2. Loop while `low <= high`.
    3. Calculate `mid = low + (high - low) // 2`.
    4. Calculate `mid_power = mid^n`.
    5. If `mid_power == m`, we found the root, return `mid`.
    6. If `mid_power > m`, the root is smaller, so set `high = mid - 1`.
    7. If `mid_power < m`, the root is larger, so set `low = mid + 1`.
    8. If the loop finishes, no integer root was found, return -1.
    
    Args:
        n (int): The root degree.
        m (int): The number to find the root of.
    
    Returns:
        int: The nth root of m, or -1 if it's not an integer.
    
    Time Complexity: O(log m * log n) - Binary search takes O(log m) iterations, and `mid^n` takes O(log n) time.
    Space Complexity: O(1) - No extra space is used.
    """
    
    low = 1
    high = m

    while low <= high:
        mid = low + (high - low) // 2
        mid_n = mid ** n
        
        if mid_n == m:
            return mid
        elif mid_n > m:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

def safePower(base, exp, limit):
    """
    Manually calculate base^exp using loop, while checking for overflow.
    This simulates how we would do it in Java or C++ where integers can overflow.

    Args:
        base (int): The base number.
        exp (int): The exponent (root degree).
        limit (int): The number m, used for early overflow detection.

    Returns:
        1 if == m
        0 if < m
        2 if > m
    """
    result = 1

    for _ in range(exp):
        result *= base
        # Simulate overflow check as we do in C++ or Java.
        # If result * base would exceed limit, return 2 to indicate overflow.
        if result > limit:
            return 2
    
    if result == limit:
        return 1 
    return 0


def nRootOp2(n, m):
    """
    Safe and portable implementation of nth root finder.
    This code avoids Python-specific features and behaves just like C++/Java.

    Binary Search Logic:
    - Try to find an integer `x` such that x^n == m.
    - If mid^n == m: return mid
    - If mid^n < m: move right (low = mid + 1)
    - If mid^n > m or overflow: move left (high = mid - 1)

    Args:
        n (int): The degree of the root.
        m (int): The number to find the root of.

    Returns:
        int: The nth root of m if it's an integer, else -1.
    """

    low = 1
    high = m

    while low <= high:
        mid = low + (high - low) // 2

        # Instead of mid ** n, we use a safe manual power function
        mid_power = safePower(mid, n, m)

        if mid_power == 1:
            return mid
        elif mid_power == 2:
            # mid^n either overflowed or exceeded m, search left
            high = mid - 1
        else:
            # mid^n < m, search right
            low = mid + 1

    return -1


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    n = 4
    m = 81
    
    print(f"Finding {n}th root of {m}:")
    
    # Test Brute Force Approach
    brute_result = nRootBrute(n, m)
    print(f"Brute Force Result: {brute_result}")

    # Test Optimal Approach
    optimal_result = nRootOp(n, m)
    print(f"Optimal (Binary Search) Result: {optimal_result}")

    # Verification
    assert brute_result == optimal_result, "Results from both approaches do not match!"
    print("Both approaches give the same result.")
    
    # Example with no integer root
    n2 = 9
    m2 = 1953125
    print(f"Finding {n2}th root of {m2}:")
    optimal_result_2 = nRootOp(n2, m2)
    print(f"Optimal (Binary Search) Result: {optimal_result_2}")
    optimal_result_3 = nRootOp2(n2, m2)
    print(f"Optimal (Binary Search) Result 2: {optimal_result_3}")