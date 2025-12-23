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

    def display(self):
        t = n1 #n3
        while t:
           print(t.data, end="->")
           t = t.next
        print()
        
    def sum(self):
        t=n1
        s=0
        while t:
            s+=t.data
            t=t.next
        print(f"Sum: {s}")
    
    def maximum(self):
        t=n1
        m=t.data
        while t:
            if m<t.data:
                m=t.data
            t=t.next
        print(f"Maximum: {m}")

    def minimum(self):
        t=n1
        m=t.data
        while t:
            if m>t.data:
                m=t.data
            t=t.next
        print(f"Minimum: {m}")

    def search(self,e):
        t=n1
        while t:
            if t.data==e:
                print(f"Element {e} found")
            return
        t=t.next

    def occurences(self,e):
        t=n1
        c=0
        while t:
            if t.data==e:
                c+=1
            t=t.next
        print(f"Element {e} occurs {c} times")
    
    def avg(self):
        t=n1
        s=0
        k=0
        while t:
            s+=t.data
            k+=1
            t=t.next
        print(f"Average: {s/k}")

    def reverse(self):
        t = n1 #n3
        rev =[]
        while t:
           rev.append(t.data)
           t = t.next
        for i in range(len(rev)-1, -1, -1):
            if i != 0:
                print(rev[i], end="->")
            else:
                print(rev[i])

    def mid(self):
        t = n1
        t=n1
        c=0
        while t:
            c+=1
            t=t.next
        t = n1
        if c%2==0:
            for _ in range(c // 2 - 1):
                t = t.next
                print("Middle elements:", t.data, t.next.data)
        else:
            for _ in range(c // 2):
                t = t.next
            print("Middle element:", t.data)

    def empty(self):
        if n1==None:
            print("Linked List is empty")
        else:
            print("Linked List is not empty")
        
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
n1.sum()

# 3. **Find Maximum Element**
n1.maximum()

# 4. **Find Minimum Element**
n1.minimum()

# 5. **Search an Element in Linked List**
n1.search(30)

# 6. **Count Occurrences of a Given Element**
n1.occurences(20)

# 7. **Find Average of Linked List Elements**
n1.avg()

# 8. **Print Linked List in Reverse Order**
n1.reverse()

# 9. **Find Middle Element of Linked List**
n1.mid()

# 10. **Check if Linked List is Empty**
n1.empty()