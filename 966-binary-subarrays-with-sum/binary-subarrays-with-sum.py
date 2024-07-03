class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {}
        n = len(nums)
        running_sum = cnt =  0

        for right in range(n):
            running_sum += nums[right]
            if running_sum == goal:
                cnt += 1
            
            if running_sum - goal in seen:
                cnt += seen[running_sum - goal]
            seen[running_sum] = seen.get(running_sum,0) + 1

        return cnt

