class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(n-1):
                if int(str(nums[j])+str(nums[j+1])) < int(str(nums[j+1])+ str(nums[j])):
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        res = "".join(map(str,nums))
        if int(res) == 0:
            res = '0'
        return res
    
        
        