from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        el1 = el2 = None
        cnt1 = cnt2 = 0

        for i in range(n):
            if cnt1 == 0 and nums[i] != el2:
                cnt1 = 1
                el1 = nums[i]
            elif cnt2 == 0 and nums[i] != el1:
                cnt2 = 1
                el2 = nums[i]
            elif el1 == nums[i]:
                cnt1 += 1
            elif el2 == nums[i]:
                cnt2 += 1
            else:
                cnt1 -=1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for i in range(n):
            if el1 == nums[i]:
                cnt1 += 1
            elif el2 == nums[i]:
                cnt2 += 1
        my_list = []
        if cnt1 > n // 3:
            my_list.append(el1)
        if cnt2 > n//3 :
            my_list.append(el2)
        
        return my_list