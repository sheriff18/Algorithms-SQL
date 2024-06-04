class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3

        hm = {}

        for num in nums:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        outcome = []
        for key,value in hm.items():
            if value > threshold:
                outcome.append(key)
        
        return outcome
        