class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        min_price = prices[0]
        profit = 0

        for i in range(n):
            maxProfit = prices[i] - min_price
            profit = max(maxProfit,profit)
            min_price = min(min_price,prices[i])

        return profit




        
        
        
	
  

        