#wpwr
def add(x,y):
    return x+y
s=add(5,10)
print(s)

#wpwor
def add(x,y):
    print(x+y)
add(5,10)

#wopwr
def add():
    x,y=6,7
    return x+y
s=add()
print(s)

#wopwor
def add():
    x,y=7,7
    print(x+y)
add()

#argument types in python

#1.Positional Arguments

#Passed by order. Python matches values to parameters based on their position.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet("Doyel", 21)

#2️⃣ Keyword Arguments: Passed using parameter names, order doesn’t matter.
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet(age=21, name="Doyel")
# Output: Hello Doyel, you are 21 years old
#28 leetcode
'''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)):
                if needle==haystack[i:len(needle)+i]:
                    return i'''


#2nd way
'''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1'''



#344
'''class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1'''

# s[i]="ho" 
#s[j]=s[i].replace(s[j]) "h"
#s[i]=s[i].replace(s[j])"o"

# nd 125

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for c in s:
            if not c.isalnum():
                s=s.replace(c,'')
        return s==s[::-1]
'''

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        for c in s:
            if not c.isalnum():
                s=s.replace(c,'')
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
'''

a=[1,2,3,4,5,6,7]
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        print(a[i],a[j])

a=[1,2,3,4,5,6,7]
t=9
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            print([i,j])

