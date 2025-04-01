class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    all_nodes_data = s.split(' -> ')
    if len(all_nodes_data) == 1:
        return None
    head = Node(int(all_nodes_data[0]))
    current = head
    for data in all_nodes_data[1:-1]:  # Skip the first (already processed) and last ("None")
        current.next = Node(int(data))
        current = current.next
    return head
