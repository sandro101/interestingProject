from AnInterestingProject.jcollection.node import Node


class Stack:  # LIFO

    def __init__(self, data=None):
        self.head = None
        if data is not None:
            self.head = Node(data)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

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

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def hasNext(self):
        return self.head is not None
