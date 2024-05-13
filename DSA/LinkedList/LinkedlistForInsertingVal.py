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

class LinkedList: #Represents the linked list itself

    def __init__(self):
        #head attribute pointing to the first node of the list.
        self.head = None

    def insert_at_begining(self,data): #o(1)
        #Inserts a new node with the given data at the beginning of the list.
        node = Node(data, self.head)
        self.head = node

    def print(self): #Prints the elements of the linked list.
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

    def insert_at_end(self,data): #o(n)
        #Inserts a new node with the given data at the end of the list.
        if self.head is None:
            self.head =Node(data,None) #here None refers to null
            return
        else:
            itr = self.head
            while itr.next: #it runs untils the last value is null
                itr = itr.next
            itr.next =Node(data,None)

    def insert_values(self,data_list): #o(n)
        #Initializes the linked list with values from a list.
        self.head = None
        for data in data_list:
            #self.insert_at_end(data)
            self.insert_at_begining(data)

    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count += 1
            itr=itr.next
        print("length",count)
        return count


ll = LinkedList() #creating a llist
ll.insert_values(["kiwi","berries","oranges","apple"])
ll.get_length()
ll.print()
#print("length:",ll.get_length())

