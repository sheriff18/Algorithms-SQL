from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        threshold = n//3

        hm = Counter(nums)

        outcome = []
        for key,value in hm.items():
            if value > threshold:
                outcome.append(key)
        
        return outcome
        