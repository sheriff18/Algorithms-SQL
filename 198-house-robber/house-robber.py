class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0
        n = len(nums)

        for i in range(n):
            current = max(nums[i] + prev2,prev1)
            prev2 = prev1
            prev1 = current
        
        return current