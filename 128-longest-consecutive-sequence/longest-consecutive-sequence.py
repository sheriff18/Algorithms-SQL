class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set()
        n = len(nums)
        longest = 1
        if n == 0:
            return 0
        
        for num in nums:
            Set.add(num)

        for val in Set:
            if val - 1 not in Set:
                cnt = 1
                x = val

                while x+1 in Set:
                    cnt += 1
                    x += 1

                longest = max(longest,cnt)

        return longest
                
        
        
       