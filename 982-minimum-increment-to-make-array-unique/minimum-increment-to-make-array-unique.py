class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        moves, expected = 0,min(nums)

        for i in range(n):
            if nums[i] < expected:
                moves += expected - nums[i]
                
            else:
                expected = nums[i]
            expected += 1
        
        return moves

        