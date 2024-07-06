class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = {}
        cnt = running_sum = 0

        for i in range(n):
            # Convert values to 0s and 1s
            
            
            running_sum += nums[i] % 2

            if running_sum == k:
                cnt += 1

            if running_sum - k in seen:
                cnt += seen[running_sum-k]
            
            seen[running_sum] =  seen.get(running_sum,0) + 1


            

        return cnt
