from typing import List

# ---------------------------------------------
# PROBLEM: UNION OF TWO SORTED ARRAYS
# ---------------------------------------------
# Given two sorted arrays, return the union of the arrays (unique elements only, sorted).
# 
# Example:
#   arr1 = [1,1,2,3,4,5]
#   arr2 = [1,2,3,3,4,4,5,6]
#   Output: [1,2,3,4,5,6]
#
# Union means combining all elements from both arrays, but only keeping distinct values.

# ---------------------------------------------
# BRUTE FORCE APPROACH
# ---------------------------------------------
def findUnion(arr1: List[int], arr2: List[int]) -> List[int]:
    n1 = len(arr1)
    n2 = len(arr2)

    # Use a set to store only unique elements
    union_set = set()

    for i in range(n1):
        union_set.add(arr1[i])
    for i in range(n2):
        union_set.add(arr2[i])

    # Convert the set to a sorted list
    sorted_set = sorted(union_set)

    union = []
    for num in sorted_set:
        union.append(num)
    
    return union

arr1 = [1,1,2,3,4,5]
arr2 = [1,2,3,3,4,4,5,6]

print(findUnion(arr1, arr2))

# ---------------------------------------------
# INTUITION:
# - Set automatically removes duplicates.
# - Sorting ensures ascending order.

# ---------------------------------------------
# VISUAL DRY RUN:
# arr1: [1,1,2,3,4,5]
# arr2: [1,2,3,3,4,4,5,6]
# union_set after both loops: {1,2,3,4,5,6}
# sorted_set: [1,2,3,4,5,6]
# Output: [1,2,3,4,5,6]

# ---------------------------------------------
# OPTIMISED APPROACH - TWO POINTERS
# ---------------------------------------------
# Pre-condition: arr1 and arr2 are sorted

def pushToArr(arr: List[int], k: int) -> None:
    # Append element only if last element is not same (ensures uniqueness)
    if len(arr) == 0 or arr[-1] != k:
        arr.append(k)

def findUnionOp(arr1: List[int], arr2: List[int]) -> List[int]:
    n1 = len(arr1)
    n2 = len(arr2)
    union = []
    i = 0
    j = 0

    # Use two pointers to merge arrays and avoid duplicates
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            pushToArr(union, arr1[i])
            i += 1
        else:
            pushToArr(union, arr2[j])
            j += 1

    # Add remaining elements from arr1
    while i < n1:
        pushToArr(union, arr1[i])
        i += 1

    # Add remaining elements from arr2
    while j < n2:
        pushToArr(union, arr2[j])
        j += 1

    return union

arr1 = [1,1,2,2,3,3,4,5]
arr2 = [1,1,2,3,3,4,4,5,6]

print(findUnionOp(arr1, arr2))

# ---------------------------------------------
# INTUITION:
# - Like merge step in merge sort.
# - Use two pointers to traverse both arrays, compare and add unique elements.

# ---------------------------------------------
# VISUAL DRY RUN:
# arr1 = [1,1,2,2,3,3,4,5]
# arr2 = [1,1,2,3,3,4,4,5,6]
#
# i -> arr1, j -> arr2, union = []
# 1 == 1 -> push 1, i++, j++
# 1 == 1 -> skip (already added), i++, j++
# 2 == 2 -> push 2, i++, j++
# 2 < 3 -> skip duplicate, i++
# 3 == 3 -> push 3, i++, j++
# ...continue until both lists end
# Output: [1,2,3,4,5,6]

# ---------------------------------------------
# PROBLEM: INTERSECTION OF TWO SORTED ARRAYS
# ---------------------------------------------
# Return only the common elements from both arrays (once, no duplicates).
# 
# Example:
# arr1 = [1,1,2,2,3,3,4,5]
# arr2 = [2,3,3,4,4,5,6]
# Output: [2,3,4,5]

# ---------------------------------------------
# BRUTE FORCE APPROACH
# ---------------------------------------------
def findIntersection(a: List[int], b: List[int]) -> List[int]:
    r_set = set()
    result = []
    n1 = len(a)
    n2 = len(b)

    # Store all elements of a in a set
    for i in range(n1):
        r_set.add(a[i])

    # Check which elements of b exist in the set
    for j in range(n2):
        if b[j] in r_set:
            result.append(b[j])
            r_set.remove(b[j])  # Remove to avoid duplicates in result

    return result

arr1 = [1,1,2,2,3,3,4,5]
arr2 = [2,3,3,4,4,5,6]

print(findIntersection(arr1, arr2))

# ---------------------------------------------
# INTUITION:
# - Use set for fast lookup (O(1)).
# - Remove from set after adding to result to ensure uniqueness.

# ---------------------------------------------
# VISUAL DRY RUN:
# r_set after arr1: {1,2,3,4,5}
# Check arr2:
# 2 in set -> add to result, remove from set
# 3 in set -> add, remove
# 3 not in set -> skip
# 4 -> add, remove
# 4 -> skip
# 5 -> add, remove
# 6 -> skip
# Output: [2,3,4,5]

# ---------------------------------------------
# OPTIMISED APPROACH - TWO POINTERS
# ---------------------------------------------
# Pre-condition: arrays are sorted

def findIntersectionOp(a: List[int], b: List[int]) -> List[int]:
    n1 = len(a)
    n2 = len(b)
    union = []
    i = 0
    j = 0

    while i < n1 and j < n2:
        # Add to union only when a[i] == b[j] and it's not duplicate
        if a[i] == b[j] and (len(union) == 0 or union[-1] != a[i]):
            union.append(a[i])
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        else:
            i += 1

    return union

a = [1,1,2,2,3,3,4,5]
b = [2,3,3,4,4,5,6]

print(findIntersectionOp(a, b))

# ---------------------------------------------
# INTUITION:
# - Use two pointers like in merge sort.
# - Only add equal elements, avoid duplicates using union[-1] check.

# ---------------------------------------------
# VISUAL DRY RUN:
# a = [1,1,2,2,3,3,4,5]
# b = [2,3,3,4,4,5,6]
# i -> a, j -> b, union = []
# a[0]=1 < b[0]=2 -> i++
# a[1]=1 < b[0]=2 -> i++
# a[2]=2 == b[0]=2 -> add 2
# a[3]=2 < b[1]=3 -> i++
# a[4]=3 == b[1]=3 -> add 3
# ...
# Output: [2,3,4,5]