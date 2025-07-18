from typing import List

# Problem: Given an integer array, find all the unique triplets [arr[i], arr[j], arr[k]]
# such that i != j, i != k, and j != k, and their sum is equal to zero. [1]

# Brute Solution
# Time Complexity => O(n^3) for the three nested loops, plus the time to sort each triplet before insertion into the set. [4, 15]
# Space Complexity => O(number of unique triplets) to store the result in the set.

    # Observation: The most straightforward way to find all triplets is to check every possible combination of three distinct elements in the array. [8, 15]
    # Inuition: Use three nested loops to iterate through all possible combinations of i, j, and k. [8, 16]
    # To handle the "unique triplets" requirement, a set is used. A set only stores unique elements.
    # Since lists are mutable and cannot be added to a set, we sort each found triplet and convert it to an immutable tuple before adding it.

    # Visual Explanation:
    # Loop i from the start of the array.
    #   Loop j starting from the element after i.
    #     Loop k starting from the element after j.
    #       - This structure (i, i+1, j+1) ensures we always have three distinct indices.
    #       - Check if arr[i] + arr[j] + arr[k] == 0.
    #       - If it is, sort the triplet to create a canonical representation (e.g., [2, -1, -1] and [-1, 2, -1] both become [-1, -1, 2]).
    #       - Add this canonical, tuple form to the set to automatically handle duplicates.
def threeSumBrute(arr: List[int]) -> List[List[int]]:

    n = len(arr)
    set_h = set()


    for i in range(n):
        for j in range(i + 1,n):
            for k in range(j + 1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    new = [arr[i],arr[j],arr[k]]
                    new.sort()
                    # we are converting list into tuples, 
                    # b/c tuples are immutable and hashing is not allowed on mutables like List in Python
                    set_h.add(tuple(new))

    return [list(triplets) for triplets in set_h]

arr = [-1,0,1,2,-1,-4]
# Visual Dry Run for arr = [-1, 0, 1, 2, -1, -4]
# i=0 (arr[i]=-1), j=1 (arr[j]=0), k=2 (arr[k]=1) -> sum is 0. Add (-1, 0, 1) to set.
# i=0 (arr[i]=-1), j=3 (arr[j]=2), k=4 (arr[k]=-1) -> sum is 0. Sort to [-1,-1,2]. Add (-1, -1, 2) to set.
# ... many other combinations are checked ...
# The set automatically prevents adding `(-1, 0, 1)` again if we find `(0, 1, -1)`.

# we are converting tuples back to list before returning
# b/c return result should be => List[List[int]]

print(f"Brute Force Result: {threeSumBrute(arr)}")

# Better Approach
# Time Complexity => O(n^2) for the nested loops. The hash set operations (add, in) take average O(1) time. [10]
# Space Complexity => O(n) for the inner `hash_set` and O(number of triplets) for the `res` set.

# Observation: We can reduce the number of loops from three to two.
# Inuition: If we fix two numbers, `arr[i]` and `arr[j]`, the third number must be `-(arr[i] + arr[j])`. [10]
# Instead of a third loop to search for this third number, we can use a hash set for an efficient O(1) average time lookup.

# Visual Explanation:
# Loop i from the start of the array. This fixes the first element of a potential triplet.
#   For each i, create an empty hash_set.
#   Loop j from i+1. This is the second element of a potential triplet.
#     - Calculate the required third element: `third_num = -(arr[i] + arr[j])`.
#     - Check if `third_num` exists in our `hash_set`.
#       - If it does, we have found a valid triplet: (arr[i], arr[j], third_num). Add its sorted tuple form to the result set.
#     - Add the current `arr[j]` to the `hash_set` for subsequent `j`'s to use.

def threeSumBetter(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    res = set()

    for i in range(n):
        hash_set = set()
        for j in range(i + 1,n):
            third_num = - (arr[i] + arr[j])

            if third_num in hash_set:

                new = [arr[i], arr[j], third_num]
                new.sort()
                res.add(tuple(new))
            
            hash_set.add(arr[j])
    
    return [list(triplets) for triplets in res]
        
arr = [-1,0,1,2,-1,-4]

# Visual Dry Run for arr = [-1, 0, 1, 2, -1, -4]
# i=0 (arr[i]=-1):
#   hash_set = {}.
#   j=1 (arr[j]=0): third_num = -(-1+0) = 1. Is 1 in hash_set? No. Add 0 to hash_set. hash_set={0}.
#   j=2 (arr[j]=1): third_num = -(-1+1) = 0. Is 0 in hash_set? Yes. Add sorted([-1,1,0]) -> (-1,0,1) to res. Add 1 to hash_set. hash_set={0,1}.
#   j=3 (arr[j]=2): third_num = -(-1+2) = -1. Is -1 in hash_set? No. Add 2 to hash_set. hash_set={0,1,2}.
#   ...and so on.

print(f"Better Approach Result: {threeSumBetter(arr)}")

# Optimal Approach
# Time Complexity => O(n log n) for the initial sort, plus O(n^2) for the loop with two pointers. Overall: O(n^2). [3, 9]
# Space Complexity => O(number of triplets) for the result list. We don't use significant extra space besides the answer. [12]
    
    # Observation: If the array is sorted, we can efficiently search for the other two elements.
    # Inuition: This approach transforms the problem into a "2Sum" problem for each element. First, sort the array. [2, 11]
    # Then, iterate through the array with a fixed pointer `i`. For each `arr[i]`, find two other numbers in the rest of the array
    # that sum up to `-arr[i]`. This subproblem can be solved in linear time using a two-pointer approach (one pointer `j` starting from `i+1`,
    # one pointer `k` starting from the end). [4, 9]

    # Visual Explanation:
    # 1. Sort the array: `[-4, -2, -2, -1, -1, 0, 0, 2, 2, 2]`
    # 2. Loop `i` from 0 to n-1. This is our first fixed number.
    #    - To avoid duplicate triplets, if `arr[i]` is the same as `arr[i-1]`, we skip it.
    # 3. For each `i`, set up two pointers: `j = i + 1` and `k = n - 1`.
    # 4. Loop while `j < k`:
    #    - Calculate the sum `arr[i] + arr[j] + arr[k]`.
    #    - If sum < 0, we need a larger sum, so move the left pointer forward: `j += 1`.
    #    - If sum > 0, we need a smaller sum, so move the right pointer backward: `k -= 1`.
    #    - If sum == 0, we found a triplet! Add it to the result.
    #      - Now, to skip duplicates for `j` and `k`, increment `j` while it's equal to the previous `j`,
    #        and decrement `k` while it's equal to the next `k`. Then move both pointers inward. [7, 13]
def threeSumOp(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    res = []

    arr.sort() # O(n log n)


    for i in range(n):
        # Skip positive fixed numbers, as the sum can't be zero.
        if arr[i] > 0:
            break
        # Skip duplicate fixed numbers
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        j = i + 1
        k = n - 1

        while j < k:
            triplets_sum = arr[i] + arr[j] + arr[k]
            if triplets_sum < 0:
                j += 1
            elif triplets_sum > 0:
                k -= 1
            else: # triplets_sum == 0
                res.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1

                # increase j till j is not equal to previous element to avoid duplicates
                while j < k and arr[j] == arr[j - 1]:
                    j += 1

                # decrease k till k is not equal to next element to avoid duplicates
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
    return res


arr = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
# Visual Dry Run for arr = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2] after sorting.
# Sorted: [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
# i=0 (arr[i]=-2): j=1, k=12. sum = -2 + -2 + 2 = -2 (<0). j++.
#   ... j moves ...
#   j=9, k=12. sum = -2 + 2 + 2 = 2 (>0). k--.
#   j=9, k=11. sum = -2 + 2 + 2 = 2 (>0). k--.
#   j=9, k=10. sum = -2 + 2 + 2 = 2 (>0). k--.
#   j=9, k=9. j is not less than k, inner loop ends for i=0.
# Wait, let's re-run for a successful case.
# Sorted arr = [-4, -1, -1, 0, 1, 2]
# i=0 (arr[i]=-4): No pair (j, k) sums to 4.
# i=1 (arr[i]=-1):
#   j=2, k=5. sum = -1 + -1 + 2 = 0. Found a triplet! res=[[-1,-1,2]].
#   j becomes 3, k becomes 4.
#   Skip duplicates: arr[j](0) != arr[j-1](-1). No skip.
#   j=3, k=4. sum = -1 + 0 + 1 = 0. Found a triplet! res=[[-1,-1,2], [-1,0,1]].
#   j becomes 4, k becomes 3. j is not less than k, inner loop ends.
# i=2 (arr[i]=-1): This is a duplicate of arr[i-1], so we `continue` and skip it.
# i=3 (arr[i]=0): arr[i] is not > 0.
# ... and so on.

print(f"Optimal Approach Result: {threeSumOp(arr)}")