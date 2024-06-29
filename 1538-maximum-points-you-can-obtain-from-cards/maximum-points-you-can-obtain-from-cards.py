class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        lsum = sum(cardPoints[:k])
        rsum = 0
        maxSum = lsum

        for i in range(1,k+1):
            lsum -=  cardPoints[k-i] 
            rsum += cardPoints[n-i]
            maxSum = max(maxSum, lsum+rsum)
        
        return maxSum

            

        
            