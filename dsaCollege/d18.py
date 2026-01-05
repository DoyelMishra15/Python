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

#242
'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        return s==t'''

'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            d1={}
            d2={}

            for i in s:
                if i in d1:
                    d1[i]+=1
                else:
                    d1[i]=1
        
            for i in t:
                if i in d2:
                    d2[i]+=1
                else:
                    d2[i]=1

            return d1==d2
        else:
            return False
'''

'''class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for c in ransomNote:
            if c in d1:
                d1[c]+=1
            else:
                d1[c]=1

        for c in magazine:
            if c in d2:
                d2[c]+=1
            else:
                d2[c]=1

        for c in d1.keys():
            if c not in d2 or d2[c] < d1[c]:
                return False
        return True'''