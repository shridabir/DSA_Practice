#Q.6 BEST TIME TO BUY AND SELL STOCKS
#profit will be maximum when you buy at minimum price and sell at maximum price
def maximumProfit (prices):
    n = len(prices)
    minPrice = prices[0]
    maxProfit = 0
    for i in range (n):
        cost_price = prices[i] - minPrice #buy at minPrice and sell at prices[i]
        maxProfit = max(maxProfit, cost_price) #update maxProfit
        minPrice = min(minPrice, prices[i]) #update minPrice
    return maxProfit
#Example usage
prices = [7,1,5,3,6,4]
print("Maximum profit is:", maximumProfit(prices))

