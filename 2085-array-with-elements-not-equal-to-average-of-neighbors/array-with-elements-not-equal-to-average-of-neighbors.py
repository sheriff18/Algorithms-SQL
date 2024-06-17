# Wiggle sort
"""Sorting an array of distinct integers in such a way where nums[i-1] < nums[i] > nums[i+1] ensures that (nums[i-1] + nums[i+1]) / 2 < nums[i].

Approach
Iterate through the array from index 1 and swap two elements if,

The index is an odd number and the previous number is greater than current number.

or

The index is an even number and the previous number is smaller or equal to the current number"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if (i%2==0) and nums[i] > nums[i+1] or  (i %2 == 1) and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums 

        