https://leetcode.com/problems/h-index/submissions/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort(reverse=True)

        
        for i in range(n):
            if citations[i] < i+1:
                return i
        

        if len(citations) == 1 and len(citations) > 0:
            return 1
        if citations[n-1] >= n:
            return n
