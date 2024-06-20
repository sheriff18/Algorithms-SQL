class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        result = sum(nums[:k])
        s = result

        for i in range(k,n):
            s -= nums[i-k]
            s += nums[i]
            result = max(result, s)

        return result/k

            


            
