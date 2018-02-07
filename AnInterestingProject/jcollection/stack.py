from AnInterestingProject.jcollection.node import Node


class Stack: # LIFO

    def __init__(self, data=None):
        if data is not None:
            self.head = Node(data)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next_node = self.head
            self.head = new_head

    def pop(self):
        if self.head is None:
            raise ValueError("Nothing in the stack")
        to_pop = self.head.data
        if self.head.next_node is not None:
            self.head.data = self.head.next_node.data
            self.head.next_node = self.head.next_node.next_node
        else:
            self.head = None
        return to_pop
