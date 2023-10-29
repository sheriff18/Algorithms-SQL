https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        nums1 = self.sortArray(nums[:mid])
        nums2 = self.sortArray(nums[mid:])
        return self.merge(nums1, nums2)
    def merge(self, nums1, nums2):
        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            elif nums1[i] >= nums2[j]:
                res.append(nums2[j])
                j+=1
        while i < len(nums1):
            res.append(nums1[i])
            i+=1
        while j < len(nums2):
            res.append(nums2[j])
            j+=1
        return res
