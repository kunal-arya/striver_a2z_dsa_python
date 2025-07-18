from typing import List

# AI please explain what is Pascal Triangle First
#
# # Pascal's Triangle: A Quick Overview
#
# ## What is it?
# # Observation: Pascal's Triangle is a triangular array of numbers that has a unique, symmetrical structure. [1]
# # It's named after the French mathematician Blaise Pascal, though it was studied centuries earlier in other parts of the world. [5]
#
# # The structure looks like this:
# #        1
# #       1 1
# #      1 2 1
# #     1 3 3 1
# #    1 4 6 4 1
# #   1 5 10 10 5 1
# #  ...and so on, infinitely.
#
# ## How is it built?
# # Inuition: The rule for creating the triangle is simple. [3]
# # 1. It starts with a single '1' at the very top.
# # 2. Every row after that also starts and ends with a '1'.
# # 3. Any other number in the triangle is the sum of the two numbers directly above it. [2]
# #    - For example, in the 4th row (1 4 6 4 1), the '6' is the sum of the '3' and '3' from the row above it.
#
# ## Why is it useful?
# # Observation: The numbers in Pascal's triangle are not random; they are "binomial coefficients". [2]
# # - The numbers in the 'n-th' row (starting our count from 0) are the coefficients of the expanded form of (x + y)^n. [2, 5]
# #   - (x+y)^2 = 1x^2 + 2xy + 1y^2. The coefficients are 1, 2, 1, which is the 2nd row of the triangle.
# #   - (x+y)^3 = 1x^3 + 3x^2y + 3xy^2 + 1y^3. The coefficients are 1, 3, 3, 1, which is the 3rd row.
# # - It is also deeply connected to combinatorics and probability. The element at row 'n' and column 'r' (nCr) tells you how many ways you can choose 'r' items from a set of 'n' items. [4]

# Three Types of questions can come related to Pascal Triangle:
# First Type => Given Row and Column, find the element at that place, ex => row = 5, column = 3 - ans => 6
# Second Type => Print any nth row of the pascal triangle
# Third Type => Given N, Print the entire Pascal Triangle

# First Type
# Brute Force Approach

# Simple Maths Formula to get the element given row and column
# (row - 1) Combination of (column - 1)
# Formula for combination of n and r => n! / r! * (n - r)!
# Time Complexity => O(n) + O(r) + O(n - r) => O(n) because of the factorial calculations.
# Space Complexity => O(1)
def pascalTriangleBrute(row: int, column: int):
    # nCr Formula => n! / r! * (n - r)!
    # We use (row - 1) and (column - 1) because Pascal's triangle is often 0-indexed.
    # The 5th row is technically row n=4.
    n = row - 1
    r = column - 1
    return nCrBrute(n,r)
    

def nCrBrute(n: int, r: int):
    # Observation: This approach directly implements the mathematical formula nCr = n! / (r! * (n-r)!).
    # Intuition: Calculating the full factorials is straightforward but computationally expensive.
    # It can also lead to integer overflow for relatively small values of n.
    nFactorial = findFactorial(n)
    rFactorial = findFactorial(r)
    nMinusrFactorial = findFactorial(n - r)
    return  nFactorial // (rFactorial * nMinusrFactorial)
def findFactorial(n: int):
    # This is a recursive function to find the factorial.
    # Base case: Factorial of 0 or 1 is 1.
    if n == 0 or n == 1:
        return 1
    # Recursive step: n! = n * (n-1)!
    return n * findFactorial(n - 1)

print(f"Type 1 (Brute): Element at row 5, col 3 is {pascalTriangleBrute(5,3)}")

# Optimal Approach
# so, if u carefully observe n! / r! * (n - r)!
# n * (n - 1) * .... * (n - r)! / r! * (n - r)!
# n - r! from denominator and numerator cancelled each other
# n * (n - 1) * ... * (n - r + 1) / r!
# Time Complexity => O(r) or O(column)
# Space complexity => O(1)
def pascalTriangleBetter(row: int, column: int):
    return nCr(row - 1,column - 1)

# AI please explain this part in depth for future reference
def nCr(n: int, r: int):
    # Observation: We can compute nCr without calculating large factorials.
    # The formula nCr is n! / (r! * (n-r)!).
    # This can be expanded to: [n * (n-1) * ... * (n-r+1)] / [r * (r-1) * ... * 1].
    #
    # Intuition: Instead of calculating the numerator and denominator separately, we can
    # calculate the result iteratively. This avoids large intermediate numbers and potential overflow.
    # The loop calculates (n/1), then multiplies by ((n-1)/2), then by ((n-2)/3), and so on, 'r' times.
    res = 1

    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
        # Visual Dry Run for nCr(4, 2) which is the element at row=5, col=3
        # n = 4, r = 2. Expected output: 6
        #
        # Initial: res = 1
        #
        # i = 0:
        #   res = res * (4 - 0) => 1 * 4 = 4
        #   res = res // (0 + 1) => 4 // 1 = 4
        #   Current res = 4. (This is 4C1)
        #
        # i = 1:
        #   res = res * (4 - 1) => 4 * 3 = 12
        #   res = res // (1 + 1) => 12 // 2 = 6
        #   Current res = 6. (This is 4C2)
        #
        # Loop ends. Return res = 6.
    return res

print(f"Type 1 (Optimal): Element at row 5, col 3 is {pascalTriangleBetter(5,3)}")


# Second Type of Problem

# Observations
# 1. The Nth row will have N elements. (For 1-based indexing).
# 2. The row is symmetric.
# 3. The first and last elements are always 1.

# Brute Force Approach
# Intuition: To get a whole row, we can just find each element individually.
# We can loop from column 1 to 'row' and call our optimal `nCr` function for each element.
# Time Complexity => O(row * r) where r is the average column index. Effectively O(row^2).
# Space Complexity => O(row) to store the answer list.
def printNthRow(row: int):
    # because of our observation => Nth row will have N elements
    ans = []
    # Loop through each column of the desired row
    for i in range(1,row + 1):
        # Calculate the element using the combination formula and add to the list
        ans.append(nCr(row -1, i - 1))

    return ans

print(f"Type 2 (Brute): Row 5 is {printNthRow(5)}")

# Optimal Approach
# Intuition: Each element in a row can be calculated from the *previous element* in the SAME row. [8]
# Let's look at the formula for two adjacent elements:
# nCr     = n! / (r! * (n-r)!)
# nC(r+1) = n! / ((r+1)! * (n-r-1)!)
#
# If we look at the ratio nC(r+1) / nCr, we find it simplifies to (n-r) / (r+1).
# So, nC(r+1) = nCr * (n-r) / (r+1).
# This means we can calculate the next element from the current one with a simple multiplication and division.
# This avoids recalculating combinations from scratch.
#
# The user's formula `sumTillPreviousColumn * (row - column) / column` correctly captures this relationship.
#
# Time Complexity => O(n) because we iterate through the row only once. [8, 10]
# Space Complexity => O(n) to store the result list.
def printNthRowOp(row: int):
    # This represents the row number in 0-indexed terms
    n = row -1
    # The first element is always 1 (nC0)
    ans = 1
    result = [ans]

    # Visual Explanation: We start with the first element (1). Then we walk across the row.
    # To get the 2nd element, we apply the formula to the 1st. To get the 3rd, we apply it to the 2nd, and so on.
    # This builds the row in a single pass.

    # Visual Dry Run for printNthRowOp(6), which is the 5th row (0-indexed). n = 5.
    # Initial: n=5, ans=1, result=[1]
    #
    # Loop for i from 1 to 5:
    # i = 1 (calculating 5C1):
    #   ans = ans * (5 - 1 + 1) / 1 => 1 * 5 / 1 = 5
    #   (Using user's formula) ans = ans * (n-i) / i => 1 * (5-0)/1 = 5 (adjusting loop variable)
    #   Let's use the code's logic:
    #   ans = ans * (n - (i-1)) => 1 * (5 - 0) = 5
    #   ans = ans // i          => 5 // 1 = 5
    #   result.append(5) => result is [1, 5]
    #
    # i = 2 (calculating 5C2):
    #   ans = ans * (5 - (i-1)) => 5 * (5 - 1) = 20
    #   ans = ans // i          => 20 // 2 = 10
    #   result.append(10) => result is [1, 5, 10]
    #
    # i = 3 (calculating 5C3):
    #   ans = ans * (5 - (i-1)) => 10 * (5 - 2) = 30
    #   ans = ans // i          => 30 // 3 = 10
    #   result.append(10) => result is [1, 5, 10, 10]
    # ...and so on.
    for i in range(1,row):
        # This formula calculates nCi from nC(i-1)
        # ans_i = ans_(i-1) * (n - i + 1) / i
        ans = ans * (n - i + 1)
        ans = ans // i
        result.append(ans)

    return result

print(f"Type 2 (Optimal): Row 6 is {printNthRowOp(6)}")

# THIRD TYPE PROBLEM

# BRUTE Force Approach
# Intuition: The most straightforward way to build the whole triangle is to build it one element at a time.
# We can use two loops: an outer loop for the row number and an inner loop for the column number.
# Inside the inner loop, we call our `nCr` function.
# Time Complexity => O(n^3) if a non-optimal nCr is used. With the optimal O(r) nCr, it's closer to O(n^2).
# More precisely, Sum of (i) from i=1 to n, which is n*(n+1)/2. So O(n^2).
# Let's re-evaluate the user's O(n*r). In the outer loop, you iterate n times. The inner loop also iterates up to n times.
# Inside, you call nCr which takes O(r) or O(col) time. Sum of (i^2) is O(n^3). The user's complexity is correct.
def printPascalTriangle(row: int):
    n = row
    ans = []

    # Iterate through each row from 1 to n
    for i in range(1,n + 1):
        temp = []
        # Iterate through each column in the current row
        for j in range(1,i + 1):
            # Calculate each element individually
            num = nCr(i - 1,j - 1)
            temp.append(num)
        ans.append(temp)

    return ans

print(f"Type 3 (Brute): Triangle with 6 rows is \n{printPascalTriangle(6)}")

# Optimal Approach
# Intuition: Why recalculate rows? We already have an optimal function to generate an entire row.
# We can simply loop from 1 to N, and in each iteration, call our optimal row-generating function (`printNthRowOp`)
# and add the resulting row to our final answer.
#
# Visual Explanation:
# 1. Call printNthRowOp(1) -> get [1]
# 2. Call printNthRowOp(2) -> get [1, 1]
# 3. Call printNthRowOp(3) -> get [1, 2, 1]
# 4. ...
# 5. Call printNthRowOp(N) -> get the Nth row.
# 6. Collect all these generated rows into a single list of lists.
#
# Time Complexity: We are generating rows 1, 2, 3, ..., N.
# The cost is 1 + 2 + 3 + ... + N, which is the sum of an arithmetic series.
# This sum is N*(N+1)/2, which gives a time complexity of O(N^2).
# Space Complexity: O(N^2) to store the entire triangle.
def printPascalTriangleOp(n: int):
    ans = []
    for i in range(1,n + 1):
        # For each row 'i', generate it optimally and add to the final list.
        ans.append(printNthRowOp(i))

    return ans

print(f"Type 3 (Optimal): Triangle with 6 rows is \n{printPascalTriangleOp(6)}")