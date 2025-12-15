# range(x,y,z)
# x is starting, y ending, z is step(inc/decrease)

#y is excluded, i.e will consider till y-1 value

for i in range(1,10):
    print(i)

for i in range(1,10,1):
    print(i)

for i in range(1,11,3):
    print(i)

for i in range(1,10):
    print(i, end=" ")

for i in range(10,0,-2):
    print(i)

##first 10 natural num

for i in range(1,11):
    print(i, end=" ")

##first 10 natural num

for i in range(1,11):
    print(i, end=" ")
    if i==5:
        break

for i in range(1,11):
    if i==5 or i==7:
        continue
    print(i, end=" ")

for i in range(1,11):
    print(i)
    #if i==7:
        #break
else:
    print("xhfhr")

# else block is executed if loop is run without breaking

#Sum of First 10 Natural Numbers
sum=0#flag variable, where we make an assumption
for i in range(1,11):
    sum+=i
print(sum)

x,y=15,17
print(f"sum of x and y: {x+y}")

x,y=15,17
print("sum of x and y: {}".format(x+y))

x=int(input())
for i in range(1,x+1):
    print(f"Number is : {i} and cube of the {i} is :{i**3}")

x=int(input())
print()
for i in range(1,11):
    print(f"{x} X {i} = {x*i}")

# Factorial Calculation
x=int(input())
print()
fact=1
for i in range(1,x+1):
    fact*=i
print(f"The Factorial of {x} is: {fact}")

#  Harmonic Series and Their Sum


#Sum of Series [9 + 99 + 999 + …]


#Sum of Series [1 - X²/2! + X⁴/4! - …]



