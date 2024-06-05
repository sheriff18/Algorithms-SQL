from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hashing = [0] * (n + 1)

        for num in nums:
            hashing[num] += 1

        for i in range(n + 1):
            if hashing[i] == 0:
                return i
