class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = {}
        cnt = running_sum = 0

        for i in range(n):
            
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
            
            running_sum += nums[i]

            if running_sum == k:
                cnt += 1

            if running_sum - k in seen:
                cnt += seen[running_sum-k]
            
            seen[running_sum] =  seen.get(running_sum,0) + 1


            

        return cnt
