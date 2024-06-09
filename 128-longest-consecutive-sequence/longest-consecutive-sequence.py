class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        cnt = 0
        longest = 1
        last_smaller = float('-inf')
        if n == 0:
            return 0
        
        for j in range(n):
            if nums[j]-1 == last_smaller:
                cnt += 1
                last_smaller = nums[j]
            elif nums[j] != last_smaller:
                cnt = 1
                last_smaller = nums[j]
            longest = max(longest, cnt)
        return longest
        
      
 
        