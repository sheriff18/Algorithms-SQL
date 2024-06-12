# Using the Boyer Moore Majority Vote Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        el = None
        n = len(nums)
        
        # Find the majority element and check if the its count is greater than n/2
        for i in range(n):
            if cnt == 0 and el != nums[i]:
                cnt = 1
                el = nums[i]
            elif el == nums[i]:
                cnt += 1
            else:
                cnt -= 1

            
        cnt = 0

        for i in range(n):
            if nums[i] == el:
                cnt += 1
        
        if cnt >= n//2:
            return el

        return -1
        