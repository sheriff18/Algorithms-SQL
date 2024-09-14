class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n-1
        arr = nums

        while low <= high:
            mid  = low + (high - low) // 2
            if nums[mid] == target:
                return True
            
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            
            elif arr[low] <= arr[mid]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < target <= arr[high]:

                    low = mid + 1
                else:
                    high = mid - 1

        return False
                    