

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        n = len(nums)
        left = right = total = 0

        while right < n:
            total += nums[right]
            

            while total >= target:
                length = right - left + 1
                
                min_len = min(min_len, length)
                total -= nums[left]
                left += 1
            right +=1
                
        return min_len if min_len != float('inf') else 0
