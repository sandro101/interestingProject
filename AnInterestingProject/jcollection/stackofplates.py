from AnInterestingProject.jcollection.node import Node


class StackOfPlates:  # LIFO
    stacks = [None]
    __stack_capacity = 2

    def __init__(self, data=None):
        if data is not None:
            self.stacks = [Node(data, position=self.__stack_capacity)]

    def push(self, data):
        if not self.stacks:
            self.stacks = [Node(data, position=self.__stack_capacity)]
        else:
            head = self.stacks[0]
            if head.position > 1:
                new_head = Node(data, position=head.position - 1)
                new_head.next_node = head
                self.stacks[0] = new_head
            else:
                new_head = Node(data, position=self.__stack_capacity)
                self.stacks.insert(0, new_head)

    def pop(self):
        if not self.stacks:
            raise ValueError("Nothing in the stack")
        head = self.stacks[0]
        to_pop = head.data
        if (head.position < self.__stack_capacity) & (head.next_node is not None):
            head.data = head.next_node.data
            head.next_node = head.next_node.next_node
            self.stacks[0] = head
        else:
            self.stacks = self.stacks[1:]
        return to_pop
