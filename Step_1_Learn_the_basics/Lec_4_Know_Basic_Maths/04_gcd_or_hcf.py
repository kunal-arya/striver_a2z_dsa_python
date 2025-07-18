# You are given two integers n1 and n2. 
# You need find the Greatest Common Divisor (GCD) of the two given numbers.
# Return the GCD of the two numbers.

## Input: n1 = 4, n2 = 6
## Output: 2

def gcd(n1: int, n2: int) -> int:
    """
    Calculate the greatest common divisor of two integers.
    
    Args:
        n1: First integer
        n2: Second integer
        
    Returns:
        The greatest common divisor of n1 and n2
    """
    # Handle edge cases
    # If either number is 0, return the absolute value of the other number
    # abs() converts negative numbers to positive (e.g., abs(-9) becomes 9)
    if n1 == 0:
        return abs(n2)  # If first number is 0, GCD is the second number
    if n2 == 0:
        return abs(n1)  # If second number is 0, GCD is the first number
    
    # Take absolute values of inputs to handle negative numbers
    # GCD of -12 and 18 is the same as GCD of 12 and 18
    n1, n2 = abs(n1), abs(n2)
    
    # Use Euclidean algorithm for efficient GCD calculation
    # This algorithm works by repeatedly dividing the larger number by the smaller
    # and taking the remainder until the remainder is 0
    while n2:  # Continue until n2 becomes 0
        temp = n2
        n2 = n1 % n2  # Simultaneously update both values (swap and modulo)
        n1 = temp
    
    return n1  # When n2 becomes 0, n1 contains the GCD

# Time Complexity: O(log min(a, b))
# Auxiliary Space: O(log (min(a,b)))

# Dry Run Example: gcd(48, 18)
# Initial values: n1 = 48, n2 = 18
# 
# First iteration:
#   n1, n2 = n2, n1 % n2
#   n1, n2 = 18, 48 % 18 = 12
#   Values after first iteration: n1 = 18, n2 = 12
#
# Second iteration:
#   n1, n2 = n2, n1 % n2
#   n1, n2 = 12, 18 % 12 = 6
#   Values after second iteration: n1 = 12, n2 = 6
#
# Third iteration:
#   n1, n2 = n2, n1 % n2
#   n1, n2 = 6, 12 % 6 = 0
#   Values after third iteration: n1 = 6, n2 = 0
#
# Since n2 is now 0, the loop ends and we return n1 = 6
# So, gcd(48, 18) = 6
#
# Another example with negative numbers: gcd(-24, 36)
# First we take abs(): n1 = 24, n2 = 36
# 
# First iteration:
#   n1, n2 = n2, n1 % n2
#   n1, n2 = 36, 24 % 36 = 24
#   Values after first iteration: n1 = 36, n2 = 24
#
# Second iteration:
#   n1, n2 = n2, n1 % n2
#   n1, n2 = 24, 36 % 24 = 12
#   Values after second iteration: n1 = 24, n2 = 12
#
# Third iteration:
#   n1, n2 = n2, n1 % n2
#   n1, n2 = 12, 24 % 12 = 0
#   Values after third iteration: n1 = 12, n2 = 0
#
# Since n2 is now 0, the loop ends and we return n1 = 12
# So, gcd(-24, 36) = 12

########################################################################

# Finding the Greatest Common Divisor (GCD) - Simple Explanation

# ## What is GCD?
# The Greatest Common Divisor (GCD) is the biggest 
# number that can divide two numbers without leaving any leftovers.

# For example, the GCD of 12 and 18 is 6 because:
# - 6 divides 12 (12 ÷ 6 = 2)
# - 6 divides 18 (18 ÷ 6 = 3)
# - No number bigger than 6 can divide both 12 and 18 evenly

# ## The Euclidean Algorithm (Simple Version)

# Imagine you have two jars of different colored blocks:
# - One jar has 18 red blocks
# - Another jar has 12 blue blocks

# We want to make equal piles using ALL blocks, with each pile having the SAME number of blocks.

# ### Step 1: Try to make as many equal groups as possible
# - Take the smaller number (12 blue blocks)
# - See how many complete groups of 12 you can make from 18 red blocks
#   - You can make 1 complete group of 12, with 6 red blocks left over

# ### Step 2: Look at what's left over
# - We have 12 blue blocks and 6 leftover red blocks
# - Now repeat with these numbers:
#   - Take the smaller number (6 red blocks)
#   - See how many complete groups of 6 you can make from 12 blue blocks
#   - You can make 2 complete groups, with 0 blue blocks left over

# ### Step 3: Since nothing is left over, we found our answer!
# - The last non-zero number (6) is our GCD
# - This means we can make 6 piles with:
#   - Each pile having 3 red blocks and 2 blue blocks
#   - All blocks are used
#   - All piles are equal

# ## Why This Works

# When we're looking for how to divide numbers evenly, we can keep simplifying the problem:
# - If we can divide 18 and 12 evenly by some number
# - Then we can also divide 12 and 6 (the remainder) evenly by that same number
# - And if we can divide 12 and 6 evenly by some number
# - Then we can divide 6 and 0 evenly by that number

# When one number becomes 0, the other number is our answer!

# ## The Code in Simple Terms

# Our code is like a recipe:
# 1. If either number is 0, the answer is the other number
# 2. Make sure all numbers are positive (change negative numbers to positive)
# 3. Keep swapping and finding remainders until one number becomes 0
# 4. When one number becomes 0, the other number is our answer!

# Just like cleaning up blocks after playtime - keep organizing 
# them into smaller and smaller groups until everything fits perfectly!