def stringify(node):
    if node is None:
        return "None"
    else:
        return f"{node.data} -> {stringify(node.next)}"