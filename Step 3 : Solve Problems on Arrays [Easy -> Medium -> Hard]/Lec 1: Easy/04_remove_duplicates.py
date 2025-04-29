# Remove Duplicates from Sorted Array
# Problem:
# Given a sorted array `arr`, remove the duplicates **in-place** such that each unique element 
# appears only once. Return the number of unique elements (`k`) and modify the array so that 
# the first `k` elements are the unique ones, maintaining original relative order.

# Constraints:
# - Do it with O(1) extra space (no new array allowed).
# - Sorted order helps to detect duplicates easily because all duplicates are adjacent.

# Approach:
# - We use a pointer `k` to track the position where the next unique element should be placed.
# - We start with `k = 1` because the first element is always unique.
# - Then we iterate through the array starting from index 1.
# - If the current element `arr[i]` is **not equal** to the previous element `arr[i-1]`,
#   we copy it to `arr[k]` and increment `k`.
# - If the current element is same as previous, we skip it.

# Why this works:
# - Since the array is sorted, all duplicates are next to each other.
# - So whenever `arr[i] != arr[i-1]`, it guarantees a new unique element.

# Time Complexity: 
# - O(n) where n = number of elements in the array.
# - We traverse the array exactly once.

# Space Complexity:
# - O(1) extra space (in-place modification, no extra array created).

# Note:
# - After running this function, only the first `k` elements of `arr` are guaranteed to be correct.
# - The elements after index `k-1` don't matter.

def remove_dup(arr, n):
    if n <= 1:
        return 1
    
    # k points to the next position to insert a unique element
    k = 1

    for i in range(1, n):
        if arr[i - 1] == arr[i]:
            continue
        else:
            arr[k] = arr[i]
            k += 1
    
    # Return both k and the modified array
    return [k, arr]
            

# Example usage:
arr = [1,1,1,2,2,2,3,4,4]
print("Unique elements and modified array:", remove_dup(arr, len(arr)))

# Output:
# Unique elements and modified array: [4, [1, 2, 3, 4, 2, 2, 3, 4, 4]]
# Explanation:
# - First 4 elements are [1,2,3,4] (unique elements).
# - k = 4
# - Rest elements (from index 4 onwards) can be anything.
