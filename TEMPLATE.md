"""
Problem: [Write the problem statement here]
Platform: [LeetCode/HackerRank/GeeksforGeeks/etc.]
Difficulty: [Easy/Medium/Hard]
Topics: [Array, String, Dynamic Programming, etc.]
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: [Describe input format and constraints]
- Output: [Describe expected output]
- Constraints: [List any constraints like array size, value ranges]
- Edge Cases: [List potential edge cases to handle]

APPROACH:
1. [Step 1 of your approach]
2. [Step 2 of your approach]
3. [Step 3 of your approach]

TIME COMPLEXITY: O(?)
SPACE COMPLEXITY: O(?)
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================

def brute_force_solution(input_params):
    """
    BRUTE FORCE APPROACH - Most straightforward solution.
    
    Intuition:
    - [Explain the basic idea behind brute force]
    - [Why this approach works but is inefficient]
    
    Approach:
    1. [Step 1 of brute force approach]
    2. [Step 2 of brute force approach]
    3. [Step 3 of brute force approach]
    
    Args:
        input_params: [Describe the input parameters]
    
    Returns:
        [Describe what the function returns]
    
    Time Complexity: O(n²) or O(n³) - [Explain why]
    Space Complexity: O(1) or O(n) - [Explain space usage]
    """
    
    # STEP 1: Input validation and edge case handling
    if not input_params:
        return []  # or appropriate default value
    
    # STEP 2: Initialize result
    result = []
    
    # STEP 3: Brute force logic - usually nested loops
    # OUTER LOOP: [Explain what outer loop does]
    for i in range(len(input_params)):
        # INNER LOOP: [Explain what inner loop does]
        for j in range(i + 1, len(input_params)):
            # PROCESS: [Explain the operation being performed]
            # Check condition and add to result
            if some_condition(input_params[i], input_params[j]):
                result.append((input_params[i], input_params[j]))
    
    return result

# ==============================================================================
# SOLUTION 2: BETTER APPROACH
# ==============================================================================

def better_solution(input_params):
    """
    BETTER APPROACH - Improved efficiency with some optimization.
    
    Intuition:
    - [Explain how this improves upon brute force]
    - [What technique/data structure makes this better]
    
    Approach:
    1. [Step 1 of better approach]
    2. [Step 2 of better approach]
    3. [Step 3 of better approach]
    
    Args:
        input_params: [Describe the input parameters]
    
    Returns:
        [Describe what the function returns]
    
    Time Complexity: O(n log n) or O(n) - [Explain the improvement]
    Space Complexity: O(n) - [Explain space usage]
    """
    
    # STEP 1: Input validation
    if not input_params:
        return []
    
    # STEP 2: Use auxiliary data structure for optimization
    # OPTIMIZATION: Using hashmap/set/sorted array to reduce time complexity
    auxiliary_ds = {}  # or set() or sorted list
    result = []
    
    # STEP 3: Single pass or reduced complexity algorithm
    for i, element in enumerate(input_params):
        # CHECK: Look for complement/target in auxiliary data structure
        if target - element in auxiliary_ds:
            result.append((element, target - element))
        
        # UPDATE: Add current element to auxiliary data structure
        auxiliary_ds[element] = i
    
    return result

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH
# ==============================================================================

def optimal_solution(input_params):
    """
    OPTIMAL APPROACH - Most efficient solution possible.
    
    Intuition:
    - [Explain the key insight that makes this optimal]
    - [Why this is the best possible time/space complexity]
    
    Approach:
    1. [Step 1 of optimal approach]
    2. [Step 2 of optimal approach]
    3. [Step 3 of optimal approach]
    
    Args:
        input_params: [Describe the input parameters]
    
    Returns:
        [Describe what the function returns]
    
    Time Complexity: O(n) - [Explain why this is optimal]
    Space Complexity: O(1) - [Explain space efficiency]
    """
    
    # STEP 1: Input validation
    if not input_params:
        return []
    
    # STEP 2: Initialize pointers/variables for optimal algorithm
    # TECHNIQUE: Two pointers/Sliding window/Mathematical formula
    left, right = 0, len(input_params) - 1
    result = []
    
    # STEP 3: Optimal algorithm - single pass with smart pointer movement
    while left < right:
        # CALCULATE: Current sum/product/difference
        current_sum = input_params[left] + input_params[right]
        
        # DECISION: Move pointers based on condition
        if current_sum == target:
            result.append((input_params[left], input_params[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return result

# ==============================================================================
# MAIN SOLUTION FUNCTION
# ==============================================================================

def solve_problem(input_params, approach="optimal"):
    """
    Main solution function that calls the appropriate approach.
    
    Args:
        input_params: [Describe the input parameters]
        approach: "brute", "better", or "optimal" (default)
    
    Returns:
        [Describe what the function returns]
    """
    
    if approach == "brute":
        return brute_force_solution(input_params)
    elif approach == "better":
        return better_solution(input_params)
    elif approach == "optimal":
        return optimal_solution(input_params)
    else:
        raise ValueError("Approach must be 'brute', 'better', or 'optimal'")

# ==============================================================================
# APPROACH COMPARISON
# ==============================================================================

def compare_approaches():
    """
    Compare all three approaches with sample input.
    Useful for understanding trade-offs and verifying correctness.
    """
    
    # Sample input for comparison
    sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("APPROACH COMPARISON:")
    print("=" * 50)
    
    # Test each approach
    approaches = ["brute", "better", "optimal"]
    
    for approach in approaches:
        print(f"\n{approach.upper()} APPROACH:")
        
        # Measure time
        import time
        start_time = time.time()
        result = solve_problem(sample_input, approach)
        end_time = time.time()
        
        print(f"Result: {result}")
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        print(f"Result length: {len(result)}")

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def helper_function(param):
    """
    Helper function to [describe purpose].
    
    Args:
        param: [Description]
    
    Returns:
        [Description]
    """
    # Implementation
    pass

# ==============================================================================
# TEST CASES
# ==============================================================================

def test_solution():
    """
    Test cases to verify all three approaches work correctly.
    """
    
    print("TESTING ALL APPROACHES:")
    print("=" * 40)
    
    # TEST CASE 1: Basic example
    input1 = [1, 2, 3, 4, 5]
    expected1 = [1, 2, 3]  # Replace with expected output
    
    print("\nTest 1 - Basic example:")
    for approach in ["brute", "better", "optimal"]:
        result1 = solve_problem(input1, approach)
        assert result1 == expected1, f"Test 1 {approach} failed: expected {expected1}, got {result1}"
        print(f"✓ {approach.capitalize()} approach passed")
    
    # TEST CASE 2: Edge case - empty input
    input2 = []
    expected2 = []
    
    print("\nTest 2 - Empty input:")
    for approach in ["brute", "better", "optimal"]:
        result2 = solve_problem(input2, approach)
        assert result2 == expected2, f"Test 2 {approach} failed: expected {expected2}, got {result2}"
        print(f"✓ {approach.capitalize()} approach passed")
    
    # TEST CASE 3: Edge case - single element
    input3 = [42]
    expected3 = [42]
    
    print("\nTest 3 - Single element:")
    for approach in ["brute", "better", "optimal"]:
        result3 = solve_problem(input3, approach)
        assert result3 == expected3, f"Test 3 {approach} failed: expected {expected3}, got {result3}"
        print(f"✓ {approach.capitalize()} approach passed")
    
    # TEST CASE 4: Large input performance test
    print("\nTest 4 - Performance comparison:")
    large_input = list(range(1000))  # Adjust size based on problem
    
    import time
    for approach in ["brute", "better", "optimal"]:
        start_time = time.time()
        result = solve_problem(large_input, approach)
        end_time = time.time()
        print(f"{approach.capitalize()} approach: {end_time - start_time:.4f} seconds")
    
    print("\n🎉 All tests passed!")

def test_correctness():
    """
    Verify that all three approaches produce the same results.
    """
    test_cases = [
        [1, 2, 3, 4, 5],
        [10, 20, 30],
        [1],
        [],
        [5, 5, 5, 5]
    ]
    
    print("CORRECTNESS VERIFICATION:")
    print("=" * 30)
    
    for i, test_input in enumerate(test_cases):
        print(f"\nTest case {i+1}: {test_input}")
        
        # Get results from all approaches
        brute_result = solve_problem(test_input, "brute")
        better_result = solve_problem(test_input, "better")
        optimal_result = solve_problem(test_input, "optimal")
        
        # Verify all approaches give same result
        assert brute_result == better_result == optimal_result, \
            f"Results don't match! Brute: {brute_result}, Better: {better_result}, Optimal: {optimal_result}"
        
        print(f"✓ All approaches agree: {brute_result}")
    
    print("\n✅ All approaches produce identical results!")

# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

"""
DETAILED COMPLEXITY ANALYSIS:

TIME COMPLEXITY:
- Best Case: O(?)
- Average Case: O(?)
- Worst Case: O(?)
- Explanation: [Explain why this complexity]

SPACE COMPLEXITY:
- O(?) 
- Explanation: [Explain space usage]

TRADE-OFFS:
- [Discuss any trade-offs between time and space]
- [When to use this approach vs alternatives]
"""

# ==============================================================================
# COMMON PATTERNS FOR DSA
# ==============================================================================

# PATTERN 1: Two Pointers
"""
left, right = 0, len(arr) - 1
while left < right:
    # Process elements at left and right
    if condition:
        left += 1
    else:
        right -= 1
"""

# PATTERN 2: Sliding Window
"""
left = 0
for right in range(len(arr)):
    # Expand window by including arr[right]
    while window_condition_violated:
        # Shrink window from left
        left += 1
    # Process current window [left, right]
"""

# PATTERN 3: Dynamic Programming
"""
dp = [0] * (n + 1)  # Initialize DP array
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = dp[i-1] + something  # Recurrence relation
"""

# ==============================================================================
# DEBUGGING HELPERS
# ==============================================================================

def debug_print(variable, description=""):
    """
    Helper function for debugging during development.
    Remove or comment out before final submission.
    """
    print(f"DEBUG - {description}: {variable}")

def visualize_array(arr, highlight_indices=None):
    """
    Visualize array state during algorithm execution.
    Useful for understanding two-pointer or sliding window problems.
    """
    visual = []
    for i, val in enumerate(arr):
        if highlight_indices and i in highlight_indices:
            visual.append(f"[{val}]")
        else:
            visual.append(str(val))
    print(" ".join(visual))

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    # Run correctness tests
    test_correctness()
    
    # Run detailed tests
    test_solution()
    
    # Compare approaches
    compare_approaches()
    
    # Example usage with default optimal approach
    sample_input = [1, 2, 3, 4, 5]
    result = solve_problem(sample_input)  # Uses optimal by default
    print(f"\nFinal Result (Optimal): {result}")
    
    # Example: Test specific approach
    brute_result = solve_problem(sample_input, "brute")
    print(f"Brute Force Result: {brute_result}")
    
    # PERFORMANCE TESTING: Uncomment to test with very large inputs
    """
    print("\nPERFORMANCE TEST WITH LARGE INPUT:")
    large_input = list(range(10000))
    
    import time
    for approach in ["brute", "better", "optimal"]:
        start_time = time.time()
        result = solve_problem(large_input, approach)
        end_time = time.time()
        print(f"{approach.capitalize()}: {end_time - start_time:.4f} seconds")
    """