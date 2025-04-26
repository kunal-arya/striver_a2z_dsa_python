# --------------------------------------------
# Hashing in Python - Notes + Code
# --------------------------------------------

# --------------------------------------------
# 1. Python Maps / Hashmaps Basics
# --------------------------------------------

# Basic dict (HashMap) example
# In Python, dict is a hashmap (key-value pairs with O(1) access time)
hashmap = {}
hashmap['apple'] = 10
hashmap['banana'] = 5
hashmap['cherry'] = 7

print(hashmap['apple'])  # Output: 10

# Dict is ordered (insertion order preserved) from Python 3.7+
ordered_map = {'first': 1, 'second': 2, 'third': 3}
print(ordered_map)  # Output: {'first': 1, 'second': 2, 'third': 3}

# Using defaultdict (auto-assigns a default value if key not present)
from collections import defaultdict

default_map = defaultdict(int)  # default value = 0
default_map['dog'] += 1
default_map['cat'] += 1
default_map['dog'] += 1

print(default_map)  # Output: defaultdict(<class 'int'>, {'dog': 2, 'cat': 1})

# Using Counter (special case for counting elements)
from collections import Counter

counter_map = Counter(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
print(counter_map)  # Output: Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Key Points:
# - dict is ordered (since Python 3.7)
# - dict is implemented using hash tables internally
# - defaultdict is useful for automatic default values
# - Counter is useful for counting frequency

# --------------------------------------------
# 2. Hashing Problems
# --------------------------------------------

# Problem:
# Given an array, answer queries about the frequency of a number.

# Brute Force Approach (Time Complexity: O(Q * N))
def brute_force_count(arr, queries):
    results = []
    for query in queries:
        count = 0
        for num in arr:
            if num == query:
                count += 1
        results.append(count)
    return results

# Optimized Approach using Hashing with Array (Only for small numbers)
def optimized_count_array_hashing(arr, queries):
    # Assumption: maximum element is small (e.g., <= 1000)
    max_element = max(arr) if arr else 0
    hash_arr = [0] * (max_element + 1)  # create hash array of size (max_element + 1)

    # Precompute frequencies
    for num in arr:
        hash_arr[num] += 1

    # Fetch the frequencies for queries
    results = []
    for query in queries:
        if query <= max_element:
            results.append(hash_arr[query])
        else:
            results.append(0)
    return results

# Optimized Approach using Dictionary (For large numbers, 10^9 etc.)
def optimized_count_dict_hashing(arr, queries):
    hash_map = {}

    # Precompute frequencies
    for num in arr:
        hash_map[num] = hash_map.get(num, 0) + 1

    # Fetch the frequencies for queries
    results = []
    for query in queries:
        results.append(hash_map.get(query, 0))
    return results

# --------------------------------------------
# 3. Character Hashing
# --------------------------------------------

# Brute Force Approach for characters (O(Q * N))
def brute_force_char_count(s, queries):
    results = []
    for ch in queries:
        count = 0
        for c in s:
            if c == ch:
                count += 1
        results.append(count)
    return results

# Optimized Character Hashing (Only lowercase letters a-z)
def optimized_char_hashing_lowercase(s, queries):
    hash_arr = [0] * 26  # Only 26 lowercase letters

    # Precompute frequencies
    for c in s:
        hash_arr[ord(c) - ord('a')] += 1

    # Fetch frequencies
    results = []
    for ch in queries:
        results.append(hash_arr[ord(ch) - ord('a')])
    return results

# Optimized Character Hashing (Mixed case letters, full ASCII)
def optimized_char_hashing_ascii(s, queries):
    hash_arr = [0] * 256  # Full ASCII table

    # Precompute frequencies
    for c in s:
        hash_arr[ord(c)] += 1

    # Fetch frequencies
    results = []
    for ch in queries:
        results.append(hash_arr[ord(ch)])
    return results

# Optimized Character Hashing using Dictionary
def optimized_char_hashing_dict(s, queries):
    hash_map = {}

    # Precompute frequencies
    for c in s:
        hash_map[c] = hash_map.get(c, 0) + 1

    # Fetch frequencies
    results = []
    for ch in queries:
        results.append(hash_map.get(ch, 0))
    return results

# --------------------------------------------
# 4. Example Usage
# --------------------------------------------

if __name__ == "__main__":
    # Example 1: Number Hashing
    arr = [1, 3, 2, 1, 3]
    queries = [1, 4, 2, 3, 12]

    print("Brute Force Count:", brute_force_count(arr, queries))
    print("Optimized Array Hashing:", optimized_count_array_hashing(arr, queries))
    print("Optimized Dictionary Hashing:", optimized_count_dict_hashing(arr, queries))

    # Example 2: Character Hashing
    s = "abcdabefc"
    char_queries = ['a', 'g', 'h', 'b', 'c']

    print("\nBrute Force Char Count:", brute_force_char_count(s, char_queries))
    print("Optimized Lowercase Hashing:", optimized_char_hashing_lowercase(s, char_queries))
    print("Optimized ASCII Hashing:", optimized_char_hashing_ascii(s, char_queries))
    print("Optimized Dictionary Char Hashing:", optimized_char_hashing_dict(s, char_queries))
