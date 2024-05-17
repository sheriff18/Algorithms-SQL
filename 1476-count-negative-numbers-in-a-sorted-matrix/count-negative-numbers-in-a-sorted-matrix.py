class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in grid:
            for num in row:
                if num < 0:
                    cnt +=1
        return cnt
        