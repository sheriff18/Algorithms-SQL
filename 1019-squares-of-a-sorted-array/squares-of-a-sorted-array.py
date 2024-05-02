class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([a**2 for a in nums])
        