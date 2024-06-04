class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class cdll:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            current = self.head.prev
            current.next = new_node
            new_node.prev = current
            self.head_prev = new_node



