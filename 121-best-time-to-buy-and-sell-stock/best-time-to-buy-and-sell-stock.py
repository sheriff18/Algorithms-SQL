class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        min_price = prices[0]
        maxProfit = 0

        for i in range(1,n):
            profit = prices[i] - min_price
            maxProfit = max(maxProfit,profit)
            min_price = min(min_price, prices[i])
        return maxProfit
        