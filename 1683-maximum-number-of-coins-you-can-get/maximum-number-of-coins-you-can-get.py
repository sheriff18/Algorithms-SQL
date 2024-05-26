class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        i = 0
        j = n-2
        k = n-1
        tot = 0

        while i < k:
            tot += piles[j]
            i += 1
            k -= 2
            j -= 2
        
        return tot
