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

'''class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i<j:
                    matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()'''

'''class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]= matrix[j][i],matrix[i][j]
            matrix[i]=matrix[i][::-1]'''

#867 did it by myself

'''class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        return result'''

#1886

'''class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        p=0
        while p<4 and mat!=target:
            for i in range(len(mat)):
                for j in range(i+1,len(mat[0])):
                    mat[i][j],mat[j][i]= mat[j][i],mat[i][j]
                mat[i]=mat[i][::-1]
            p+=1
        return mat==target'''

#3242


#spiral matrix