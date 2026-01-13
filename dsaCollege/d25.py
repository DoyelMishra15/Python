#stack- append, pop
#and in queue- appned, pop(0)

#155

'''class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()'''

'''class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        stack=[c for c in s if c.isalpha()]
        s=[stack.pop() if c.isalpha() else c for c in s]
        return ''.join(s)'''