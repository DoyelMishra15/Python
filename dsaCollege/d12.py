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

    def DAS(self):#delete at start
        if not self.head:
            print("SLL is empty, deletion not possible")
        else:
            self.head=self.head.next

    def DAE(self):#delete at end
        if not self.head:
            print("SLL is empty, deletion not possible")
        elif self.head == self.tail:
            self.head=None
            self.tail=None
        else:
            t = self.head
            while t.next != t.tail:
                t = t.next
            t.next = None
            self.tail = t
    def InsertAtPosition(self, data, position):
        if position == 0:
            self.InsertAtStart(data)
            return
        new_node = Node(data)
        t = self.head
        count = 0
        while t and count < position - 1:
            t = t.next
            count += 1
        if not t:
            print("Position out of bounds")
            return
        new_node.next = t.next
        t.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def DeleteAtPosition(self, position):
        if position == 0:
            self.DeleteAtStart()
            return
        t = self.head
        count = 0
        while t and count < position - 1:
            t = t.next
            count += 1
        if not t or not t.next:
            print("Position out of bounds")
            return
        t.next = t.next.next
        if t.next is None:
            self.tail = t

s1 = SLL()
while True:
    op = int(input("1.InsertAtStart 2.InsertAtEnd 3.Display 4.DeleteAtStart 5.DeleteAtEnd 6.InsertAtPosition 7.DeleteAtPosition 8.Exit: "))
    if op == 1:
        d = int(input("Enter data to insert at start: "))
        s1.InsertAtStart(d)
    elif op == 2:
        d = int(input("Enter data to insert at end: "))
        s1.InsertAtEnd(d)
    elif op == 3:
        s1.display()
    elif op == 4:
        s1.DeleteAtStart()
    elif op == 5:
        s1.DeleteAtEnd()
    elif op == 6:
        d = int(input("Enter data to insert at position: "))
        p = int(input("Enter position: "))
        s1.InsertAtPosition(d, p)
    elif op == 7:
        p = int(input("Enter position to delete: "))
        s1.DeleteAtPosition(p)
    elif op == 8:
        break
    else:
        print("Invalid input")