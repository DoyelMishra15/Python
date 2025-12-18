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