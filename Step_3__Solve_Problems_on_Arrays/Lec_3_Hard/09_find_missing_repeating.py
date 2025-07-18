# =============================================================================
# PROBLEM STATEMENT: Find Missing and Repeating Numbers
# =============================================================================
# Given an array of n integers where each integer is between 1 to n.
# One number is missing and one number is repeated.
# Find both the missing and repeating numbers.
# 
# Example: [1,3,4,5,5,6] → Missing: 2, Repeating: 5
# Array should have been [1,2,3,4,5,6] but 2 is missing and 5 appears twice

from typing import List

# =============================================================================
# APPROACH 1: BRUTE FORCE
# =============================================================================
# INTUITION: Check frequency of each number from 1 to n
# OBSERVATION: If count == 2 → repeating, if count == 0 → missing
# TIME: O(n²) SPACE: O(1)

def findMissingRepeatingBrute(arr: List[int]):
    n = len(arr)
    repeating, missing = -1, -1

    # Check each number from 1 to n
    for i in range(1, n + 1):
        count = 0
        
        # Count occurrences of number i in array
        for j in range(n):
            if arr[j] == i:
                count += 1
        
        # Determine if missing or repeating
        if count == 2:
            repeating = i
        elif count == 0:
            missing = i

        # Early termination when both found
        if repeating != -1 and missing != -1:
            break

    return {"repeating": repeating, "missing": missing}

# DRY RUN: arr = [1,3,4,5,5,6]
# i=1: count=1 (normal) | i=2: count=0 (missing=2) | i=3: count=1 (normal)
# i=4: count=1 (normal) | i=5: count=2 (repeating=5) | i=6: count=1 (normal)
# Result: missing=2, repeating=5

# =============================================================================
# APPROACH 2: HASH TABLE / FREQUENCY ARRAY
# =============================================================================
# INTUITION: Use extra space to count frequency in single pass
# OBSERVATION: hash[i] = frequency of number i
# TIME: O(n) SPACE: O(n)

def findMissingRepeatingBetter(arr: List[int]):
    n = len(arr)
    hash = [0] * (n + 1)  # Index 0 unused, 1 to n used

    # Count frequency of each number
    for i in range(n):
        hash[arr[i]] += 1
    
    missing, repeating = -1, -1

    # Check frequencies from 1 to n
    for i in range(1, n + 1):
        if hash[i] == 2:
            repeating = i
        elif hash[i] == 0:
            missing = i
        
        if repeating != -1 and missing != -1:
            break
    
    return {"repeating": repeating, "missing": missing}

# VISUAL: arr = [1,3,4,5,5,6]
# hash = [0, 1, 0, 1, 1, 2, 1]  (index represents number, value is frequency)
#         0  1  2  3  4  5  6
# hash[2] = 0 → missing=2, hash[5] = 2 → repeating=5

# =============================================================================
# APPROACH 3: MATHEMATICS (Sum and Sum of Squares)
# =============================================================================
# INTUITION: Use mathematical formulas to create equations
# OBSERVATION: Let x = repeating, y = missing
# S - Sn = x - y (equation 1)
# S2 - S2n = x² - y² = (x-y)(x+y) (equation 2)
# TIME: O(n) SPACE: O(1)

def findMissingRepeatingOp(arr: List[int]):
    n = len(arr)
    
    # Mathematical formulas for sum of first n natural numbers
    Sn = (n * (n + 1)) // 2           # Sum: 1+2+...+n
    S2n = (n * (n + 1) * (2 * n + 1)) // 6  # Sum of squares: 1²+2²+...+n²
    
    # Calculate actual sums from array
    S = sum(arr)                      # Actual sum
    S2 = sum(x * x for x in arr)     # Actual sum of squares
        
    # Create two equations:
    val1 = S - Sn        # x - y (repeating - missing)
    val2 = S2 - S2n      # x² - y² = (x-y)(x+y)
    
    # Solve: x² - y² = (x-y)(x+y) → x+y = (x²-y²)/(x-y)
    val2 = val2 // val1  # x + y (repeating + missing)
    
    # Solve system of equations:
    # x - y = val1
    # x + y = val2
    # Adding: 2x = val1 + val2 → x = (val1 + val2) / 2
    x = (val1 + val2) // 2  # repeating number
    y = val2 - x            # missing number

    return {"repeating": x, "missing": y}

# MATHEMATICAL DERIVATION:
# For [1,3,4,5,5,6]: Expected sum = 1+2+3+4+5+6 = 21, Actual sum = 1+3+4+5+5+6 = 24
# val1 = 24 - 21 = 3 = x - y
# Expected sum² = 1+4+9+16+25+36 = 91, Actual sum² = 1+9+16+25+25+36 = 112
# val2 = 112 - 91 = 21 = x² - y²
# x + y = 21 / 3 = 7
# x = (3 + 7) / 2 = 5 (repeating), y = 7 - 5 = 2 (missing)

# =============================================================================
# APPROACH 4: CYCLIC SORT
# =============================================================================
# INTUITION: Numbers 1 to n should be at positions 0 to n-1 respectively
# OBSERVATION: After sorting, arr[i] should equal i+1. If not, we found our answer
# TIME: O(n) SPACE: O(1)

def findMissingRepeatingOp2(arr: List[int]):
    n = len(arr)
    
    # Cyclic sort: place each number at its correct position
    i = 0
    while i < n:
        correct_idx = arr[i] - 1  # Number arr[i] should be at index arr[i]-1
        
        # If number is already at correct position, move to next
        if arr[i] == arr[correct_idx]:
            i += 1
        else:
            # Swap current number to its correct position
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    # After sorting, find the position where number doesn't match
    for k in range(1, n + 1):
        if arr[k - 1] != k:
            repeating = arr[k - 1]  # Number at wrong position
            missing = k             # Expected number at this position
            break

    return {"repeating": repeating, "missing": missing}

# VISUAL DRY RUN: arr = [5,5,4,3,6,1]
# Step 1: Sort cyclically
# Initial: [5,5,4,3,6,1] (5 should be at index 4)
# After swaps: [1,2,3,4,5,6] but we have [1,5,3,4,5,6] (5 appears twice)
# 
# Step 2: Find mismatch
# Index 1: arr[1] = 5, expected = 2 → missing = 2, repeating = 5

# =============================================================================
# APPROACH 5: XOR BIT MANIPULATION (Most Optimal)
# =============================================================================
# INTUITION: XOR all array elements with 1 to n, only missing^repeating remains
# OBSERVATION: Use bit difference to separate missing and repeating numbers
# TIME: O(n) SPACE: O(1)

def findMissingRepeatingOp3(arr: List[int]):
    n = len(arr)

    # Step 1: XOR all array elements with numbers 1 to n
    # This gives us: missing XOR repeating
    xr = 0
    for i in range(n):
        xr ^= arr[i]    # XOR with array elements
        xr ^= (i + 1)   # XOR with numbers 1 to n
    
    # Step 2: Find rightmost set bit (where missing and repeating differ)
    # This bit will help us separate the two numbers
    bitNo = 0
    while True:
        if (xr & (1 << bitNo)) != 0:
            break
        bitNo += 1
    
    # Step 3: Divide all numbers into two groups based on the bit
    # Group with bit set to 0, Group with bit set to 1
    zero = 0  # XOR of all numbers with bit 0 at position bitNo
    one = 0   # XOR of all numbers with bit 1 at position bitNo
    
    # Process array elements
    for i in range(n):
        if (arr[i] & (1 << bitNo)) != 0:
            one ^= arr[i]
        else:
            zero ^= arr[i]
    
    # Process numbers 1 to n
    for i in range(1, n + 1):
        if (i & (1 << bitNo)) != 0:
            one ^= i
        else:
            zero ^= i
    
    # Step 4: Determine which is missing and which is repeating
    # Count occurrences of one of the candidates in original array
    count = 0
    for i in range(n):
        if arr[i] == zero:
            count += 1
    
    # If count is 0, then 'zero' is missing, 'one' is repeating
    # If count is 2, then 'zero' is repeating, 'one' is missing
    if count == 0:
        missing, repeating = zero, one
    else:
        missing, repeating = one, zero

    return {"repeating": repeating, "missing": missing}

# XOR LOGIC EXPLANATION:
# Example: [5,5,4,3,6,1] should be [1,2,3,4,5,6]
# 
# Step 1: XOR all elements
# 5^5^4^3^6^1^1^2^3^4^5^6 = 5^2 = 7 (binary: 111)
# 
# Step 2: Find different bit
# 5 = 101, 2 = 010 → they differ at bit 0 (rightmost)
# 
# Step 3: Separate into groups based on bit 0
# Bit 0 = 1: [5,5,3,1] and [1,3,5] from 1-6 → XOR = 5
# Bit 0 = 0: [4,6] and [2,4,6] from 1-6 → XOR = 2
# 
# Step 4: Check which appears in array
# 5 appears twice → repeating=5, missing=2

# =============================================================================
# MEMORY HELPERS & KEY INSIGHTS
# =============================================================================
# 1. BRUTE FORCE: Count each number's frequency - simple but slow O(n²)
# 
# 2. HASH TABLE: Trade space for time - O(n) time, O(n) space
# 
# 3. MATHEMATICS: Use algebraic equations
#    - Sum difference gives (repeating - missing)
#    - Sum of squares difference gives (repeating² - missing²)
#    - Solve system of equations to get both numbers
# 
# 4. CYCLIC SORT: Place each number at correct position
#    - Number 'i' should be at index 'i-1'
#    - After sorting, mismatch reveals the answer
# 
# 5. XOR BIT MANIPULATION: Most elegant solution
#    - XOR cancels out identical numbers
#    - Use bit difference to separate missing and repeating
#    - No extra space, O(n) time
#
# INTERVIEW TIP: Start with brute force, then optimize step by step.
# XOR approach shows strong bit manipulation skills!

# Test all approaches
if __name__ == "__main__":
    arr = [6, 5, 8, 7, 1, 4, 1, 3, 2]
    print("Test array:", arr)
    print("Brute Force:", findMissingRepeatingBrute(arr.copy()))
    print("Hash Table:", findMissingRepeatingBetter(arr.copy()))
    print("Mathematics:", findMissingRepeatingOp(arr.copy()))
    print("Cyclic Sort:", findMissingRepeatingOp2(arr.copy()))
    print("XOR Method:", findMissingRepeatingOp3(arr.copy()))