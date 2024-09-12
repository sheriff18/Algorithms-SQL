class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1

        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2

            if mid*mid < x:
                left = mid + 1
            elif mid*mid > x:
                right = mid - 1
            else:
                return mid
        return right



        