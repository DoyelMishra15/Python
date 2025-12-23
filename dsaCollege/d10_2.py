# class Node:
#     #def __init__(self,data,next): if passing next node
    
#     def __init__(self,data):
#         self.data = data
#         #self.next = next
#         #next ki jagah None
#         self.next = None
    
#     def display(self):
#         t = n1 #n3
#         while t:
#             print(t.data, end="->")
#             t = t.next
#         print()
    

# n1 = Node(10)
# #n1=Node(10,None)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)

# #print(n1.next)

# n1.next=n2

# #print(n1.next)

# n2.next=n3
# n3.next=n4
# n4.next=n5

# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)
# print(n1.next.next.next.data)
# print(n1.next.next.next.next.data)

# n1.display()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def length(self):
        t=n1
        c=0
        while t:
            c+=1
            t=t.next
        print("Length:",c)
        
        
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

# 1. **Find Length of a Linked List**
n1.length()
# 2. **Find Sum of All Elements**
# 3. **Find Maximum Element**
# 4. **Find Minimum Element**
# 5. **Search an Element in Linked List**
# 6. **Count Occurrences of a Given Element**
# 7. **Find Average of Linked List Elements**
# 8. **Print Linked List in Reverse Order**
# 9. **Find Middle Element of Linked List**
# 10. **Check if Linked List is Empty**