class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def swap_pairs(head):
    zero_node = Node(0)
    zero_node.next = head
    prev = zero_node

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
    return zero_node.next
