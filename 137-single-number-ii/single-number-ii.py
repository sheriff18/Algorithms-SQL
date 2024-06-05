from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = Counter(nums)

        for key, value in a.items():
            if value == 1:
                return key

        