# =================================================================================================
# PROBLEM: Find the Majority Element
# =================================================================================================
#
# Given an array of 'n' integers, the task is to find the element that appears more than n/2 times.
# We can assume that the array is non-empty.
#
# For example:
# Input: arr = [2, 2, 1, 1, 1, 2, 2]
# n = 7,  n/2 = 3.5
# The element '2' appears 4 times, which is > 3.5. So, 2 is the majority element.
#
# The problem will be solved in three ways:
# 1. Brute Force: The most straightforward, but least efficient way.
# 2. Better (Hashing): A more efficient method using extra memory.
# 3. Optimal (Moore's Voting Algorithm): The most efficient method with no extra memory.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Brute Force (Pick one element and scan the entire array)
# =================================================================================================

# --- INTUITION ---
# The simplest idea is to check every single element in the array. For each element,
# we can count how many times it appears in the total array.
# If we find an element whose count is greater than n/2, we have found our answer.
# It's like asking every person in a room, "Who are you?", and then for each person,
# asking everyone else again, "Are you the same as this person?" to count their supporters.

def majorityElementN2Brute(arr):
    # Get the size of the array. We need this to check against the n/2 condition.
    n = len(arr)

    # Outer loop: Picks one element at a time to be our 'candidate' for the majority element.
    for candidate in arr:
        # Initialize a counter for the current candidate.
        count = 0
        # Inner loop: Iterate through the entire array AGAIN to count occurrences of the 'candidate'.
        for element in arr:
            # If we find an element that matches our candidate, we increment the count.
            if candidate == element:
                count += 1
        
        # After counting all occurrences of the 'candidate', check if it's a majority element.
        if count > (n / 2):
            # If the count is more than half the array's size, we've found our answer.
            # We can stop and return it immediately.
            return candidate
    
    # If the outer loop completes without finding any element that satisfies the condition,
    # it means there is no majority element in the array.
    return -1

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2)
# Why? We have a nested loop structure. The outer loop runs N times, and for each of those N iterations,
# the inner loop also runs N times. This results in N * N = N^2 operations.
#
# Space Complexity: O(1)
# Why? We are not using any extra data structures that grow with the size of the input array.
# We only use a few variables like 'n', 'candidate', 'count', and 'element', which is constant space.
#
# --- HOW TO REMEMBER ---
# Think "Brute Force = Nested Loops". It's the "try everything" approach. For each thing, check against every other thing.

# Example Usage:
arr = [2,2,1,3,1,1,3,1,1]
# n = 9, n/2 = 4.5. The majority element must appear at least 5 times.
# The element '1' appears 5 times.
print(f"Brute Force Result: {majorityElementN2Brute(arr)}") # Expected: 1


# =================================================================================================
# Approach 2: Better (Using a Hash Map / Dictionary)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach is slow because we recount the same numbers over and over.
# A much better way is to count the frequency of EACH unique element just ONCE.
# A hash map (dictionary in Python) is the perfect tool for this. We can use the array
# elements as keys and their frequencies (counts) as values.
#
# The process is two-step:
# 1. First Pass: Go through the array and store the frequency of each number in the hash map.
# 2. Second Pass: Go through the hash map and check if any number's frequency is > n/2.

def majorityElN2Better(arr):
    n = len(arr)

    # Step 1: Create a frequency map.
    # The key will be the number from the array, and the value will be its count.
    freq_map = {}

    # Iterate through the array once to populate the frequency map.
    for num in arr:
        # Check if the number is already a key in our map.
        if num in freq_map:
            # If yes, increment its count.
            freq_map[num] += 1
        else:
            # If no, add it to the map with an initial count of 1.
            freq_map[num] = 1
    
    # Step 2: Find the majority element from the frequency map.
    # Now that we have the counts of all unique elements, we can iterate through our map.
    # .items() gives us key-value pairs (number, count).
    for num, count in freq_map.items():
        # Check if the count of the current number is greater than n/2.
        if count > (n / 2):
            # If it is, this is our majority element.
            return num
    
    # If we finish the loop and haven't returned, no majority element exists.
    return -1

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? The first loop runs N times to build the map. The second loop runs 'k' times, where 'k' is the
# number of unique elements. In the worst case, k can be N. So, O(N) + O(k) is O(N).
# (Assuming hash map operations like insertion and lookup take O(1) on average).
#
# Space Complexity: O(N) or O(k)
# Why? We are using a hash map to store the frequencies. In the worst-case scenario where all elements
# in the array are unique, the map will have to store N key-value pairs. So, the space required
# grows with the input size. 'k' is the number of unique elements.
#
# --- HOW TO REMEMBER ---
# Think "Counting = Hash Map". When you need to count things efficiently, a hash map is often the answer.
# It trades extra space for a faster time complexity compared to brute force.

# Example Usage:
arr = [2,2,1,3,1,1,3,1,1]
print(f"Better (Hashing) Result: {majorityElN2Better(arr)}") # Expected: 1


# =================================================================================================
# Approach 3: Optimal (Moore's Voting Algorithm)
# =================================================================================================

# --- INTUITION ---
# This is a very clever algorithm. The core idea is based on cancellation.
# If an element truly is the majority (appears > n/2 times), it will "survive" a process
# where every occurrence of it is cancelled out by an occurrence of a different element.
#
# Think of it as an election or a battle:
# - We have one candidate for the majority element.
# - We iterate through the array (voters).
# - If a voter is the same as our candidate, the candidate's vote count increases by 1.
# - If a voter is different, it's an opponent, and they cancel each other out, so the vote count decreases by 1.
# - If the vote count ever drops to 0, our current candidate is "out". The very next element we see
#   becomes the new candidate with a fresh vote count of 1.
#
# At the end of this process, the element that remains as the candidate is our *potential* majority element.
# Why "potential"? Because this algorithm only guarantees finding the correct candidate IF a majority element exists.
# For an array like [1, 2, 3], the candidate at the end would be 3, which is not a majority.
#
# So, the algorithm has two steps:
# 1. Find a candidate: Use the voting process to find the single element that could be the majority.
# 2. Verify the candidate: Do a second, simple pass through the array to count the actual occurrences
#    of the candidate to confirm if it's truly a majority element.

def majorityElN2Op(arr):

    # ----- Step 1: Find the candidate element -----
    candidate = None
    count = 0
    
    for num in arr:
        # If count is 0, it means we have no active candidate.
        # So, we elect the current number 'num' as the new candidate.
        if count == 0:
            count = 1
            candidate = num
        # If the current number is the same as our candidate, it's a "vote for".
        elif candidate == num:
            count += 1
        # If the current number is different, it's a "vote against" (cancellation).
        else: # candidate != num
            count -= 1
            
    # At this point, 'candidate' holds the only element that could be the majority.
    # But we MUST verify it.

    # ----- Step 2: Verify if the candidate is the majority element -----
    n = len(arr)
    # Reset count to do a final, real count of the candidate.
    final_count = 0
    for num in arr:
        if candidate == num:
            final_count += 1
    
    # Check if the verified count is greater than n/2.
    if final_count > n / 2:
        return candidate
    else:
        # This handles cases where no majority element exists.
        return -1


# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? We iterate through the array twice. The first pass is for the voting process (O(N)), and the
# second pass is for verification (O(N)). O(N) + O(N) = O(2N), which simplifies to O(N).
#
# Space Complexity: O(1)
# Why? We only use a few variables ('candidate', 'count', 'final_count'). The memory usage does not
# depend on the size of the input array. This is the main advantage over the hashing approach.
#
# --- HOW TO REMEMBER ---
# Think "Voting/Cancellation". One for me, one for you, they cancel out. The majority group is bigger,
# so one of its members will be left standing at the end. Always remember the two steps: 1. Find Candidate, 2. Verify.

# Example Usage:
arr = [2,2,1,3,1,1,3,1,1]
print(f"Optimal (Moore's Voting) Result: {majorityElN2Op(arr)}") # Expected: 1