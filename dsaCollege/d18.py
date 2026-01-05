d={}
print(type(d))
d1={
    "k1":1,
    "k2":2,
    "k3":3
}
print(d1)

'''n = int(input("Enter a number: "))

while True:
    rev = int(str(n)[::-1])
    n = n + rev
    print(n)

    if str(n) == str(n)[::-1]:
        break'''

d1['k4']=4433
print(d1)

d1 = {"a": 10, "b": 20, "c": 30}

for i in d1.keys():
    print(i,end=" ")

print()
for i in d1.values():
    print(i,end=" ")

print()
for i in d1.items():
    print(i,end=", ")