# Algorithmic Patterns in Array Problems (Striver A2Z DSA Python)

This document categorizes the array problems by common algorithmic patterns, providing explanations for each pattern and mapping specific problem solutions to them. For each solution, its time and space complexity are noted.

---

## 1. Basic Array Traversal / Linear Scan

**Explanation:** This pattern involves iterating through an array, usually once, to perform a simple operation like finding a maximum/minimum element, counting occurrences, or checking a condition. It's the most fundamental approach and often serves as the brute-force or a simple optimal solution for problems that don't require complex data structures or algorithms.

**Problems & Solutions:**

*   **01_largest_elm.py (Largest Element in the array)**
    *   **Solution:** `largest` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Linear Scan
*   **02_second_largest_element.py (Find Second Largest Element in an Array)**
    *   **Solution:** `secLargest` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Linear Scan
*   **03_check_arr_sorted.py (Maximum Ascending Subarray Sum)**
    *   **Solution:** `max_sub` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Linear Scan, Greedy (Kadane's variant)
*   **03_check_arr_sorted.py (Check if Array is Sorted and Rotated)**
    *   **Solution:** `arr_sorted_op` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Linear Scan (with modulo for circular check)
*   **08_linear_search.py (Linear Search)**
    *   **Solution:** `linearSearch` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Linear Scan
*   **11_max_consecutive_ones.py (Maximum Consecutive Ones)**
    *   **Solution:** `max_consecutive_ones` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Linear Scan, Counter

---

## 2. Two Pointers

**Explanation:** This pattern involves using two pointers (indices) to traverse an array or data structure. The pointers can move in the same direction (e.g., for sliding window, or in-place modification) or in opposite directions (e.g., for searching pairs, merging sorted arrays, or partitioning). It's highly effective for problems requiring linear time complexity and often constant space.

**Problems & Solutions:**

*   **04_remove_duplicates.py (Remove Duplicates from Sorted Array)**
    *   **Solution:** `remove_dup` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Two Pointers (In-place modification)
*   **07_move_zeroes_to_end.py (Move Zeroes to End)**
    *   **Solution:** `moveZeroesOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Two Pointers (In-place swap)
*   **09_find_the_union.py (Union of Two Sorted Arrays)**
    *   **Solution:** `findUnionOp` (Optimal)
    *   **Time Complexity:** O(N+M)
    *   **Space Complexity:** O(N+M) (for result array)
    *   **Pattern:** Two Pointers (Merge-like)
*   **09_find_the_union.py (Intersection of Two Sorted Arrays)**
    *   **Solution:** `findIntersectionOp` (Optimal)
    *   **Time Complexity:** O(N+M)
    *   **Space Complexity:** O(N+M) (for result array)
    *   **Pattern:** Two Pointers (Merge-like)
*   **01_two_sum_problem.py (Two Sum)**
    *   **Solution:** `TwoSumProblemOp` (Optimal, requires sorting)
    *   **Time Complexity:** O(N log N) (due to sort)
    *   **Space Complexity:** O(N) (for storing pairs with indices)
    *   **Pattern:** Two Pointers (on sorted array)
*   **02_sort_color.py (Sort Colors)**
    *   **Solution:** `sortColorOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Three Pointers (Dutch National Flag Algorithm)
*   **07_rearrange_array_elements_by_signs.py (Rearrange Array Elements by Sign)**
    *   **Solution:** `rearrangeArrayElOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N) (for new result array)
    *   **Pattern:** Two Pointers (Direct placement into new array)
*   **07_rearrange_array_elements_by_signs.py (Rearrange Array Elements by Sign - Unequal Counts)**
    *   **Solution:** `rearrangeArrayElOp2` (Optimal Variant)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N) (for separate positive/negative lists)
    *   **Pattern:** Two Pointers (Separate and Merge)
*   **03_3sum.py (3Sum)**
    *   **Solution:** `threeSumOp` (Optimal)
    *   **Time Complexity:** O(N^2) (after sorting)
    *   **Space Complexity:** O(N) (for result, or O(1) if not counting result)
    *   **Pattern:** Two Pointers (nested with fixed element on sorted array)
*   **04_4sum.py (4Sum)**
    *   **Solution:** `fourSumOp` (Optimal)
    *   **Time Complexity:** O(N^3) (after sorting)
    *   **Space Complexity:** O(N) (for result, or O(1) if not counting result)
    *   **Pattern:** Two Pointers (nested with two fixed elements on sorted array)
*   **08_merge_two_sorted_array.py (Merge Two Sorted Arrays - In-place)**
    *   **Solution:** `mergeTwoSortedArrOp` (Optimal 1)
    *   **Time Complexity:** O(min(N,M) + N log N + M log M)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Two Pointers (Swap and Sort)
*   **08_merge_two_sorted_array.py (Merge Two Sorted Arrays - Gap Method)**
    *   **Solution:** `mergeTwoSortedArrOp2` (Optimal 2)
    *   **Time Complexity:** O((N+M) log (N+M))
    *   **Space Complexity:** O(1)
    *   **Pattern:** Two Pointers (Gap Method, Shell Sort variant)

---

## 3. Sliding Window

**Explanation:** This pattern is used for problems that involve finding a subarray or substring that satisfies a certain condition. It works by maintaining a "window" (a range defined by two pointers, `start` and `end`) that slides over the array. The window expands by moving the `end` pointer and shrinks by moving the `start` pointer, typically to maintain the condition or optimize the search.

**Problems & Solutions:**

*   **13_14_longest_subarray_with_sum_k.py (Longest Subarray with Sum K)**
    *   **Solution:** `longestSubArraySumKOp` (Optimal, for non-negative numbers)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Sliding Window (Two Pointers)

---

## 4. Hashing (Hash Maps / Sets)

**Explanation:** This pattern leverages hash-based data structures (dictionaries/hash maps or sets) for efficient lookups, insertions, and deletions (average O(1) time complexity). It's particularly useful for problems involving frequency counting, checking for existence, or storing relationships between elements. It often trades space complexity for improved time complexity.

**Problems & Solutions:**

*   **09_find_the_union.py (Union of Two Sorted Arrays)**
    *   **Solution:** `findUnion` (Brute Force / Better)
    *   **Time Complexity:** O(N+M)
    *   **Space Complexity:** O(N+M)
    *   **Pattern:** Hashing (Set for uniqueness)
*   **09_find_the_union.py (Intersection of Two Sorted Arrays)**
    *   **Solution:** `findIntersection` (Brute Force / Better)
    *   **Time Complexity:** O(N+M)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Set for lookup)
*   **10_missing_number.py (Find the Missing Number from Array)**
    *   **Solution:** `missingNumHashing` (Better)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Set for presence check)
*   **12_single_num.py (Find the Single Number)**
    *   **Solution:** `singleNumBetter` (Better)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Frequency Map)
*   **13_14_longest_subarray_with_sum_k.py (Longest Subarray with Sum K)**
    *   **Solution:** `longestSubArraySumKBetter` (Better)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Prefix Sum Map)
*   **01_two_sum_problem.py (Two Sum)**
    *   **Solution:** `TwoSumProblemBetter` (Optimal for index-based return)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Map for complement lookup)
*   **03_majority_element_n2.py (Find the Majority Element (> n/2 times))**
    *   **Solution:** `majorityElN2Better` (Better)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Frequency Map)
*   **10_longest_consecutive_subsequence.py (Longest Consecutive Sequence)**
    *   **Solution:** `longestSubsequenceOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Set + Smart Start)
*   **14_count_subarray_with_given_sum.py (Count Subarray with Given Sum K)**
    *   **Solution:** `countSubArraySumKOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Prefix Sum Map)
*   **02_majority_element_2.py (Find Majority Elements (> n/3 times))**
    *   **Solution:** `majorityElBetter` (Better)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Frequency Map)
*   **03_3sum.py (3Sum)**
    *   **Solution:** `threeSumBetter` (Better)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Two Loops + Hash Set)
*   **04_4sum.py (4Sum)**
    *   **Solution:** `fourSumBetter` (Better)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Three Loops + Hash Set)
*   **05_largest_subarray_with_sum0.py (Largest Subarray with Sum 0)**
    *   **Solution:** `largestSubOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Prefix Sum Map)
*   **06_count_subarray_with_given_xor_k.py (Count Subarray with Given XOR K)**
    *   **Solution:** `countSubArrayxorKOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Prefix XOR Map)
*   **09_find_missing_repeating.py (Find Missing and Repeating Numbers)**
    *   **Solution:** `findMissingRepeatingBetter` (Better)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Hashing (Frequency Array)

---

## 5. Kadane's Algorithm / Dynamic Programming (Greedy)

**Explanation:** Kadane's algorithm is a dynamic programming approach used to find the maximum sum of a contiguous subarray within a one-dimensional array of numbers. It's a greedy algorithm that maintains a `current_sum` and a `max_sum`, resetting `current_sum` to 0 if it becomes negative. This pattern is highly efficient (linear time, constant space).

**Problems & Solutions:**

*   **04_maximum_subarray_sum.py (Maximum Subarray Sum)**
    *   **Solution:** `maxSubArraySumOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Kadane's Algorithm
*   **05_print_subarray_sum.py (Print Subarray with Maximum Sum)**
    *   **Solution:** `printMaxSubArraySumOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Kadane's Algorithm (with index tracking)
*   **12_max_product_subarray.py (Maximum Product Subarray)**
    *   **Solution:** `maxProductSubArrayOptimal` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Dynamic Programming / Greedy (Prefix/Suffix Product variant of Kadane's idea)

---

## 6. Matrix Manipulation / Traversal

**Explanation:** This pattern involves algorithms specifically designed for 2D arrays (matrices). This can include operations like rotation, setting elements to zero based on conditions, or traversing the matrix in specific patterns (e.g., spiral).

**Problems & Solutions:**

*   **11_set_matrix_zeroes.py (Set Matrix Zeroes)**
    *   **Solution:** `setMatrixZeroesOp` (Optimal)
    *   **Time Complexity:** O(M*N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** In-place Matrix Manipulation (using first row/col as markers)
*   **12_rotate_90_deg.py (Rotate Image by 90 Degrees)**
    *   **Solution:** `rotateOptimal` (Optimal)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Matrix Manipulation (Transpose + Reverse Rows)
*   **13_print_matrix_spiral.py (Print Matrix in Spiral Order)**
    *   **Solution:** `spiralPrint` (Optimal)
    *   **Time Complexity:** O(M*N)
    *   **Space Complexity:** O(M*N) (for result list)
    *   **Pattern:** Matrix Traversal (Boundary Shrinking)

---

## 7. Sorting / Divide and Conquer

**Explanation:** This pattern involves using sorting as a preprocessing step to simplify a problem, or using a divide-and-conquer strategy (like Merge Sort) where the problem is broken down into smaller subproblems, solved recursively, and then combined.

**Problems & Solutions:**

*   **10_missing_number.py (Find the Missing Number from Array)**
    *   **Solution:** `missingNumBetter` (Better)
    *   **Time Complexity:** O(N log N) (due to sort)
    *   **Space Complexity:** O(1) (depends on sort implementation)
    *   **Pattern:** Sorting
*   **02_sort_color.py (Sort Colors)**
    *   **Solution:** `sortColorBrute` (Brute Force)
    *   **Time Complexity:** O(N log N) (Merge Sort)
    *   **Space Complexity:** O(N) (Merge Sort)
    *   **Pattern:** Sorting (General Purpose)
*   **10_longest_consecutive_subsequence.py (Longest Consecutive Sequence)**
    *   **Solution:** `longestSubsequenceBetter` (Better)
    *   **Time Complexity:** O(N log N) (due to sort)
    *   **Space Complexity:** O(1) (depends on sort implementation)
    *   **Pattern:** Sorting
*   **07_merge_overlapping_subintervals.py (Merge Overlapping Intervals)**
    *   **Solution:** `mergeIntervalsBrute` (Brute Force)
    *   **Time Complexity:** O(N^2) (due to nested loop after sort)
    *   **Space Complexity:** O(N) (for result)
    *   **Pattern:** Sorting + Iteration
    *   **Solution:** `mergeIntervalsOp` (Optimal)
    *   **Time Complexity:** O(N log N) (due to sort)
    *   **Space Complexity:** O(N) (for result)
    *   **Pattern:** Sorting + Single Pass
*   **10_count_inversion.py (Count Inversions in Array)**
    *   **Solution:** `inversionCount` (Optimal)
    *   **Time Complexity:** O(N log N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Divide and Conquer (Merge Sort with Counting)
*   **11_reverse_pair.py (Reverse Pairs)**
    *   **Solution:** `reversePairOp` (Optimal)
    *   **Time Complexity:** O(N log N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Divide and Conquer (Merge Sort with Counting)

---

## 8. Bit Manipulation

**Explanation:** This pattern involves using bitwise operators (AND, OR, XOR, NOT, left shift, right shift) to solve problems efficiently. It's often used for problems related to numbers, sets, or flags, providing constant time operations and minimal space usage.

**Problems & Solutions:**

*   **12_single_num.py (Find the Single Number)**
    *   **Solution:** `singleNumOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Bit Manipulation (XOR)
*   **09_find_missing_repeating.py (Find Missing and Repeating Numbers)**
    *   **Solution:** `findMissingRepeatingOp3` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Bit Manipulation (XOR)

---

## 9. Mathematical / Formula-Based

**Explanation:** This pattern applies mathematical properties or formulas to derive a solution, often leading to highly efficient algorithms with constant space complexity.

**Problems & Solutions:**

*   **10_missing_number.py (Find the Missing Number from Array)**
    *   **Solution:** `missingNumberOpS` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Mathematical (Summation)
*   **01_pascal_triangle.py (Pascal's Triangle - Type 1: Element at (row, col))**
    *   **Solution:** `pascalTriangleBrute` (Brute Force)
    *   **Time Complexity:** O(N) (due to factorial recursion)
    *   **Space Complexity:** O(N) (for recursion stack)
    *   **Pattern:** Mathematical (Combinatorics - nCr Factorial)
    *   **Solution:** `pascalTriangleBetter` (Optimal)
    *   **Time Complexity:** O(R) (where R is column index)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Mathematical (Optimized Combinatorics - nCr Iterative)
*   **01_pascal_triangle.py (Pascal's Triangle - Type 2: Print Nth Row)**
    *   **Solution:** `printNthRow` (Brute Force)
    *   **Time Complexity:** O(N*R) (N calls to O(R) nCr)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Mathematical (Combinatorics - Iterative nCr calls)
    *   **Solution:** `printNthRowOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Mathematical (Optimized Row Generation)
*   **01_pascal_triangle.py (Pascal's Triangle - Type 3: Print Entire Triangle)**
    *   **Solution:** `printPascalTriangle` (Brute Force)
    *   **Time Complexity:** O(N^3) (N^2 calls to O(N) nCr)
    *   **Space Complexity:** O(N^2)
    *   **Pattern:** Mathematical (Combinatorics - Nested nCr calls)
    *   **Solution:** `printPascalTriangleOp` (Optimal)
    *   **Time Complexity:** O(N^2) (N calls to O(N) row generation)
    *   **Space Complexity:** O(N^2)
    *   **Pattern:** Mathematical (Iterative Row Generation)
*   **09_find_missing_repeating.py (Find Missing and Repeating Numbers)**
    *   **Solution:** `findMissingRepeatingOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Mathematical (Summation and Sum of Squares)

---

## 10. Cyclic Sort

**Explanation:** This pattern is useful for problems involving arrays that contain numbers in a specific range (e.g., 1 to N). The core idea is to place each element at its correct sorted position. If an element `x` should be at index `x-1`, you swap it there. This process continues until all elements are in their correct places. It's an in-place sorting algorithm that can achieve O(N) time complexity for specific problem types.

**Problems & Solutions:**

*   **10_missing_number.py (Find the Missing Number from Array)**
    *   **Solution:** `findMissingOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Cyclic Sort
*   **09_find_missing_repeating.py (Find Missing and Repeating Numbers)**
    *   **Solution:** `findMissingRepeatingOp2` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Cyclic Sort

---

## 11. Boyer-Moore Voting Algorithm

**Explanation:** This algorithm is specifically designed to find the majority element(s) in an array. It works on the principle of "vote cancellation," where elements that are not the majority cancel out occurrences of other elements. It's highly efficient, achieving linear time and constant space complexity.

**Problems & Solutions:**

*   **03_majority_element_n2.py (Find the Majority Element (> n/2 times))**
    *   **Solution:** `majorityElN2Op` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Boyer-Moore Voting Algorithm
*   **02_majority_element_2.py (Find Majority Elements (> n/3 times))**
    *   **Solution:** `majorityElOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Extended Boyer-Moore Voting Algorithm

---

## 12. Brute Force (General)

**Explanation:** This refers to the most straightforward, often least efficient, approach to a problem. It typically involves checking every possible combination or permutation, leading to high time complexities (e.g., O(N^2), O(N^3), O(N^4), or O(N!)). While inefficient, it serves as a baseline and helps in understanding the problem before optimizing.

**Problems & Solutions:**

*   **03_check_arr_sorted.py (Check if Array is Sorted and Rotated)**
    *   **Solution:** `arr_sorted_b` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Brute Force (Rotation and Check)
*   **06_left_rotate_an_array_by_d_places.py (Left Rotate an Array by D Places)**
    *   **Solution:** `leftRotateBrute` (Brute Force)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(D)
    *   **Pattern:** Brute Force (Using temporary array)
*   **07_move_zeroes_to_end.py (Move Zeroes to End)**
    *   **Solution:** `moveZeroesBrute` (Brute Force)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Brute Force (Using temporary array)
*   **10_missing_number.py (Find the Missing Number from Array)**
    *   **Solution:** `missingNum` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loop search)
*   **12_single_num.py (Find the Single Number)**
    *   **Solution:** `singleNumBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loop counting)
*   **13_14_longest_subarray_with_sum_k.py (Longest Subarray with Sum K)**
    *   **Solution:** `longestSubArraySumKBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loops for all subarrays)
*   **01_two_sum_problem.py (Two Sum)**
    *   **Solution:** `TwoSumProblem` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loops for all pairs)
*   **03_majority_element_n2.py (Find the Majority Element (> n/2 times))**
    *   **Solution:** `majorityElementN2Brute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loop counting)
*   **04_maximum_subarray_sum.py (Maximum Subarray Sum)**
    *   **Solution:** `maximumSubArraySumBrute` (Brute Force)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Triple nested loops for all subarrays)
    *   **Solution:** `maximumSubArraySumBetter` (Better Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Optimized sum calculation)
*   **05_print_subarray_sum.py (Print Subarray with Maximum Sum)**
    *   **Solution:** `printMaxSubArrarySumBrute` (Brute Force)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(1) (for indices)
    *   **Pattern:** Brute Force (Triple nested loops)
    *   **Solution:** `printMaxSubArraySumBetter` (Better Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1) (for indices)
    *   **Pattern:** Brute Force (Optimized sum calculation)
*   **06_stock_buy_sell.py (Best Time to Buy and Sell Stock)**
    *   **Solution:** `stockBuySellBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loops for all buy/sell pairs)
*   **08_next_permutation.py (Next Permutation)**
    *   **Solution:** `next_permutation_brute` (Brute Force)
    *   **Time Complexity:** O(N! * N)
    *   **Space Complexity:** O(N! * N)
    *   **Pattern:** Brute Force (Generate all permutations)
*   **09_leader_in_the_array.py (Leaders in an Array)**
    *   **Solution:** `leaderInArrBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Brute Force (Nested loop comparison)
*   **10_longest_consecutive_subsequence.py (Longest Consecutive Sequence)**
    *   **Solution:** `longestSubsequenceBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loop search)
*   **11_set_matrix_zeroes.py (Set Matrix Zeroes)**
    *   **Solution:** `setMatrixZeroesBrute` (Brute Force - Note: This specific implementation has a flaw if -1 is a valid number in the matrix, but represents the brute force idea of marking elements.)
    *   **Time Complexity:** O(M*N * (M+N))
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Direct marking)
*   **12_rotate_90_deg.py (Rotate Image by 90 Degrees)**
    *   **Solution:** `rotateBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(N^2)
    *   **Pattern:** Brute Force (Using extra matrix)
*   **14_count_subarray_with_given_sum.py (Count Subarray with Given Sum K)**
    *   **Solution:** `countSubArraySumKBrute` (Brute Force)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Triple nested loops)
    *   **Solution:** `countSubArraySumKBetter` (Better Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Optimized sum calculation)
*   **02_majority_element_2.py (Find Majority Elements (> n/3 times))**
    *   **Solution:** `majorityElBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loop counting)
*   **03_3sum.py (3Sum)**
    *   **Solution:** `threeSumBrute` (Brute Force)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Brute Force (Triple nested loops)
*   **04_4sum.py (4Sum)**
    *   **Solution:** `fourSumBrute` (Brute Force)
    *   **Time Complexity:** O(N^4)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Brute Force (Quadruple nested loops)
*   **05_largest_subarray_with_sum0.py (Largest Subarray with Sum 0)**
    *   **Solution:** `largestSubBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(N)
    *   **Pattern:** Brute Force (Nested loops for all subarrays)
*   **06_count_subarray_with_given_xor_k.py (Count Subarray with Given XOR K)**
    *   **Solution:** `countSubArrayxorK` (Brute Force)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Triple nested loops)
    *   **Solution:** `countSubArrayxorKBetter` (Better Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Optimized XOR sum calculation)
*   **08_merge_two_sorted_array.py (Merge Two Sorted Arrays)**
    *   **Solution:** `mergeTwoSortedArrayBrute` (Brute Force)
    *   **Time Complexity:** O(N+M)
    *   **Space Complexity:** O(N+M)
    *   **Pattern:** Brute Force (Using temporary array)
*   **09_find_missing_repeating.py (Find Missing and Repeating Numbers)**
    *   **Solution:** `findMissingRepeatingBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loop counting)
*   **10_count_inversion.py (Count Inversions in Array)**
    *   **Solution:** `countInversion` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loops for all pairs)
*   **11_reverse_pair.py (Reverse Pairs)**
    *   **Solution:** `reversePairBrute` (Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Nested loops for all pairs)
*   **12_max_product_subarray.py (Maximum Product Subarray)**
    *   **Solution:** `maxProductSubArrayBrute` (Brute Force)
    *   **Time Complexity:** O(N^3)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Triple nested loops)
    *   **Solution:** `maxProductSubArrayBetter` (Better Brute Force)
    *   **Time Complexity:** O(N^2)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Brute Force (Optimized product calculation)

---

## 13. Backtracking / Recursion (for Permutations)

**Explanation:** Backtracking is a general algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem, and then trying another piece. It's often used for combinatorial problems like generating permutations or combinations.

**Problems & Solutions:**

*   **08_next_permutation.py (Permutations - Generating All)**
    *   **Solution:** `printAllPermutations` (General Permutation Generation)
    *   **Time Complexity:** O(N! * N)
    *   **Space Complexity:** O(N) (for recursion depth and frequency array)
    *   **Pattern:** Backtracking (using frequency array)
    *   **Solution:** `printAllPermutations2` (General Permutation Generation)
    *   **Time Complexity:** O(N! * N)
    *   **Space Complexity:** O(N) (for recursion depth)
    *   **Pattern:** Backtracking (using in-place swapping)

---

## 14. Greedy Algorithms

**Explanation:** Greedy algorithms make locally optimal choices at each step with the hope of finding a global optimum. They are often simple and efficient, but don't always guarantee the best solution for all problems.

**Problems & Solutions:**

*   **06_stock_buy_sell.py (Best Time to Buy and Sell Stock)**
    *   **Solution:** `stockBuySellOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Greedy (Single Pass, tracking minimum)

---

## 15. Advanced Array Reversal

**Explanation:** This pattern involves using array reversal operations to achieve complex array manipulations efficiently, often in-place and with linear time complexity.

**Problems & Solutions:**

*   **06_left_rotate_an_array_by_d_places.py (Left Rotate an Array by D Places)**
    *   **Solution:** `leftRotateOp` (Optimal)
    *   **Time Complexity:** O(N)
    *   **Space Complexity:** O(1)
    *   **Pattern:** Array Reversal (Three Reversals)

---
