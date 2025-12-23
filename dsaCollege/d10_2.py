class Node:
    #def __init__(self,data,next): if passing next node
    def __init__(self,data):
        self.data = data
        #self.next = next
        #next ki jagah None
        self.next = None
    
    def display(self):
        t = n1
        while t:
            print(t.data)
            t = t.next

n1 = Node(10)
#n1=Node(10,None)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

print(n1.next)
n1.next=n2
print(n1.next)
n2.next=n3
n3.next=n4
n4.next=n5

# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)
# print(n1.next.next.next.data)
# print(n1.next.next.next.next.data)

n1.display()