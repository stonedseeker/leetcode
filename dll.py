import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current


    def display(self):
        if not self.head:
            return None
        else:
            current = self.head
            while current:
                print(current.val)
                current = current.next
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

curr = dll.head

while curr:
    print(curr.val)
    curr = curr.next

curr = 

