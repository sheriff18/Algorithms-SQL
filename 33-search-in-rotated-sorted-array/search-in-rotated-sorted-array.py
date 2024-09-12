# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         low, high = 0, n-1
#         arr = nums
        

#         while low <= high:
#             mid  = low + (high-low) // 2
#             if nums[mid] == target:
#                 return mid 

#             elif arr[low] <= arr[mid]:
#                 if arr[low] <= target < arr[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 if arr[mid] <= target < arr[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#         return -1


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # If the target is found at mid
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[low] <= nums[mid]:
                # Target lies within the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half is sorted
            else:
                # Target lies within the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Target not found
        return -1

            