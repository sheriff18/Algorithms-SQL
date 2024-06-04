class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = maximum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                maximum = max(maximum,cnt)

            else:
                cnt = 0

        return maximum

        