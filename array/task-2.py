def maxProfit(prices):
    # Initialize two pointers, l (left) and r (right), and maxProfit
    l, r = 0, 1
    maxProfit = 0

    # Iterate through the list with the right pointer
    while r < len(prices):
        # Check if the current price at left pointer is less than at right pointer
        if prices[l] < prices[r]:
            # Calculate the profit if we buy at l and sell at r
            profit = prices[r] - prices[l]
            # Update maxProfit if the current profit is greater than maxProfit
            maxProfit = max(profit, maxProfit)
        else:
            # Move the left pointer to the right pointer if prices[r] is less than prices[l]
            l = r
        # Move the right pointer to the next position
        r += 1

    # Return the maximum profit found
    return maxProfit


# Example usage
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5

# Time Complexity: O(n)
# Space Complexity: O(1)
