class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        # newNode = Node(arr[i])
        # current.next = newNode
        # newNode.prev = current
        # current = newNode

        current.next = ListNode(arr[i])
        current.next.prev = current
        current = current.next
    return head

def addNode(head, p, data):
    newNode = ListNode(data)
    current = head
    count = 0
    while current is not None and count < p:
        current = current.next
        count += 1

    if current is None:
        return head
    newNode.next = current.next
    if current.next is not None:
        current.next.prev = newNode
    current.next = newNode
    newNode.prev = current

    return head


# Example usage:
arr = [1, 2, 3, 4, 5]
head = construct_linked_list(arr)

# You can then traverse the linked list to see its elements
current = head
while current:
    print(current.val)
    current = current.next