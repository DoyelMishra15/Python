#hashmap,matrix,fast and slow, sliding window

#54

#wrong one
'''class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        t,b,l,r=0,len(matrix)-1,0,len(matrix[0])-1
        while t <= b and l<=r:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            #t-b -> r-=1
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            #r-l -> b-=1
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b-=1
            #b-t -> l+=1
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res'''

