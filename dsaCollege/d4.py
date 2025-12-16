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

n=1234
temp=n
rev=0
count=0
while temp>0:
    temp1= temp%10
    rev = rev*10 + temp1
    temp=temp//10
print(f"Reverse of the number: {rev}")
#if rev==n:
    #print("Number is palindrome")
    
print(f"Palindrome: {rev==n}")
print()
n=53

count=0
flag=True
for i in range(2,54):
    if n%i==0:
        count+=1
    if count>1:
        flag = False
        break
print(f"num is prime: {flag}")

print()

for i in range(1,6):
    for k in range(6-i-1):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print()

for i in range(1,6):
    for k in range(6-i-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for l in range(2,i+1):
        print("*", end="")
    print()

print()

for i in range(1,6):
    for j in range(i):
        print(" ",end="")
    for k in range(6-i-1):
        print("*",end="")
    for l in range(4-i):
        print("*", end="")
    print()

print()

for i in range(1,6):
    for k in range(6-i-1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for l in range(2,i+1):
        print("*", end="")
    print()
for i in range(1,6):
    for j in range(i):
        print(" ",end="")
    for k in range(6-i-1):
        print("*",end="")
    for l in range(4-i):
        print("*", end="")
    print()

print()

for r in range(4):
    for sp in range(4-r-1):
        print(" ",end="")
    for s in range(2*r + 1):
        print("*",end="")
    print()
for r in range(2,-1,-1):
    for sp in range(2-r+1):
        print(" ",end="")
    for s in range(2*r + 1):
        print("*",end="")
    print()