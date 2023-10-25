https://leetcode.com/problems/matrix-cells-in-distance-order/solutions/278786/python-1-line-sorting-based-solution/

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return [[a,b] for a in range(rows) for b in range(cols)]
        
