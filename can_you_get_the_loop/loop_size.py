class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def loop_size(node):
    fast = node
    slow = node
    i = 0
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        i += 1
        if slow == fast:
            break
    slow = slow.next
    i = 1
    while slow != fast:
        slow = slow.next
        i += 1
    return i
