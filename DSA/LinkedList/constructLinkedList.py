class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next

    return head


# Example usage:
arr = [1, 2, 3, 4, 5]
head = construct_linked_list(arr)

# You can then traverse the linked list to see its elements
current = head
while current:
    print(current.val)
    current = current.next