from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = Counter(nums)
        for x,y in a.items():
            if y > 1:
                return x
