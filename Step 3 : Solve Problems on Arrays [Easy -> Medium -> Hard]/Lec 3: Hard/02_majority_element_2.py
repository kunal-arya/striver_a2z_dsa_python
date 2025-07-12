from typing import List

# Problem: Find all elements that appear more than n/3 times in an array.

# Observation
# If you try to count how many majority elements an array can have such that they appear more than n/3 times, the answer is at most two. [3]
# Intuition: Let's say you have an array of size n=9. The threshold is 9/3 = 3. A majority element must appear at least 4 times.
# Can you have three such elements? If you had elements A, B, and C, each appearing 4 times, you would need 4 + 4 + 4 = 12 spots in the array.
# But the array only has 9 spots. This is a contradiction. Therefore, you can have a maximum of two such majority elements. [4]

# Brute Force Approach
# Time Complexity => O(n^2)
# Space Complexity => O(1) (excluding the space for the answer)
def majorityElBrute(arr: List[int]) -> List[int]:
    # Intuition: The most straightforward way is to pick each element and simply count its occurrences.
    # We can use two nested loops. The outer loop picks a number, and the inner loop counts how many times it appears.
    ans: List[int] = []
    n = len(arr)
    threshold = n // 3

    # Visual Explanation:
    # 1. Iterate through each element `arr[i]` of the array.
    # 2. Before counting, check if we have already found this element to avoid duplicates in the `ans` list.
    # 3. If it's a new number, start a second loop (from `j` to `n`) to count its total occurrences (`sum`).
    # 4. After counting, if `sum` is greater than the `n/3` threshold, add it to our answer.
    # 5. As a small optimization, since we know there can be at most two such elements, we can break early if we find them.
    for i in range(n):
        # Check if the element is already in the answer list to avoid recounting.
        if len(ans) == 0 or ans[0] != arr[i]:
            count = 0
            for j in range(n):
                if arr[i] == arr[j]:
                    count += 1
            
            if count > threshold:
                ans.append(arr[i])

        # Optimization: If we've found two majority elements, we can stop.
        if len(ans) == 2:
            break
    
    return ans

arr = [1, 1, 1, 3, 3, 2, 2, 2]
# Visual Dry Run for Brute Force with arr = [1, 1, 1, 3, 3, 2, 2, 2], n=8, threshold=2
# i=0, arr[0]=1. Not in ans. Inner loop counts three 1s. 3 > 2, so ans becomes [1].
# i=1, arr[1]=1. Already in ans (ans[0] == arr[1]), so skip.
# i=2, arr[2]=1. Already in ans, skip.
# i=3, arr[3]=3. Not in ans. Inner loop counts two 3s. 2 is not > 2, so do nothing.
# i=4, arr[4]=3. Not in ans. Inner loop counts two 3s. 2 is not > 2, do nothing.
# i=5, arr[5]=2. Not in ans. Inner loop counts three 2s. 3 > 2, so ans becomes [1, 2].
# Now len(ans) is 2, so we break the loop.
# Final Answer: [1, 2]
print(f"Brute Force Result: {majorityElBrute(arr)}")

# Better Solution ( Hashing )
# Time Complexity => O(n) because we iterate through the array once to count and potentially once more over the hash map.
# Space Complexity => O(n) in the worst case, where all elements are unique and stored in the hash map.
def majorityElBetter(arr: List[int]) -> List[int]:
    # Intuition: Instead of recounting for each element, we can use extra space to be more time-efficient.
    # A hash map (or dictionary in Python) is perfect for storing element frequencies.
    # Visual Explanation:
    # 1. Create an empty hash map to store counts: `hash = {element: frequency}`.
    # 2. Iterate through the array once. For each number:
    #    - If the number is in the map, increment its count.
    #    - If it's not, add it to the map with a count of 1.
    # 3. After counting everything, iterate through the map.
    # 4. For each key-value pair, check if the value (frequency) is greater than `n/3`.
    # 5. If it is, add the key (the element) to your answer list.
    n = len(arr)
    threshold = n // 3
    hash_map = {}
    ans = []

    for num in arr:
        hash_map[num] = hash_map.get(num, 0) + 1

    for num, count in hash_map.items():
        if count > threshold:
            ans.append(num)
        # Your original code had an early break condition inside the first loop.
        # This is more accurate: build the full frequency map first, then check.
    
    return ans

arr = [1, 1, 1, 3, 3, 2, 2, 2]
# Visual Dry Run for Better Solution with arr = [1, 1, 1, 3, 3, 2, 2, 2], n=8, threshold=2
# 1. After first loop, hash_map = {1: 3, 3: 2, 2: 3}.
# 2. Second loop iterates through the map:
#    - num=1, count=3. Is 3 > 2? Yes. ans becomes [1].
#    - num=3, count=2. Is 2 > 2? No.
#    - num=2, count=3. Is 3 > 2? Yes. ans becomes [1, 2].
# Final Answer: [1, 2]
print(f"Better Solution Result: {majorityElBetter(arr)}")

# Optimal Solution (Extended Boyer-Moore Voting Algorithm)
# Time Complexity => O(n). The algorithm iterates through the array twice in the worst case.
# Space Complexity => O(1). We only use a few variables to store candidates and their counts. [6, 7]
def majorityElOp(arr: List[int]) -> List[int]:
    # Intuition: This is an extension of the Boyer-Moore Voting algorithm. [1, 3] The core idea is "vote cancellation".
    # Since we're looking for up to two candidates, we use two counters and two candidate variables. [5]
    # If we see a number that matches a candidate, we increment its vote.
    # If we see a different number, we decrement *both* candidates' votes.
    # This works because if two elements truly have a high frequency, they will "survive" this cancellation process.
    # A number that isn't a majority element will have its vote canceled out by the others.
    
    # Visual Explanation:
    # Part 1: Finding the two best candidates.
    # 1. Initialize two candidates (el1, el2) and their counts (count1, count2) to zero.
    # 2. Iterate through the array. For each number `num`:
    #    - If `num` is el1, increment count1.
    #    - If `num` is el2, increment count2.
    #    - If count1 is 0, make `num` the new el1 and set count1 to 1.
    #    - If count2 is 0, make `num` the new el2 and set count2 to 1.
    #    - If the number is different from both candidates, decrement both counts.
    # At the end of this pass, el1 and el2 hold the *potential* majority elements. But they are not guaranteed.
    
    # Part 2: Verifying the candidates.
    # 3. The first pass only gives us candidates; they might not actually appear > n/3 times.
    # 4. We must iterate through the array a second time to get the *actual* counts of el1 and el2.
    # 5. Finally, check if their actual counts are greater than n/3 and add them to the answer if they are.
    
    el1, el2 = float("-inf"), float("-inf")
    count1, count2 = 0, 0

    # Visual Dry Run (Part 1) for arr = [1, 1, 1, 3, 3, 2, 2, 2]
    # num=1: count1=0, el1 becomes 1, count1 becomes 1. (el1=1, c1=1, el2=-inf, c2=0)
    # num=1: el1==num, count1 becomes 2. (el1=1, c1=2, el2=-inf, c2=0)
    # num=1: el1==num, count1 becomes 3. (el1=1, c1=3, el2=-inf, c2=0)
    # num=3: count2=0, el2 becomes 3, count2 becomes 1. (el1=1, c1=3, el2=3, c2=1)
    # num=3: el2==num, count2 becomes 2. (el1=1, c1=3, el2=3, c2=2)
    # num=2: different, decrement both. c1 becomes 2, c2 becomes 1. (el1=1, c1=2, el2=3, c2=1)
    # num=2: different, decrement both. c1 becomes 1, c2 becomes 0. (el1=1, c1=1, el2=3, c2=0)
    # num=2: count2=0, el2 becomes 2, count2 becomes 1. (el1=1, c1=1, el2=2, c2=1)
    # End of Part 1: Our candidates are el1=1 and el2=2.
    for num in arr:
        if count1 == 0 and num != el2:
            el1 = num
            count1 = 1
        elif count2 == 0 and num != el1:
            el2 = num
            count2 = 1
        elif el1 == num:
            count1 += 1
        elif el2 == num:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # Visual Dry Run (Part 2) for el1=1, el2=2, n=8, threshold=2
    # Reset counts to 0.
    count1, count2 = 0, 0
    # Iterate through array again to get real counts of 1 and 2.
    # Final counts: count1 = 3 (for el1=1), count2 = 3 (for el2=2).
    for num in arr:
        if num == el1:
            count1 += 1
        
        if num == el2:
            count2 += 1
    
    n = len(arr)
    threshold = n // 3
    ans = []
    
    # Check if the counts are sufficient.
    # For el1=1: is count1 (3) > threshold (2)? Yes. Add 1 to ans. ans = [1].
    # For el2=2: is count2 (3) > threshold (2)? Yes. Add 2 to ans. ans = [1, 2].
    if count1 > threshold:
        ans.append(el1)
    
    if count2 > threshold:
        ans.append(el2)

    return ans

arr = [1, 1, 1, 3, 3, 2, 2, 2]
print(f"Optimal Solution Result: {majorityElOp(arr)}")