#To create a linked list with sample inputs
#Node class
class Node:
    #Function to initialise the node object
    def __init__(self,data):
        self.data=data
        self.next=None
#Linked List class contains a Node object
class LinkedList:
    #function to initialize head
    def __init__(self):
        self.head=None

    #print contents of linked list
    def printList(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
#Code execution starts here

#starts with empty list
list1=LinkedList()
list1.head=Node(10)
second=Node(20)
third=Node(30)

list1.head.next=second;
second.next=third;

list1.printList()
