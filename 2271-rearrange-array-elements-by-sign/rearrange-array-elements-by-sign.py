class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pos = 0
        neg = 1
  
        arr = [0]*n

        for i in range(n):
            if nums[i] < 0:
                arr[neg] = nums[i]
                neg+= 2
            else:
                arr[pos] = nums[i]
                pos+= 2
        

        

        return arr
        