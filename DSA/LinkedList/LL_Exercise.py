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

    def remove_at(self, index):  # 0(n)
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            # it updates the head pointer to point to the next node in the list,
            # effectively removing the first node.
            self.head = self.head.next
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def insert_at(self,index,data): #0(n)
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index -1:
                    node = Node(data,itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def insert_after_value(self,data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return
        else:
            itr = self.head
            while itr:
                if itr.data == data_after:
                    itr.next = Node(data_to_insert,itr.next)
                    break
                itr = itr.next

    def remove_by_values(self,data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            itr = self.head
            while itr.next:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next



ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple")
ll.print()
ll.remove_by_values("orange")
ll.print()
ll.remove_by_values("figs")
ll.print()
ll.remove_by_values("banana")
ll.remove_by_values("mango")
ll.remove_by_values("apple")
ll.remove_by_values("grapes")
ll.print()



