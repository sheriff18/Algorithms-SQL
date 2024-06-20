class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n-1
        max_capacity = 0

        while left < right :
            if height[left] < height[right]:
                max_capacity = max(max_capacity, (right - left) * height[left])
                left += 1
            elif height[left] >= height[right]:
                max_capacity = max(max_capacity, (right-left)*height[right])
                right -= 1
        
        return max_capacity




        