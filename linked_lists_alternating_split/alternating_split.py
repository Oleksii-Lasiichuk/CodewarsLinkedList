class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    a_head = head
    b_head = head.next
    a_current = a_head
    b_current = b_head

    while a_current and b_current:
        if b_current.next:
            a_current.next = b_current.next
            a_current = a_current.next
        else:
            a_current.next = None
            break

        if a_current.next:
            b_current.next = a_current.next
            b_current = b_current.next
        else:
            b_current.next = None
            break

    return Context(a_head, b_head)
