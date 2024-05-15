#Stacks Using Array
#The principle is last in first out
#push(): Insert the element in the stack.
#pop(): Remove and return the topmost element of the stack.
#peek()/top(): Returns the top element without removing it
#IsEmpty(): checks if the stack is empty
#IsFull(): check is the stack is full
#size(): Return the number of remaining elements in the stack.
# TC: O(n) and SC: O(n)

#Function to create a stack.
# It initializes size of stack as 0
def createStack():
    stack = []
    return stack
#Stack is empty when stack size is 0
def isEmpty(stack):
    return len(stack) == 0

# Function to add an item to stack.
# It increases size by 1
def push(stack, item):
    stack.append(item)
    print(str(item) + " pushed to stack ")

# Function to remove an item from stack.
# It decreases size by 1
def pop(stack):
    if (isEmpty(stack)):
        return -1 # return minus infinite
    return stack.pop()

# Function to return the top from stack without removing it
def peek(stack):
    if (isEmpty(stack)):
        return -1 # return minus infinite
    return stack[len(stack) - 1]

# test above functions
stack = createStack()
push(stack, 10)
push(stack, 20)
push(stack, 30)
print(stack)
print(isEmpty(stack))
print(str(peek(stack)) + " is the Top element")
print(str(pop(stack)) + " popped from stack")
print(stack)
print(str(pop(stack)) + " popped from stack")
print(stack)
print(str(pop(stack)) + " popped from stack")
print(stack)
print(isEmpty(stack))
print(str(pop(stack)) + " popped from stack")
print(stack)



