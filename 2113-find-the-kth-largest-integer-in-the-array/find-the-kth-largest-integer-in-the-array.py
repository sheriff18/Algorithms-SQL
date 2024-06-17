class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n = len(nums)
        nums = [int(num) for num in nums]
        nums.sort()

        ans = str(nums[n-k])

        return ans
        