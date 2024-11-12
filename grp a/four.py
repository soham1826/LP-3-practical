# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapSack(W, wt, val, n): 
    dp = [0 for i in range(W+1)]  # Making the dp array

    # Iterate over all items
    for i in range(1, n+1): 
        # Iterate from back to front for the current item
        for w in range(W, 0, -1): 
            # If the item can be included in the knapsack
            if wt[i-1] <= w: 
                # Update the dp array to include the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]] + val[i-1]) 

    return dp[W]  # Return the maximum value of the knapsack

# Driver code 
val = [60, 100, 120]  # Values of the items
wt = [10, 20, 30]     # Weights of the items
W = 50                # Capacity of the knapsack
n = len(val)          # Number of items

# Function call to get the maximum value
print(knapSack(W, wt, val, n))
