class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findfirst(nums, target):
            n = len(nums)
            low, high,first = 0, n - 1,-1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    first = mid
                    high = mid - 1
            return first

        
        def findlast(nums, target):
            n = len(nums)
            low, high,last = 0, n - 1,-1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    last = mid
                    low = mid + 1
            return last
        
        first, last = findfirst(nums,target),findlast(nums,target)
        if first ==-1:
            return [-1,-1]
        else: 
            return [first,last]

        