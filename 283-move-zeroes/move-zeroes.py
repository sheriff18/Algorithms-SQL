class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        a = nums
        j = -1
    # Place the pointer j
        for i in range(n):
            if a[i] == 0:
                j = i
                break
    
    # No non-zero elements
        if j == -1:
            return a
    
    # Move the pointers i and j and swap accordingly
        for i in range(j + 1, n):

            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j += 1
    
        return a
        # j = -1
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] == 0:
        #         j = i
        #         break 
        
        # for i in range(j+1,n):
        #     if nums[i] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j += 1

        # return nums

        """
        Do not return anything, modify nums in-place instead.
        """
        

            
            

        
        





    
      

