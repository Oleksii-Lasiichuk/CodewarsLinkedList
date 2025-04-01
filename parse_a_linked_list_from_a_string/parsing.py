def linked_list_from_string(s):
    all_nodes_data = s.split(' -> ')
    lst = [Node(all_nodes_data[0])]
    for i, note in enumerate(all_nodes_data):
        if i == 0:
            continue
        if i == len(all_nodes_data) - 1:
            return lst[0]
        new_node = Node(note)
        lst[-1].next = new_node
        lst.append(new_node)
        
        
    return lst[0]