import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = [i for i in range(int(math.sqrt(c))+1)]
        n = len(arr)

        left, right = 0, n-1

        while left <= right:
            num = arr[left]**2 + arr[right]**2
            if num < c:
                left += 1
            elif num > c:
                right -= 1
            else:
                return True
        return False