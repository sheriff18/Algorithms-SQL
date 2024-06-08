class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        mini = prices[0]
        

        for i in range(n):
            cost = prices[i] - mini
            profit = max(profit, cost)
            mini = min(mini,prices[i])

        return profit




        
        
        
	
  

        