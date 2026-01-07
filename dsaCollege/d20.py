#1351
'''class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            for j in i:
                if j < 0:
                    c+=1
        return c'''

#73

'''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    l.append((i,j))
        
        for i,j in l:
            for col in range(len(matrix[0])):
                matrix[i][col]=0
            for row in range(len(matrix)):
                matrix[row][j]=0'''

#48


#spiral matrix