from typing import List

# Brute Force
def countSubArrayxorK(arr: List[int], target: int) -> int:
    n = len(arr)

    count = 0
    # Observation: We need to check all possible subarrays.
    # Intuition: A straightforward way is to use three nested loops.
    # The outer two loops define the start and end of the subarray.
    # The innermost loop calculates the XOR sum of the current subarray.
    for i in range(n):
        for j in range(i,n):
            XOR = 0
            for k in range(i,j + 1):
                XOR ^= arr[k]
            
            if XOR == target:
                count += 1

    return count

arr = [4, 2, 2, 6, 4]
target = 6

print(countSubArrayxorK(arr,target))

# Better Force
def countSubArrayxorKBetter(arr: List[int], target: int) -> int:
    n = len(arr)

    count = 0

    # Observation: The innermost loop in the brute force is redundant.
    # Intuition: We can calculate the XOR sum of the subarray [i...j] efficiently
    # by extending the XOR sum from the previous subarray [i...j-1].
    # When j increments, we just XOR with arr[j].
    for i in range(n):
        XOR = 0
        for j in range(i,n):
            XOR ^= arr[j] # Calculate XOR for subarray arr[i...j]

            if XOR == target:
                count += 1
    
    return count

arr = [4, 2, 2, 6, 4]
target = 6

print(countSubArrayxorKBetter(arr,target))

# Optimal Approach

def countSubArrayxorKOp(arr: List[int], k: int) -> int:
    n = len(arr)
    # Observation: The problem can be rephrased in terms of prefix XORs.
    # Intuition: Similar to how prefix sums are used for sum problems,
    # prefix XORs can be used for XOR problems.
    # Let XOR[i] be the XOR sum of elements from arr[0] to arr[i].
    # The XOR sum of a subarray arr[j...i] can be found as XOR[i] ^ XOR[j-1].
    # We are looking for subarrays where XOR[i] ^ XOR[j-1] == k.
    # Rearranging this, we get XOR[j-1] = XOR[i] ^ k.
    # So, for each current prefix XOR (XOR[i]), we need to find how many
    # previous prefix XORs (XOR[j-1]) exist such that XOR[j-1] == XOR[i] ^ k.
    # We use a hash map (dictionary in Python) to store the frequency of prefix XORs encountered so far.

    # Initialize prefixSum map (or prefixXOR map in this context) with {0: 1}.
    # This handles the case where a subarray starting from index 0 itself has XOR sum 'k'.
    # If current_XOR ^ k == 0, it means current_XOR == k, and since we consider a prefix XOR of 0
    # before any elements, it accounts for the subarray from index 0 to current index.
    prefixSum = {0:1} 
    XOR = 0 # This variable will store the current prefix XOR.
    count = 0 # This will store the total count of subarrays with XOR sum k.

    for i in range(n):
        XOR = XOR ^ arr[i] # Calculate the prefix XOR up to the current element.

        x = XOR ^ k # This is the 'XOR[j-1]' we are looking for.

        if x in prefixSum: # If 'XOR[j-1]' exists in our map, it means we found 'prefixSum[x]' subarrays
                          # ending at current 'i' that have an XOR sum of 'k'.
            count += prefixSum[x]
        
        # Store the current prefix XOR in the map.
        # If it's already there, increment its frequency. Otherwise, add it with frequency 1.
        if XOR in prefixSum:
            prefixSum[XOR] += 1
        else:
            prefixSum[XOR] = 1
    
    return count
        
arr = [4, 2, 2, 6, 4]
target = 6

print(countSubArrayxorKOp(arr,target))