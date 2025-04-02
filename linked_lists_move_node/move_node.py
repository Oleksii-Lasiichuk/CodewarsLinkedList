
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError("Source list cannot be empty")
    new_head = source
    source = source.next
    new_head.next = dest

    return Context(source, new_head)
