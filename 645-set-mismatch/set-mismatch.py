from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        hm = Counter(nums)
        repeating = missing = -1

        for key,count in hm.items():
            if count == 2:
                repeating = key

        arr = [num for num in range(1,n+1)]
        for num in arr:
            if num not in nums:
                missing = num

        return [repeating, missing]
        



        
        