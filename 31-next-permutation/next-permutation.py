class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        index = -1
        n = len(nums)

        # Look for a breakpoint, where the value of the next index is greater than
        # the current index

        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        # If breakpoint doesnt exist
        if index == -1:
            nums.reverse()
            return nums

        for i in range(n-1,index,-1):
            if nums[i] > nums[index]:
                nums[i],nums[index] = nums[index], nums[i]
                break
        
        nums[index+1:] = reversed(nums[index+1:]) 

        return nums
       
        