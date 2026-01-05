class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def IAS(self,d):
        nn=Node(d)
        if not self.head:
            self.head=nn
            self.tail=nn
        else:
            nn.next=self.head
            self.head=nn
            self.head=nn
    
    def IAE(self,d):
        nn=Node(d)
        if not self.head:
            self.head=nn
            self.tail=nn
        else:
            t=self
            t.tail.next=nn
            nn.prev=t
            t.tail=nn
    
    def DAE(self):
        t=self
        if t:
            ...
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def display(self):
        t=self.head
        while t:
            print(t.data,end="->")
            t=t.next
        print()

#1472