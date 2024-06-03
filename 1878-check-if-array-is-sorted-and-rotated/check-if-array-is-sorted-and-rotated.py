class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        break_point = 0

        for i in range(n):
            if nums[i] > nums[(i+1)%n]: break_point+=1

        if break_point > 1: return False

        return True
        

        
            
        