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

    def DAS(self,d):#delete at start
        if not self.head:
            print("SLL is empty, deletion not possible")
        else:
            self.head=self.head.next

    def DAE(self):#delete at end
        if not self.head:
            print("SLL is empty, deletion not possible")
        elif head==tail:
            self.head=None
            self.tail=None
        else:
            t = self.head
            while t.next != t.tail:
                t = t.next
            t.next = None
            self.tail = t
        
