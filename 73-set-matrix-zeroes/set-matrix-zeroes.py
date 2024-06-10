class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n= len(matrix[0])
        m = len(matrix)
        arr = []
       
      
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    arr.append([row,col])
        
        for i,j in arr:
            for row in range(m):
                matrix[row][j] = 0
            for col in range(n):
                matrix[i][col] = 0

        return matrix