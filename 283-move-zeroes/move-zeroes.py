class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        arr = []
        
        for num in nums:
            if num != 0:
                arr.append(num)
        
        for i in range(len(arr)):
            nums[i] = arr[i]
            
        for i in range(len(arr),len(nums)):
            nums[i] = 0
        
        return nums

        """
        Do not return anything, modify nums in-place instead.
        """
        

            
            

        
        





    
      

