https://leetcode.com/problems/sort-array-by-parity-ii/description/


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        my_list = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        for i in range(len(even)):


            my_list.append(even[i])
            my_list.append(odd[i])

        return my_list
