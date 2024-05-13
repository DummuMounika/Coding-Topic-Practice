#linked list is of 3 types: Singular,Double and Circular
#Singular linked list goes with the head flow to tail flow in one direction
#Double linked list goes with both direction
#For both singular and double we have null pointer at last
#For circular linked list we don't have null pointer

#singly linked list
class Node: #represents individual element in the node class.
    def __init__(self,data=None,next=None):
        self.data = data #field to store the value
        self.next = next #field to store a reference to the next node in the list.

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data): #it'll take the data val and insert at begining
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LL is empty")
            return
        else:
            itr = self.head
            llstr= ''

            while itr:
                llstr += str(itr.data) + '--->'
                itr = itr.next

            print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head =Node(data,None) #here None refers to null
            return
        else:
            itr = self.head
            while itr.next: #it runs untils the last value is null
                itr = itr.next
            itr.next =Node(data,None)

ll = LinkedList() #creating a llist
ll.insert_at_begining(9) #insert values
ll.insert_at_begining(45)
ll.insert_at_end(78)
ll.insert_at_end(1)
ll.print()

