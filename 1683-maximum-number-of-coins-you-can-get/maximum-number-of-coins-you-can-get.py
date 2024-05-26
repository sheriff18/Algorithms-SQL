class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse= True)
        n = len(piles)
        tot = 0
        
        for i in range(1, n//3*2,2):
            tot += piles[i]
        return tot
