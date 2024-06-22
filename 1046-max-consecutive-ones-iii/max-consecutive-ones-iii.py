

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = 0
        max_len = 0
        cnt = 0

        while right < n:
            if nums[right] == 0:
                cnt += 1
            
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len
