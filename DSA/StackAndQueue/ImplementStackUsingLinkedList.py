#Stack implementation using a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #Pointer to the next node in the linked list

class Stack:
    def __init__(self):
        self.head = None #Initialize an empty stack with no nodes

    def isEmpty(self):
        return self.head is None #Check if the stack is empty

    def push(self,data):
        newNode = Node(data) #Create a new node with the given data
        if self.isEmpty() is None:
            self.head = newNode #If the stack is empty, set the new node as the head
        else:
            newNode.next = self.head #Point the new node's next to the current head
            self.head = newNode #Update the head to the new node

    def pop(self):
        if self.isEmpty():
            return None #If the stack is empty, return None
        else:
            popped = self.head.data #Store the data of the node to be popped
            self.head = self.head.next #Move the head pointer to the next node
            return popped #Return the popped data

    def peek(self):
        if self.isEmpty():
            return None #If the stack is empty, return None
        else:
            return self.head.data #Return the data of the top node

    def display(self):
        current = self.head #Start from the head of the stack
        while current is not None:
            print(current.data, end="->") #Print the data of the current node
            current = current.next #Move to the next node
        print(None) #Print a newline to separate from other outputs

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print("Top Element on the stack: ", stack.peek())
print("Remove the Element on the stack:", stack.pop())
print("Remove the Element on the stack:", stack.pop())
stack.display()




