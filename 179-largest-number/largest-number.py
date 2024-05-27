class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        arr = [str(num) for num in nums]

        arr.sort(key=lambda x:x*10, reverse = True)

        if arr[0] == '0':
            return '0'

        return ''.join(arr)

        
        
        