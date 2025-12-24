#CRUD or CURD Operations.....
#create, read, update, delete

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def display(self):
        t = n1 #n3
        while t:
           print(t.data, end="->")
           t = t.next
        print()

