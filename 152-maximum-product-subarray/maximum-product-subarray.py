class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = suffix = 1
        maxSum = float('-inf')

        for i in range(n):
            
            if suffix == 0:
                suffix = 1
            if prefix == 0:
                prefix = 1

            prefix *= nums[i]
            suffix *= nums[n-i-1]

            maxSum = max(maxSum,suffix,prefix)
        return maxSum
