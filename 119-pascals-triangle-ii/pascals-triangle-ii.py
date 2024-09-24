class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        base = [1]

        for i in range(1, rowIndex+1):
            base.append(int(base[i-1] * (rowIndex - i+1)/i))

        return base
        
        