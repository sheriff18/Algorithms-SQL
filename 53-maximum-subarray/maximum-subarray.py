class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        Sum = 0

        for i in range(n):
            Sum += nums[i]
            maxi = max(maxi,Sum)

            if Sum < 0:
                Sum = 0

        return maxi

            

        