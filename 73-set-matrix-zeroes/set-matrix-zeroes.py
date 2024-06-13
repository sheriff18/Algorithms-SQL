class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n= len(matrix[0])
        m = len(matrix)
        arr = []
       
      
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    arr.append([i,j])


        for i,j in arr:
            for col in range(n):
                matrix[i][col] = 0
            
            for row in range(m):
                matrix[row][j] = 0

        return matrix