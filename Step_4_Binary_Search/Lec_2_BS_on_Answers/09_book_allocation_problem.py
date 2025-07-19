"""
Problem: Allocate Minimum Pages
Platform: GeeksforGeeks
Difficulty: Medium
Topics: Array, Binary Search
LINK: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

Problem Statement:
You are given an array arr[] of integers, where each element arr[i] represents the number of pages in the ith book.
You also have an integer k representing the number of students.
The task is to allocate books to each student such that:
- Each student receives at least one book.
- Each student is assigned a contiguous sequence of books.
- No book is assigned to more than one student.

The objective is to minimize the maximum number of pages assigned to any student.
In other words, out of all possible allocations, find the arrangement where the student
who receives the most pages still has the smallest possible maximum.

Note: Return -1 if a valid assignment is not possible.

Examples:
Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation:
Possible allocations:
1. [12] and [34, 67, 90] -> Max pages = 191
2. [12, 34] and [67, 90] -> Max pages = 157
3. [12, 34, 67] and [90] -> Max pages = 113
The minimum of these maximums is 113.

Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Not enough books for 5 students.
"""

# =============================================================================
# PROBLEM ANALYSIS
# =============================================================================

"""
PROBLEM BREAKDOWN:
- Input: An array of integers `arr` representing pages in books, and an integer `k` for the number of students.
- Output: The minimum possible value for the maximum number of pages any single student is assigned.
- Constraints:
  - 1 <= arr.size() <= 10^6
  - 1 <= arr[i] <= 10^3
  - 1 <= k <= 10^3
- Edge Cases:
  - If the number of students `k` is greater than the number of books `n`, allocation is impossible. Return -1.
  - If there is only one student, they get all the books. The result is the sum of all pages.

APPROACH:
The problem asks to minimize a maximum value, which is a strong hint for using "Binary Search on Answer".

1.  **Define Search Space:** The answer (minimum of maximum pages) must lie in a specific range.
    -   The minimum possible value for the max pages is `max(arr)`. This happens when one student gets the thickest book, and we try to distribute the rest. No allocation can have a maximum smaller than the largest book.
    -   The maximum possible value is `sum(arr)`. This happens when `k=1`, and one student gets all the books.
    -   So, our search space for the answer is `[max(arr), sum(arr)]`.

2.  **Binary Search:** We can binary search on this range of possible answers.
    -   For each `mid` value (which represents a potential maximum number of pages a student can be assigned), we need to check if it's possible to allocate all books to `k` students.

3.  **Check Feasibility (`is_possible` function):**
    -   This function will take `mid` (max allowed pages) as input.
    -   It greedily allocates books to students. It counts how many students are needed to distribute all books without any student exceeding `mid` pages.
    -   Iterate through the books, summing up pages for the current student. If adding the next book exceeds `mid`, we assign that book to a new student and increment the student count.
    -   If the number of students required is less than or equal to `k`, then this `mid` is a possible solution.

4.  **Adjust Search Space:**
    -   If `is_possible(mid)` is true, it means we might be able to do even better with a smaller maximum. So, we try the left half of the search space: `high = mid - 1`.
    -   If `is_possible(mid)` is false, `mid` is too small. We need to allow more pages for each student. So, we try the right half: `low = mid + 1`.

5.  **Result:** The final answer will be `low` (or the variable storing the last valid `mid`), as we are trying to find the smallest possible maximum.

TIME COMPLEXITY: O(N * log(sum(arr) - max(arr))) where N is the number of books.
SPACE COMPLEXITY: O(1)
"""

# =============================================================================
# HELPER FUNCTION (for both approaches)
# =============================================================================

def count_students_for_allocation(arr, max_pages_allowed) -> int:
    """
    Calculates the number of students required to allocate all books
    such that no student is assigned more than `max_pages_allowed`.

    Args:
        arr: The array of pages in books.
        max_pages_allowed: The maximum number of pages any single student can have.

    Returns:
        The total number of students required for this allocation.
    """
    n = len(arr)
    pages_allocated_to_current_student = 0
    total_students_needed = 1

    for i in range(n):
        # This check is implicitly handled by the search space in the main functions
        # but is good for a standalone helper. A single book cannot be larger than max_pages_allowed.
        # if arr[i] > max_pages_allowed: return float('inf')

        if pages_allocated_to_current_student + arr[i] <= max_pages_allowed:
            # Allocate current book to the same student
            pages_allocated_to_current_student += arr[i]
        else:
            # Start with a new student
            total_students_needed += 1
            # Allocate the current book to the new student
            pages_allocated_to_current_student = arr[i]

    return total_students_needed

# =============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# =============================================================================

def book_allocation_brute(arr, k):
    """
    BRUTE FORCE APPROACH

    Intuition:
    The answer must be between the maximum element of the array and the sum of all elements.
    We can iterate through every possible value in this range and, for each value, check if it's
    a valid maximum page allocation for `k` students. The first value that works is our answer
    because we are iterating from the smallest possible answer upwards.

    Approach:
    1. Define the search range: `low = max(arr)`, `high = sum(arr)`.
    2. Iterate from `max_pages = low` to `high`.
    3. For each `max_pages`, use the helper function `count_students_for_allocation` to see
       how many students are needed.
    4. If `count_students_for_allocation(arr, max_pages)` is equal to `k`, we have found the
       lowest possible maximum, so we return `max_pages`.

    Time Complexity: O(N * (sum(arr) - max(arr))) - Very high, will time out.
    Space Complexity: O(1)
    """
    n = len(arr)
    if k > n:
        return -1

    low = max(arr)
    high = sum(arr)

    for max_pages in range(low, high + 1):
        students_needed = count_students_for_allocation(arr, max_pages)
        if students_needed <= k: # We check for <= k because we can always use fewer students
            return max_pages

    return -1

# =============================================================================
# SOLUTION 2: OPTIMAL APPROACH (BINARY SEARCH)
# =============================================================================

def book_allocation_optimal(arr, k):
    """
    OPTIMAL APPROACH - Binary Search on the Answer.

    Intuition:
    The range of possible answers `[max(arr), sum(arr)]` is monotonic.
    If we can allocate books with a maximum of `X` pages per student, we can definitely
    do it with `X+1` pages. This monotonicity allows us to use binary search to find
    the minimum possible value for this maximum allocation.

    Approach:
    1. Define the search space: `low = max(arr)`, `high = sum(arr)`.
    2. Use a while loop: `while low <= high`.
    3. Calculate `mid = low + (high - low) // 2`. This `mid` is our potential answer.
    4. Check if an allocation is possible with `mid` as the max pages using the helper function.
       - `students_needed = count_students_for_allocation(arr, mid)`
    5. If `students_needed <= k`:
       - This `mid` is a possible answer. We try for an even smaller max.
       - Store `mid` as a potential answer and search in the left half: `high = mid - 1`.
    6. If `students_needed > k`:
       - `mid` is too small. We need to allow more pages per student.
       - Search in the right half: `low = mid + 1`.
    7. The loop terminates when `low` crosses `high`, and `low` will hold the minimum possible value.

    Time Complexity: O(N * log(sum(arr) - max(arr)))
    Space Complexity: O(1)
    """
    n = len(arr)
    if k > n:
        return -1

    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = low + (high - low) // 2
        students_needed = count_students_for_allocation(arr, mid)

        if students_needed <= k:
            # This is a potential answer, try for a smaller one
            high = mid - 1
        else:
            # Need to allow more pages, so increase the lower bound
            low = mid + 1

    return low

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    arr = [12, 34, 67, 90]
    k = 2
    print(f"Array: {arr}, Students: {k}")
    
    # Brute force solution
    brute_result = book_allocation_brute(arr, k)
    print(f"Brute Force Result: {brute_result}")

    # Optimal solution
    optimal_result = book_allocation_optimal(arr, k)
    print(f"Optimal Result: {optimal_result}")

    print("-" * 20)

    arr2 = [25, 46, 28, 49, 24]
    k2 = 4
    print(f"Array: {arr2}, Students: {k2}")
    optimal_result2 = book_allocation_optimal(arr2, k2)
    print(f"Optimal Result: {optimal_result2}") # Expected: 71
