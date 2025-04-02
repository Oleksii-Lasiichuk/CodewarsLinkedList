
class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node is None:
        raise ValueError("Invalid node")
    if 0 == index:
        return node
    return get_nth(node.next, index-1)
