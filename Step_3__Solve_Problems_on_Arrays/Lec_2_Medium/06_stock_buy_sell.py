# =================================================================================================
# PROBLEM: Best Time to Buy and Sell Stock
# =================================================================================================
#
# Given an array of prices where `prices[i]` is the price of a given stock on the `i-th` day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any
# profit, return 0.
#
# For example:
# Input: arr = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# The problem will be solved in two ways:
# 1. Brute Force: The simplest solution that tries all possibilities.
# 2. Optimal: A much more efficient single-pass solution.
#
# =================================================================================================


# =================================================================================================
# Approach 1: Brute Force (Try every possible pair of buy and sell days)
# =================================================================================================

# --- INTUITION ---
# The most direct way to solve this is to try every single valid combination of buying and selling.
# What does a valid combination mean? It means picking a day `i` to buy and a day `j` to sell,
# with the only condition being that you must sell *after* you buy (i.e., `j > i`).
#
# So, the plan is:
# 1. Pick a day to buy the stock.
# 2. Then, for that buy day, try selling it on every subsequent day.
# 3. Calculate the profit for each of these transactions.
# 4. Keep track of the highest profit found so far.
# This naturally leads to a nested loop structure.

# --- ALGORITHM ---
# 1. Initialize `maxProfit` to 0. (If we can't make a profit, the answer is 0).
# 2. Use a loop `i` from 0 to n-1 to represent the "buy day".
# 3. Inside it, use another loop `j` from `i + 1` to n-1 to represent the "sell day".
# 4. For each pair (i, j), calculate the profit: `arr[j] - arr[i]`.
# 5. If this profit is greater than `maxProfit`, update `maxProfit`.
# 6. After checking all pairs, `maxProfit` will hold the answer.

def stockBuySellBrute(arr):
    n = len(arr)

    # Initialize maxProfit to 0, as profit cannot be negative.
    # If no profitable transaction is found, 0 will be the correct answer.
    maxProfit = 0
    buy_day_price, sell_day_price = arr[0], arr[0] # To store the prices for the best transaction

    # Outer loop iterates through all possible "buy" days.
    for i in range(n):
        # Inner loop iterates through all possible "sell" days *after* the buy day.
        for j in range(i + 1, n):
            # Calculate profit for the current buy/sell pair.
            profit = arr[j] - arr[i]
            
            # If we found a better profit, update our records.
            if profit > maxProfit:
                maxProfit = profit
                buy_day_price = arr[i]
                sell_day_price = arr[j]

    return {'max_profit': maxProfit, 'buy_price': buy_day_price, 'sell_price': sell_day_price}

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N^2)
# Why? We have two nested loops. The outer loop runs N times, and the inner loop runs, on average,
# N/2 times. This results in a time complexity of O(N*N).
#
# Space Complexity: O(1)
# Why? We only use a few variables to store the state (`maxProfit`, `i`, `j`, etc.),
# which does not depend on the size of the input array.
#
# --- HOW TO REMEMBER ---
# Brute Force = "Try every pair". In this problem, it's every valid (buy, sell) day pair.
# Nested loops are a clear indicator of this approach.

arr = [7,1,5,3,6,4]
print(f"Brute Force Result: {stockBuySellBrute(arr)}") # Expected: {'max_profit': 5, 'buy_price': 1, 'sell_price': 6}

# =================================================================================================
# Approach 2: Optimal (Single Pass)
# =================================================================================================

# --- INTUITION ---
# The brute-force approach is slow because it re-evaluates past days unnecessarily. We can be smarter.
# Let's try to solve this in a single pass.
# As we iterate through the array of prices, let's think about what we need to know at any given day `i`.
# To calculate the maximum profit if we sell on day `i`, we need to subtract the *lowest price we have seen so far* from the current price `arr[i]`.
#
# This is the key idea: we only need to maintain two pieces of information as we loop:
# 1. The minimum stock price encountered so far.
# 2. The maximum profit we could have made so far.
#
# By keeping track of the "cheapest day to buy" found up to the current point, we can instantly
# calculate the best possible profit if we were to sell today.

# --- ALGORITHM ---
# 1. Initialize `max_profit` to 0.
# 2. Initialize a variable `min_price_so_far` to the price on the first day, `arr[0]`.
# 3. Iterate through the array from the second day (`i = 1` to `n-1`).
# 4. For each day `i`:
#    a. Calculate the potential profit if we sell today: `current_profit = arr[i] - min_price_so_far`.
#    b. Update `max_profit` with this `current_profit` if it's higher: `max_profit = max(max_profit, current_profit)`.
#    c. Update `min_price_so_far` with the current day's price if it's a new minimum: `min_price_so_far = min(min_price_so_far, arr[i])`.
# 5. Return `max_profit`.

def stockBuySellOp(arr):
    n = len(arr)
    
    # Initialize max profit to 0.
    max_profit = 0
    # The minimum price seen so far is initialized to the first day's price.
    min_price_so_far = arr[0]
    
    # We will also track the prices for the best transaction found.
    # Initially assume buying and selling on day 0 for 0 profit.
    buy_price = arr[0]
    sell_price = arr[0]

    # Start from the second day since we can't buy and sell on the same day for a profit.
    for i in range(1, n):
        # Calculate the potential profit if we sell on the current day `i`.
        # The best time to have bought would have been at the minimum price seen before today.
        current_profit = arr[i] - min_price_so_far
        
        # If this transaction yields a better profit, update our max_profit and the corresponding buy/sell prices.
        if current_profit > max_profit:
            max_profit = current_profit
            # The sell price is the current price.
            sell_price = arr[i]
            # The buy price was the minimum we had tracked to get this profit.
            buy_price = min_price_so_far

        # After checking for profit, update the minimum price seen so far.
        # This prepares us for future days.
        if arr[i] < min_price_so_far:
            min_price_so_far = arr[i]
    
    return {'max_profit': max_profit, 'buy_price': buy_price, 'sell_price': sell_price}

# --- COMPLEXITY ANALYSIS ---
# Time Complexity: O(N)
# Why? We iterate through the array only once.
#
# Space Complexity: O(1)
# Why? We use a constant number of variables (`max_profit`, `min_price_so_far`, etc.)
# regardless of the input size.
#
# --- HOW TO REMEMBER ---
# Optimal = "One Pass, Track the Minimum".
# As you walk through the prices, just remember the lowest price you've seen.
# At each step, you can instantly check the "sell now" profit and update your overall max.

arr = [7,1,5,3,6,4]
print(f"Optimal Approach Result: {stockBuySellOp(arr)}") # Expected: {'max_profit': 5, 'buy_price': 1, 'sell_price': 6}