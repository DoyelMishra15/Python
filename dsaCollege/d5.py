#list declaration and accesing elements
#list properties
#list method and functions(min,max,sum,count)
#list slicing 
#list comprehension

# 1,2,3,4,5,7,12,14,17,22,30,35,38,51,55,66,69,72,73,74,75

#1
a=[1,2,3,4,5]
sum=0
for x in a:
    sum+=x
print(sum)

#2
m=1
for x in a:
    m*=x
print(m)

#3
m=a[1]
for x in a:
    if m>x:
        m=x
print(m)
print(min(a))

#4
print(max(a))
m=a[1]
for x in a:
    if m<x:
        m=x
print(m)


#5
b=['abc', 'xyz', 'aba', '1221']
count=0
for x in b:
    if len(x)>2 and x==x[::-1]:
        count+=1
print(count)

#7
a=[1,2,3,4,4,3,3,2,1,2,4,6,7]
print(list(set(a)))

#30
freq={}
for item in a:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print(freq)

#another way
res=[]
for e in a:
    if e not in res:
        print(f"count of {e}= {a.count(e)}")
        res.append(e)
print(res)

#12
a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a.pop(5)
a.pop(4)
a.pop(0)
print(a)

#14
a=[1,2,3,4,5,6]
for i in a[:]:
    if i%2==0:
        a.remove(i)
print(a)

#17,
a=[2,3,5,6,4]
flag=True
for x in a:
    for i in range(2,int(x** 0.5)+1):
        if x%i!=0:
            flag=False
            break
print(flag)

#22,

print(a.index(5))

#35

l=['p','q']
n=int(input("enter a num: "))
res=[]
for x in l:
    for i in range(1,n+1):
        res.append(x+str(i))
print(res)

