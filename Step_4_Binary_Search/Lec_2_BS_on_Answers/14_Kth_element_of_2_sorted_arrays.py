"""
Problem: K-th element of two sorted arrays
Platform: GeeksforGeeks
Difficulty: Hard
Topics: Array, Binary Search
LINK: https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array/0
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: Two sorted arrays `arr1` and `arr2` of size `n` and `m` respectively, and an integer `k`.
- Output: The k-th smallest element after merging the two arrays.
- Constraints: 
  - 1 <= n, m <= 10^6
  - 1 <= arr1[i], arr2[i] <= 10^9
  - 1 <= k <= n + m
- Edge Cases: 
  - One array is empty.
  - k = 1 (smallest element)
  - k = n + m (largest element)

APPROACH:
The problem is similar to finding the median of two sorted arrays. We can adapt the binary search approach to find the k-th element. The core idea is to partition the two arrays such that all elements in the left partitions are smaller than all elements in the right partitions, and the total number of elements in the left partitions is equal to k.

TIME COMPLEXITY: O(log(min(n, m)))
SPACE COMPLEXITY: O(1)
"""

# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def kthElement_brute(arr1, arr2, n, m, k):
    """
    BRUTE FORCE APPROACH - Merge the two arrays and find the k-th element.
    
    Intuition:
    - The most straightforward way is to merge the two sorted arrays into a single sorted array.
    - The k-th element of the merged array is the answer.
    
    Approach:
    1. Create a new array `merged_arr` of size n + m.
    2. Use two pointers, `i` for `arr1` and `j` for `arr2`, to merge the arrays into `merged_arr`.
    3. Return `merged_arr[k-1]`.
    
    Args:
        arr1: The first sorted array.
        arr2: The second sorted array.
        n: Size of arr1.
        m: Size of arr2.
        k: The k-th element to find.
    
    Returns:
        The k-th smallest element of the two arrays.
    
    Time Complexity: O(n + m) - We iterate through both arrays once.
    Space Complexity: O(n + m) - We use an auxiliary array to store the merged elements.
    """
    
    merged_arr = []
    i, j = 0, 0
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1
            
    while i < n:
        merged_arr.append(arr1[i])
        i += 1
        
    while j < m:
        merged_arr.append(arr2[j])
        j += 1
        
    return merged_arr[k-1]

# =============================================================================
# SOLUTION 2: BETTER APPROACH
# =============================================================================

def kthElement_better(arr1, arr2, n, m, k):
    """
    BETTER APPROACH - Using two pointers without extra space.
    
    Intuition:
    - We can find the k-th element without creating a merged array.
    - We can use two pointers to traverse the arrays and keep a count of the elements.
    
    Approach:
    1. Use two pointers, `i` for `arr1` and `j` for `arr2`, and a counter `count`.
    2. Iterate while `count` is less than `k`.
    3. In each iteration, compare `arr1[i]` and `arr2[j]` and move the pointer of the smaller element.
    4. Increment the counter.
    5. When the counter reaches `k`, the last moved element is the k-th element.
    
    Args:
        arr1: The first sorted array.
        arr2: The second sorted array.
        n: Size of arr1.
        m: Size of arr2.
        k: The k-th element to find.
    
    Returns:
        The k-th smallest element of the two arrays.
    
    Time Complexity: O(k) - We iterate up to k times.
    Space Complexity: O(1) - No extra space is used.
    """
    
    i, j, count = 0, 0, 0
    
    while i < n and j < m:
        if count == k - 1:
            return min(arr1[i], arr2[j])
            
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
        count += 1
        
    while i < n:
        if count == k - 1:
            return arr1[i]
        i += 1
        count += 1
        
    while j < m:
        if count == k - 1:
            return arr2[j]
        j += 1
        count += 1
        
    return -1

# =============================================================================
# SOLUTION 3: OPTIMAL APPROACH
# =============================================================================

def kthElement_optimal(arr1, arr2, n, m, k):
    """
    OPTIMAL APPROACH - Binary Search on the smaller array.
    
    Intuition:
    - This is a variation of the "Median of two sorted arrays" problem.
    - We can partition the arrays into two halves, a left part and a right part.
    - The left part should contain `k` elements.
    - The maximum element in the left part of `arr1` should be less than or equal to the minimum element in the right part of `arr2`, and vice-versa.
    
    Approach:
    1. Ensure `arr1` is the smaller array to optimize the binary search range.
    2. Perform binary search on `arr1`. The `low` and `high` pointers will define the partition in `arr1`.
    3. For each `mid1` (partition in `arr1`), calculate `mid2` (partition in `arr2`) as `k - mid1`.
    4. Check if the partitions are valid:
       - `l1 <= r2` and `l2 <= r1`, where `l1`, `l2` are the max elements in the left partitions and `r1`, `r2` are the min elements in the right partitions.
    5. If the partition is valid, the answer is `max(l1, l2)`.
    6. If `l1 > r2`, it means the partition in `arr1` is too large, so move `high` to `mid1 - 1`.
    7. If `l2 > r1`, it means the partition in `arr1` is too small, so move `low` to `mid1 + 1`.
    
    Args:
        arr1: The first sorted array.
        arr2: The second sorted array.
        n: Size of arr1.
        m: Size of arr2.
        k: The k-th element to find.
    
    Returns:
        The k-th smallest element of the two arrays.
    
    Time Complexity: O(log(min(n, m))) - Binary search is on the smaller array.
    Space Complexity: O(1) - No extra space is used.
    """
    
    if n > m:
        return kthElement_optimal(arr2, arr1, m, n, k)
        
    low = max(0, k - m)
    high = min(k, n)
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        
        l1 = arr1[cut1 - 1] if cut1 > 0 else float('-inf')
        l2 = arr2[cut2 - 1] if cut2 > 0 else float('-inf')
        r1 = arr1[cut1] if cut1 < n else float('inf')
        r2 = arr2[cut2] if cut2 < m else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
            
    return -1

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    arr1 = [2, 3, 6, 7, 9]
    arr2 = [1, 4, 8, 10]
    n = len(arr1)
    m = len(arr2)
    k = 5
    
    print(f"Brute force result: {kthElement_brute(arr1, arr2, n, m, k)}")
    print(f"Better approach result: {kthElement_better(arr1, arr2, n, m, k)}")
    print(f"Optimal approach result: {kthElement_optimal(arr1, arr2, n, m, k)}")
