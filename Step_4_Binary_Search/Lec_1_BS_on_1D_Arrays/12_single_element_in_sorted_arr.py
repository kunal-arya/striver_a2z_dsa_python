'''
# **Part 1: Main Header Documentation**

# **1. Problem Statement:**
# You are given a sorted array consisting of only integers where every element appears
# exactly twice, except for one element which appears exactly once. Find this single
# element that appears only once.

# **2. Brute-force Approach (as in `singleElBrute`):**
# A simple approach is to iterate through the array and check the neighbors of each element.
# - If an element `arr[i]` is not equal to `arr[i-1]` and not equal to `arr[i+1]`, it must
#   be the single element.
# - Special checks are needed for the first (`i=0`) and last (`i=n-1`) elements.
# - Time Complexity: O(n), as we scan the array.
# - Space Complexity: O(1).

# **3. Better Approach (XOR):**
# A very clever linear-time solution uses the XOR bitwise operator.
# - The XOR property `a ^ a = 0` means that any number XORed with itself cancels out.
# - The property `a ^ 0 = a` means any number XORed with zero remains unchanged.
# - If we XOR all elements in the array, all the duplicate pairs will cancel each other
#   out (`arr[i] ^ arr[i] = 0`), leaving only the single, non-duplicated element.
# - **Example:** `[1,1,2,3,3] -> (1^1)^(3^3)^2 -> 0^0^2 -> 2`.
# - Time Complexity: O(n).
# - Space Complexity: O(1).

# **4. Optimal Approach (Binary Search, as in `singleElOp`):**
# Since the array is sorted, we can achieve O(log n) complexity. This solution relies on
# a key observation about the indices of the paired elements.

# **4.1. Intuition & Observation:**
# - Before the single element, the pairs follow a strict pattern: the first instance of a
#   pair is at an **even** index, and the second is at the next **odd** index.
#   - Example: `[1, 1, 2, 2, ...]`. `1` is at `(0, 1)`. `2` is at `(2, 3)`.
# - After the single element, this pattern is disrupted. The first instance of a pair
#   will be at an **odd** index, and the second at the next **even** index.
#   - Example: `[..., 4, 5, 5, 6, 6]`. `5` is at `(5, 6)`. `6` is at `(7, 8)`.
# - We can use binary search to find this "breaking point". At any `mid`, we can check if
#   the pattern is still intact. If it is, the single element must be to the right. If
#   it's broken, the single element is at or to the left of our current position.

# **4.2. Step-by-step Approach:**
#   1.  Handle edge cases first: if `n=1`, return `arr[0]`. If the single element is at
#       the very start (`arr[0] != arr[1]`) or end (`arr[n-1] != arr[n-2]`), return it.
#       This simplifies the main loop by allowing us to search within `low=1, high=n-2`.
#   2.  Loop while `low <= high`.
#   3.  Calculate `mid`. If `arr[mid]` is not equal to its neighbors, it's the single
#       element. Return it.
#   4.  **Check the index pattern:** We need to check `mid`'s partner.
#       - If `mid` is **odd**, its partner should be at `mid-1`.
#       - If `mid` is **even**, its partner should be at `mid+1`.
#   5.  **Decision:**
#       - If `mid` and its partner are the same (`arr[mid] == arr[partner]`), the pair is
#         intact. This means we are in the "good" left half where the (even, odd) pattern
#         holds. The single element must be to our right. So, we eliminate the left half:
#         `low = mid + 1`.
#       - If `mid` and its partner are different, the pattern is broken. The single element
#         is either `mid` or to its left. So, we eliminate the right half: `high = mid - 1`.
#   6.  The loop will eventually converge on the single element.

# **4.3. Dry Run:**
# `arr = [1, 1, 2, 2, 3, 4, 4]`
# - **Initial:** `low=1`, `high=5`.
# - **Step 1:** `mid=3`. `arr[3]=2`. `arr[3]` is not the single element.
#   - `mid` is odd. Its partner is at `mid-1=2`. `arr[3](2) == arr[2](2)`.
#   - The pair `(2,2)` is intact. We are in the good left half. Search right: `low = mid + 1 = 4`.
# - **Step 2:** `low=4`, `high=5`. `mid=4`. `arr[4]=3`.
#   - `arr[4]` is not equal to `arr[3]` and not equal to `arr[5]`.
#   - Wait, `arr[5]` is 4. `arr[4]` is not equal to `arr[5]`.
#   - Let's re-check the logic. `arr[mid] != arr[mid-1]` and `arr[mid] != arr[mid+1]`.
#   - `arr[4](3)` vs `arr[3](2)` and `arr[5](4)`. Yes, `3` is the single element. Return `arr[4]`.
#   - My dry run was slightly off, the user's code is correct. Let's trace the user's logic:
#   - `mid=4`. `arr[4]=3`. `arr[4] != arr[3]` and `arr[4] != arr[5]`. Return `arr[4]`. Correct.

# **7. Time Complexity:**
# - Brute Force: O(n)
# - XOR: O(n)
# - Binary Search: O(log n)

# **8. Space Complexity:**
# - All three approaches use O(1) space.
'''
# Brute Approach
def singleElBrute(arr):
    n = len(arr)

    # If there's only one element, it must be the single one
    if n == 1:
        return arr[0]
    
    for i in range(n):
        # Check first element
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        # Check last element
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        # Check middle elements
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]
            
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(f"Brute Force Result: {singleElBrute(arr)}")


# Optimal Approach (Binary Search)
def singleElOp(arr):
    n = len(arr)

    # Handle single-element array
    if n == 1:
        return arr[0]
    
    # Check if the single element is at the start
    if arr[0] != arr[1]:
        return arr[0]
    
    # Check if the single element is at the end
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    
    # Search in the reduced space, excluding the checked ends
    low = 1
    high = n - 2

    while low <= high:
        mid = low + (high - low) // 2

        # If arr[mid] is the single element, it won't match its neighbors
        if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
            return arr[mid]

        # We are in the left half (pattern is intact), so the single element is on the right.
        # This condition checks if we are on an (even, odd) pair.
        # If mid is odd, its partner is mid-1. If mid is even, its partner is mid+1.
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or \
           (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half
            low = mid + 1
        # We are in the right half (pattern is broken), so the single element is on the left.
        else:
            # Eliminate the right half
            high = mid - 1

    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(f"Optimal Solution Result: {singleElOp(arr)}")
'''
# **Part 3: Footer Documentation**

# **1. Edge Cases to Consider:**
# - **Single element at the start or end:** Your code handles this perfectly by checking
#   the boundaries before starting the main binary search loop. This is a great optimization.
# - **Array with only one element:** Handled.
# - **Array with three elements:** The boundary checks and the loop logic will correctly
#   find the single element.

# **2. Common Follow-up Questions & Variations:**
# 1.  **Why did you start the search from `low=1` and `high=n-2`?** This is a clever
#     optimization. By handling the two edge cases (single element at `arr[0]` or `arr[n-1]`)
#     before the loop, we guarantee that any element we check inside the loop will always
#     have a `mid-1` and `mid+1` to compare against, which simplifies the code.
# 2.  **Could the logic be simplified inside the loop?** Yes. A common alternative is to
#     always ensure `mid` is at an even index before checking its partner.
#     ```python
#     # Inside while loop:
#     mid = low + (high - low) // 2
#     if mid % 2 == 1:
#         mid -= 1 # Ensure we are at the start of a pair
#     if arr[mid] == arr[mid + 1]:
#         low = mid + 2 # Pair is good, search right
#     else:
#         high = mid # Pattern broken, search left
#     ```
#     This is another way to frame the same core logic.
# 3.  **What if the array wasn't sorted?** If the array were unsorted, the binary search
#     would not work. The XOR approach (O(n) time, O(1) space) or a hash map (O(n) time,
#     O(n) space) would be the best solutions.
'''