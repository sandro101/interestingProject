from AnInterestingProject.jcollection.node import Node


class Stack: # LIFO
    head = None

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
        # just take the top node off and then set the current
        # set the data = data from next node
        # set the next_node = the third node
        # this makes first node into the second node and removes the first
        to_pop = self.head.data
        if self.head.next_node is not None:
            self.head.data = self.head.next_node.data
            self.head.next_node = self.head.next_node.next_node
        else:
            self.head = None
        return to_pop
