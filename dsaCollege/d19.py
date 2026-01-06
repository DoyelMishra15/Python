m=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    for j in range(3):
        if i+j==2:
            print(m[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
    
for i in range(3):
    for j in range(3):
        if i==j:
            print(m[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(3):
    for j in range(3):
        if i==j or i+j==2:
            print(m[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

'''i/p is 3 3
1 2 3
4 5 6
7 8 9'''

r,c=map(int, input().split())
m=[]
for i in range(r):
  l=list(map(int,input().split()))
  m.append(l)
print(m)


'''if i/p=> 3 3
1 2 3 4 5 6 7 8 9'''

