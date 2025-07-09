
# Brute Approach

def printMaxSubArrarySumBrute(arr):
    n = len(arr)
    maxSum = 0
    start = 0
    end = 0

    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j + 1):
                sum += arr[k]
            if sum > maxSum:
                maxSum = sum
                start = i
                end = j
    
    maxSub = []
    while start <= end:
        maxSub.append(arr[start])
        start += 1

    return maxSub

arr = [-2,-3,4,-1,-2,1,5,-3]
print(f"Brute Force Result: {printMaxSubArrarySumBrute(arr)}") # Expected: ([4,-1,-2,1,5])

# Better Approach
def printMaxSubArraySumBetter(arr):
    n = len(arr)

    maxSum, start, end = 0, 0, 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

            if sum > maxSum:
                maxSum = sum
                start = i
                end = j
        
    maxSub = []

    while start <= end:
        maxSub.append(arr[start])
        start += 1

    return maxSub

arr = [-2,-3,4,-1,-2,1,5,-3]
print(f"Better Result: {printMaxSubArraySumBetter(arr)}") # Expected: ([4,-1,-2,1,5])


# Optimised Approach ( because brute force and better approach can be seen from Sno-4)
def printMaxSubArraySumOp(arr):
    n = len(arr)
    sum = 0
    maxSum = float('-inf')
    finalStart, finalEnd, start = 0,0,0

    for i in range(n):
        if sum == 0: start = i
        
        sum += arr[i]
        if maxSum < sum:
            maxSum = sum
            finalStart = start
            finalEnd = i

        if sum < 0:
            sum = 0
    
    maxSub = []

    while finalStart <= finalEnd:
        maxSub.append(arr[finalStart])
        finalStart += 1

    return maxSub

arr = [-2,-3,4,-1,-2,1,5,-3]
print(f"Optimised Result: {printMaxSubArraySumOp(arr)}") # Expected: ([4,-1,-2,1,5])
        
    