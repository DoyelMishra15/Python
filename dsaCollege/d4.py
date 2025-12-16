for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
print()

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()
    
print()

for i in range(1,5):
    for j in range(1,5):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print()

for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or i==5 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end=" ")
    print()

print()

for i in range(5):
    for j in range(i):
        print(" ",end=" ")
    for k in range(5-i):
        print("*",end=" ")
    print()

print()

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print("*",end="")
    print()


print()

