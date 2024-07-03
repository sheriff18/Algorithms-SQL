class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = {}
        cnt = running_sum = 0

        for i in range(n):
            running_sum += nums[i]

            if not running_sum % k:
                cnt += 1

            if running_sum % k in seen:
                cnt += seen[running_sum%k] 
            seen[running_sum%k] = seen.get(running_sum%k,0) + 1

        return cnt
        