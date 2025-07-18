"""
Find the Smallest Divisor Given a Threshold
LINK: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
Example 2:

Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 106
nums.length <= threshold <= 106
"""
import math

# Helper Function
def isSumPossibleDiv(arr,t,divisor):
    sum = 0
    
    for i in range(len(arr)):
        sum += math.ceil(arr[i] / divisor)
    
    return sum <= t

# Brute Approach
def findSmallestDivisorBrute(arr,t):
    high = max(arr)

    for divisor in range(1,high + 1):
        if isSumPossibleDiv(arr,t,divisor):
            return divisor
        
    return -1

arr = [1,2,5,9]
threshold = 6

arr2 = [44,22,33,11,1]
threshold2 = 5

print(findSmallestDivisorBrute(arr,threshold))
print(findSmallestDivisorBrute(arr2,threshold2))


# Optimal Approach
def findSmallestDivisorOp(arr, t):
    low = 1
    high = max(arr)
    n = len(arr)

    # Not Possible Scenerio
    if t < n:
        return -1
    
    while low <= high:
        mid = low + (high - low) // 2

        if isSumPossibleDiv(arr,t,mid):
            high = mid - 1
        else:
            low = mid + 1

    return low

print(findSmallestDivisorOp(arr,threshold))
print(findSmallestDivisorOp(arr2,threshold2))