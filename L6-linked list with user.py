#121910313025
#create a linked list with user inputs
#Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        if self.tail is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
#display
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
list1=LinkedList()
n=int(input("How many elements would you like to read"))
for i in range(n):
    data=int(input("enter data item:"))
    list1.append(data)
print("The linked list:",end=' ')
list1.display()
        
