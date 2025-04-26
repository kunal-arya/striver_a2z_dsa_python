# Check if a given string is a palindrome or not

def str_pal(n: str, i = 0):
    if(i >= len(n) // 2): 
        return True
    if n[i] != n[len(n) - i - 1]:
        return False
    
    return str_pal(n,i + 1)

print(str_pal("MADAM"))

# URL - https://leetcode.com/problems/valid-palindrome/

# Brute Force
def isPalindrome(s: str, i , j):
    if i >= j:
        return True

    if not s[i].isalnum():
        return isPalindrome(s,i + 1,j)
    
    if not s[j].isalnum():
        return isPalindrome(s,i,j - 1)
    
    if s[i].lower() != s[j].lower():
        return False
    
    return isPalindrome(s,i + 1, j - 1)

pal_str = "A man, a plan, a canal: Panama"
last_pal_str = len(pal_str) - 1
print(isPalindrome(pal_str, 0, last_pal_str))

# Optimised - without extra space (using two pointers)
# - Skip non-alphanumeric characters using while loops before recursion.
# - This reduces the number of recursive calls.
# - Make sure each recursion only happens for real character comparisons.

def isPalOp(s: str, i: int, j: int) -> bool:
    while i < j and not s[i].isalnum():
        i += 1
    while i < j and not s[j].isalnum():
        j -= 1

    if i >= j:
        return True
    
    if s[i].lower() != s[j].lower():
        return False
    
    return isPalOp(s,i + 1, j - 1)
   
print(isPalOp(pal_str, 0, last_pal_str))



# ------------------------------------------------------------
# 🧠 Python Recursion Limit - Notes
# ------------------------------------------------------------

# 1. Why recursion limit exists?
# - Python sets a recursion depth limit (~1000 by default) to prevent infinite recursion and stack overflow.
# - Too many recursive calls without a base case would crash the program.
# - You can check the current limit:
import sys
print(sys.getrecursionlimit())  # Usually outputs 1000

# 2. How to increase recursion limit?
# - Use sys.setrecursionlimit(new_limit) to manually increase it.
# - Example:
import sys
sys.setrecursionlimit(10000)

# - ⚠️ Warning: Setting it too high (e.g., 1 million) can crash Python with a stack overflow.
# - Safe practical limit: around 10,000 to 20,000 depending on your system.

# 3. Why iteration is better for very large inputs?
# - In recursion, every function call adds a new frame on the call stack.
# - In iteration (loops), memory is constant (heap-based, no deep call stack).
# - Hence, for very large inputs, iterative two-pointer method is more scalable.

# 5. Fun Fact - Tail Recursion Optimization (TCO) in Python:
# - Python does NOT perform tail call optimization by default.
# - Even if your recursion is 'tail-recursive', Python will still build call stacks.
# - There are hacky decorators to simulate TCO, but they are not recommended in real projects.

# ------------------------------------------------------------
# 🚀 Conclusion:
# - Recursion is elegant and good for clean code.
# - Iteration is better for performance and large inputs.
# - You can increase recursion limits safely within a range.
# - Always be careful about stack overflows if you use deep recursion.
# ------------------------------------------------------------

