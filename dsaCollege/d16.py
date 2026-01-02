class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
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
    def IAE(self,d):
        nn=Node(d)
        if not self.head:
            self.head=nn
            self.tail=nn
        else:
            self.tail.next=nn
            self.tail=nn
    def display(self):
        t=self.head
        while t:
            print(t.data,end="->")
            t=t.next
        print()
        
