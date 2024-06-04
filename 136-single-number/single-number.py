class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}

        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1

        for key,value in hm.items():
            if value == 1:
                return key
        