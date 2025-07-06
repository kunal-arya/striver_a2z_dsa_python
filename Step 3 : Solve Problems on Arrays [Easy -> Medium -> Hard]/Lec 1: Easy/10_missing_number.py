from typing import List

# -------------------------------------------------------
# PROBLEM: FIND THE MISSING NUMBER FROM ARRAY
# -------------------------------------------------------
# You are given an array of size `n` containing numbers from 0 to n (inclusive),
# but one number is missing. Return the missing number.
#
# Example:
#   arr = [0,1,2,4,5] → n = 5 → Missing = 3
#   Output: 3
#
# There will be exactly one number missing.

# -------------------------------------------------------
# APPROACH 1: BRUTE FORCE
# -------------------------------------------------------
def missingNum(arr: List[int]) -> int:
    n = len(arr)

    # For every number from 1 to n, check if it's in the array
    for i in range(1, n + 1):
        found = False
        for j in range(n):
            if arr[j] == i:
                found = True
        if found == False:
            return i

    return -1

arr = [1, 2, 4, 5]
print(missingNum(arr))  # Output: 3

# -------------------------------------------------------
# INTUITION:
# For each number in the expected range, we loop and search.
#
# TIME COMPLEXITY: O(n^2)
# SPACE COMPLEXITY: O(1)

# VISUAL DRY RUN:
# arr = [1, 2, 4, 5], n = 4
# Check: 1 ✅, 2 ✅, 3 ❌ → return 3

# -------------------------------------------------------
# APPROACH 2: BETTER (USING SORT)
# -------------------------------------------------------
def missingNumBetter(arr: List[int]) -> int:
    n = len(arr)
    arr.sort()
    i = 0

    # Check if sorted values match expected numbers
    for j in range(n):
        if arr[j] == i:
            i += 1
        else:
            return i
    return -1

arr = [0, 1, 2, 4, 5]
print(missingNumBetter(arr))  # Output: 3

# -------------------------------------------------------
# INTUITION:
# After sorting, the index should match the number at that index.
# As soon as mismatch is found, that's the missing number.
#
# TIME: O(n log n) due to sorting
# SPACE: O(1)

# VISUAL DRY RUN:
# Sorted arr = [0, 1, 2, 4, 5]
# i = 0 → 0 ✅ → i=1 → 1 ✅ → i=2 → 2 ✅ → i=3 → 4 ❌ → return 3

# -------------------------------------------------------
# APPROACH 3: BETTER (USING HASHING)
# -------------------------------------------------------
def missingNumHashing(arr: List[int]) -> int:
    """
    Use a set to track all numbers in the array.
    Loop from 0 to n, and return the number not found in the set.
    """
    n = len(arr)
    s = set(arr)

    for i in range(n + 1):
        if i not in s:
            return i
    return -1

arr = [0, 1, 2, 4, 5]
print(missingNumHashing(arr))  # Output: 3

# -------------------------------------------------------
# TIME: O(n)
# SPACE: O(n) (for set)

# VISUAL DRY RUN:
# set = {0,1,2,4,5}
# i: 0 ✅, 1 ✅, 2 ✅, 3 ❌ → return 3

# -------------------------------------------------------
# EXTRA: CYCLIC SORT HELPER FUNCTION (FOR 1 TO N)
# -------------------------------------------------------
def cyclicSort(arr: List[int]) -> List[int]:
    n = len(arr)
    i = 0
    while i < n:
        correct_idx = arr[i] - 1
        if arr[i] == arr[correct_idx]:
            i += 1
        else:
            arr[correct_idx], arr[i] = arr[i], arr[correct_idx]
    return arr

arr = [3, 4, 2, 1, 5]
print("Cyclic Sort")
print(cyclicSort(arr))  # Output: [1,2,3,4,5]

# -------------------------------------------------------
# CYCLIC SORT WORKS WELL WHEN:
# - Numbers are from 1 to n (or 0 to n with adjustments).
# - You can place every number at its correct index.

# -------------------------------------------------------
# APPROACH 4: OPTIMAL USING CYCLIC SORT
# -------------------------------------------------------

def cyclicSortForMissing(arr: List[int], n: int) -> None:
    i = 0
    while i < n:
        correct_idx = arr[i]
        # If number is n or already placed correctly, skip
        if correct_idx == n or arr[correct_idx] == arr[i]:
            i += 1
            continue
        else:
            arr[correct_idx], arr[i] = arr[i], arr[correct_idx]

def findMissingOp(arr: List[int]) -> int:
    n = len(arr)

    # Step 1: Place numbers at correct index
    cyclicSortForMissing(arr, n)

    # Step 2: Check which index is incorrect
    correctNum = 0 
    missing = -1

    for num in arr:
        if num == correctNum and num != n:
            correctNum += 1
        else:
            missing = correctNum
            break

    # If all elements are at correct positions, missing is n
    if missing == -1:
        return n
    else:
        return missing

arr = [0, 1, 2, 4, 5]
print(findMissingOp(arr))  # Output: 3

# -------------------------------------------------------
# INTUITION:
# - Use modified Cyclic Sort to place each number at index = value.
# - If a number equals n, skip it since n is out of bounds.
# - Traverse array and check which index does not match the value.
#
# TIME: O(n)
# SPACE: O(1)

# VISUAL DRY RUN:
# arr = [0,1,2,4,5], n = 5
# After cyclic sort → [0,1,2,5,4]
# index 3 → value is 5 (should be 3) → missing = 3

# Final Output: 3


# Optimised Version ( sum )

def missingNumberOpS(nums: List[int]) -> int:
        n = len(nums)

        sum_of_n: int = ( n * (n + 1) ) // 2

        sum: int = 0

        for num in nums:
            sum += num
        
        missing = sum_of_n - sum

        return missing

arr = [0, 1, 2, 4, 5]
print(missingNumberOpS(arr))  # Output: 3