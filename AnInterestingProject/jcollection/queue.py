from jcollection.node import Node


class Queue:  # FIFO
    head = None

    def __init__(self, data):
        self.head = Node(data)

    def push(self, data):
        head = self.head
        while self.head.next_node != None:
            self.head = self.head.next_node
        self.head.next_node = Node(data)
        self.head = head

    def pop(self):
        # just take the top node off and then set the current
        # set the data = data from next node
        # set the next_node = the third node
        # this makes first node into the second node and removes the first
        to_pop = self.head.data
        self.head.data = self.head.next_node.data
        self.head.next_node = self.head.next_node.next_node
        return to_pop
