
"""
Problem: Minimize Max Distance to Gas Station
Platform: GeeksforGeeks / LeetCode
Difficulty: Hard
Topics: Array, Binary Search, Heap (Priority Queue)
LINK: https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
"""

# ==============================================================================
# PROBLEM ANALYSIS
# ==============================================================================

"""
PROBLEM BREAKDOWN:
- Input: A sorted list of integers `stations` representing their positions, and an integer `k` representing the number of new gas stations to add.
- Output: The smallest possible value for the maximum distance 'd' between any two adjacent gas stations after adding `k` new stations.
- Constraints:
  - 10 <= n <= 10000
  - 0 <= stations[i] <= 10^9
  - 0 <= k <= 10^5
- Edge Cases: If k=0, the answer is the largest initial gap between stations.

APPROACH:
The core of the problem is to minimize a maximum value (the distance 'd'). This pattern points towards a few potential solutions:
1.  A greedy approach where we iteratively place stations in the largest gaps.
2.  A more efficient greedy approach using a priority queue to quickly find the largest gap.
3.  Binary search on the answer, where we search for the optimal value of 'd' itself.
"""

# ==============================================================================
# SOLUTION 1: BRUTE FORCE APPROACH
# ==============================================================================
from typing import List

def minimizeMaxGasBrute(arr: List[int],k: int) -> int:
    """
    BRUTE FORCE APPROACH - Greedily place stations one by one.

    Intuition:
    To minimize the maximum distance, 
    it always makes sense to place the next gas station in the currently largest gap. 
    This greedy strategy should lead us to the optimal arrangement. 
    We can repeat this process `k` times.

    Approach:
    1. Create an array `howMany` of size `n-1` 
        to store the number of new stations placed in each initial gap. Initialize with zeros.
    2. Loop `k` times to place each of the `k` gas stations.
    3. In each iteration of the loop:
       a. Find the largest current section. Iterate through all `n-1` sections.
       b. The length of a section `i` is `(stations[i+1] - stations[i]) / (howMany[i] + 1)`.
       c. Keep track of the section with the maximum length and its index.
    4. After finding the largest section, place a gas station in it 
        by incrementing `howMany` at that index.
    5. After the loop finishes, calculate the final maximum distance by 
        checking all resulting section lengths.

    Time Complexity: O(k * n) - For each of the `k` stations, we iterate through `n` sections to find the max.
    Space Complexity: O(n) - To store the `howMany` array.
    """
    n = len(arr)

    howMany = [0] * (n - 1)

    # Note: The loop should go from 1 to k, range(1, k+1)
    for gasStations in range(1,k + 1):
        maxSection = -1.0
        maxInd = -1

        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            sectionLen = diff / (howMany[i] + 1)
            if sectionLen > maxSection:
                maxSection = sectionLen
                maxInd = i

        howMany[maxInd] += 1

    ans = -1.0

    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        sectionLen = diff / (howMany[i] + 1)
        ans = max(ans,sectionLen)

    return ans

# ==============================================================================
# SOLUTION 2: BETTER APPROACH (Using Priority Queue)
# ==============================================================================
import heapq
from decimal import Decimal, ROUND_HALF_UP

def minMaxGasBetter(arr: List[int], k: int) -> int:
    """
    BETTER APPROACH - Using a Max Priority Queue to optimize finding the largest gap.

    Intuition:
    The brute-force approach is slow because it repeatedly scans all sections to find the largest one. We can significantly speed this up by using a data structure that provides the largest section efficiently. A max-priority queue is perfect for this.

    Approach:
    1. Create an array `howMany` of size `n-1` to store station counts.
    2. Create a max-priority queue. Since `heapq` is a min-heap, we store negative values to simulate a max-heap.
    3. Push the initial section lengths (and their indices) into the priority queue. The items will be `(-section_length, index)`.
    4. Loop `k` times:
       a. Pop the top element from the priority queue. This is the largest current section.
       b. Increment the number of stations for this section in the `howMany` array.
       c. Calculate the new, smaller section length that results from adding a station.
       d. Push the new section length back into the priority queue.
    5. After the loop, the top of the priority queue holds the largest section length, which is our answer.

    Time Complexity: O(n*log(n) + k*log(n)) - O(n*log(n)) to build the heap and O(k*log(n)) for k push/pop operations.
    Space Complexity: O(n) - For the `howMany` array and the priority queue.
    """
    n = len(arr)
    howMany = [0] * (n - 1)
    pq = []

    # Initialize priority queue with initial section lengths
    for i in range(n - 1):
        diff = arr[i + 1] - arr[i]
        # Push negative diff to simulate max-heap
        heapq.heappush(pq, (-diff, -i))

    # Place k stations
    for _ in range(k):
        # Get the largest section
        neg_diff, neg_idx = heapq.heappop(pq)
        idx = -neg_idx
        # Place one station in this section
        howMany[idx] += 1

        # Calculate new section length and push back
        initial_diff = arr[idx + 1] - arr[idx]
        new_section_len = initial_diff / (howMany[idx] + 1)
        heapq.heappush(pq, (-new_section_len, -idx))

    # The top of the heap is the max distance


    ans, _ = heapq.heappop(pq)
    # PYTHON IS STUPID, if u try to use round on 8.325, it will make it closer to even
    # 8.32 not 8.33
    # below is the hacky way
    return float(Decimal(str(-ans)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

# ==============================================================================
# SOLUTION 3: OPTIMAL APPROACH (Binary Search on Answer)
# ==============================================================================
import math

def numOfGasStationReq(distance, arr):
    """
    Helper function to calculate how many stations are needed to ensure
    no distance between stations is greater than `distance`.
    """
    cnt = 0
    for i in range(len(arr) - 1):
        gap = arr[i+1] - arr[i]
        # if gap is 10 and distance is 3, we need floor(10/3) = 3 stations.
        # if gap is 9 and distance is 3, we need floor(9/3) = 3 stations, but we only need 2.
        # The number of new stations needed is ceil(gap/distance) - 1
        if gap > distance:
             cnt += math.ceil(gap / distance) - 1
    return cnt

def minMaxGasOp(arr: List[int], k: int) -> int:
    """
    OPTIMAL APPROACH - Binary Search on the Answer.

    Intuition:
    Instead of placing stations, we can search for the answer itself. The "answer" is the minimum possible value of the maximum distance, let's call it `d`.
    There's a monotonic property: if we can achieve a max distance of `d` with `k` stations, we can surely achieve a max distance of `d+0.1` (or any larger value) with `k` or fewer stations. This monotonicity allows binary search.

    Approach:
    1. Define the search space for the answer `d`.
       - `low = 0` (the smallest possible distance).
       - `high = max initial gap` (the largest possible distance, when k=0).
    2. Perform binary search on this range `[low, high]`.
    3. For each `mid` value (our potential answer for `d`):
       a. Check if it's possible to achieve this max distance `mid` by adding at most `k` stations.
       b. This check is done by a helper function `numOfGasStationReq(mid, arr)` which calculates how many stations are needed.
    4. Adjust the search space:
       - If `numOfGasStationReq(mid, arr) <= k`, it means `mid` is a possible answer. We try for an even smaller `d`, so `high = mid`.
       - If `numOfGasStationReq(mid, arr) > k`, `mid` is too small. We need to allow a larger distance, so `low = mid`.
    5. The loop continues until `high - low` is smaller than the required precision (e.g., 1e-6).

    Time Complexity: O(n * log(L/precision)) where L is the range of search space (high - low).
    Space Complexity: O(1)
    """
    arr.sort()
    n = len(arr)
    low = 0.0
    high = 0.0

    high = max(arr[i + 1] - arr[i] for i in range(n - 1))

    # Binary search for the answer
    while high - low > 1e-2: # Precision for competitive programming
        mid = (low + high) / 2.0
        if mid == 0: # Avoid division by zero
            low = 1e-2
            continue

        stations_needed = numOfGasStationReq(mid, arr)

        if stations_needed <= k:
            # This distance is achievable, try for a smaller one
            high = mid
        else:
            # This distance is too small, need to allow a larger distance
            low = mid

    return round(high, 2)


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    arr = [
        2, 56, 95, 157, 265, 292, 296, 408, 427, 435, 444, 607, 621, 731, 754, 772, 863, 972, 1014, 1171,
        1282, 1372, 1579, 1689, 1734, 1738, 2080, 2113, 2114, 2269, 2275, 2447, 2619, 2642, 2713, 2736,
        2769, 2839, 2885, 3017, 3067, 3082, 3130, 3210, 3261, 3362, 3418, 3441, 3528, 3643, 3681, 3735,
        3857, 3950, 3979, 4067, 4193, 4196, 4205, 4285, 4439, 4484, 4619, 4674, 4776, 4977, 5129, 5242,
        5300, 5412, 5436, 5471, 5492, 5525, 5545, 5561, 5586, 5624, 5630, 5682, 5702, 5705, 5778, 5966,
        6050, 6163, 6276, 6286, 6290, 6396, 6453, 6527, 6719, 6974, 6977, 6984, 7103, 7257, 7359, 7481,
        7723, 7799, 7949, 8329, 8350, 8422, 8463, 8469, 8776, 8787, 8830, 8860, 8902, 8915, 9022, 9077,
        9170, 9263, 9282, 9315, 9464, 9561, 9689, 9792, 9809, 10017, 10122, 10161, 10209, 10317, 10356,
        10404, 10557, 10754, 10802, 10805, 10810, 11009, 11123, 11137, 11368, 11461, 11505, 11565, 11612,
        11668, 11711, 11832, 11875, 11886, 11989, 12081, 12156, 12193, 12315, 12323, 12344, 12345, 12347,
        12365, 12375, 12483, 12582, 12620, 12661, 13023, 13121, 13156, 13170, 13221, 13277, 13292, 13353,
        13497, 13515, 13583, 13642, 13848, 13862, 13886, 13955, 14110, 14178, 14275, 14327, 14404, 14512,
        14515, 14617, 14734, 14821, 14888, 14919, 14993, 15168, 15182, 15256, 15326, 15364, 15375, 15450,
        15586, 15667, 15679, 15744, 15788, 16024, 16033, 16092, 16175, 16202, 16248, 16316, 16396, 16488,
        16516, 16724, 16780, 16807, 16816, 16933, 16976, 17114, 17182, 17266, 17269, 17301, 17322, 17673,
        17685, 17885, 17967, 18048, 18176, 18196, 18256, 18264, 18276, 18310, 18355, 18373, 18401, 18419,
        18612, 18639, 18758, 18796, 18805, 18848, 18857, 19012, 19040, 19046, 19081, 19120, 19136, 19175,
        19310, 19323, 19593, 19681, 19854, 19931, 20181, 20203, 20207, 20379, 20506, 20657, 20662, 20811,
        20844, 20941, 20945, 21209, 21245, 21368, 21620, 21667, 21967, 22209, 22253, 22588, 22619, 22663,
        22686, 22713, 22732, 23074, 23108, 23110, 23135, 23210, 23347, 23387, 23440, 23487, 23516, 23530,
        23563, 23571, 23584, 23644, 23685, 23783, 23895, 23923, 24120, 24204, 24241, 24394, 24894, 25004,
        25145, 25184, 25290, 25294, 25622, 25723, 25769, 25776, 25848, 25967, 25996, 26033, 26263, 26393,
        26422, 26508, 26551, 26657, 26784, 26934, 26997, 27071, 27134, 27337, 27350, 27600, 27725, 27756,
        27953, 27989, 28105, 28138, 28311, 28416, 28464, 28479, 28492, 28526, 28564, 28697, 28805, 28901,
        29086, 29114, 29160, 29211, 29249, 29283, 29308, 29424, 29527, 29623, 29637, 29715, 29749, 29757,
        29871, 29979, 30057, 30170, 30204, 30243, 30257, 30283, 30308, 30392, 30502, 30721, 30742, 30752,
        30817, 30883, 30989, 31049, 31178, 31217, 31277, 31384, 31527, 31869, 32009, 32135, 32227, 32232,
        32252, 32472, 32492, 32496, 32500, 32554, 32558, 32656
    ]
    k = 22320
    print("--- Test Case 1 ---")
    # print(f"Stations: {arr}, k: {k}")
    print(f"Brute Force Result: {minimizeMaxGasBrute(arr,k):.2f}")
    print(f"Better (Heap) Result: {minMaxGasBetter(arr,k):.2f}")
    print(f"Optimal (Binary Search) Result: {minMaxGasOp(arr,k):.2f}")
    print("\n")

    arr2 = [1,2,4,5,6]
    k2 = 4
    print("--- Test Case 2 ---")
    print(f"Stations: {arr2}, k: {k2}")
    print(f"Brute Force Result: {minimizeMaxGasBrute(arr2,k2):.2f}")
    print(f"Better (Heap) Result: {minMaxGasBetter(arr2,k2):.2f}")
    print(f"Optimal (Binary Search) Result: {minMaxGasOp(arr2,k2):.2f}")
