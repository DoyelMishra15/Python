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

    def display(self):
        t=self.head
        while t:
            if t.next != None:
                print(t.data, end="->")
            else:
                print(t.data)
            t=t.next
        print()
