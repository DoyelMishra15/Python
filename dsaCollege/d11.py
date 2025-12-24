#CRUD or CURD Operations.....
#create, read, update, delete


#inserting at start
#  nn=Node(data)
        # if head is None:
        #     head=nn
        #     tail=nn
        #   else:
        #       nn.next=head
        #   head=nn


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def IAS(self,d):#insert at start
        nn=Node(d)
        if not self.head:
            self.head=nn
            self.tail=nn
        else:
            nn.next=self.head
            self.head=nn

    def IAE(self,d):#insert at end
        nn=Node(d)
        if not self.head:
            self.head=nn
            self.tail=nn
        else:
            self.tail.next=nn
            self.tail=nn

    def IAM(self):#insert at middle
        pass

    def display(self):
        t=self.head
        while t:
            print(t.data, end="->")
            t=t.next
        print()

s1= SLL()
s1.IAS(10)
s1.IAS(20)
s1.IAS(30)
s1.IAS(40)

s1.display()