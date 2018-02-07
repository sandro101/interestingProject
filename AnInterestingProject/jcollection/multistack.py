from AnInterestingProject.jcollection.node import Node


class MultiStack:  # LIFO
    stacks = [None, None, None]
    def __init__(self, data=None, stack_no=None):
        if (data is not None) & (stack_no is not None):
            self.stacks[stack_no] = Node(data)

    def push_at(self, data, stack_no):
        if self.stacks[stack_no] is None:
            self.stacks[stack_no] = Node(data)
        else:
            new_head = Node(data)
            new_head.next_node = self.stacks[stack_no]
            self.stacks[stack_no] = new_head

    def pop_at(self, stack_no):
        if self.stacks[stack_no] is None:
            raise ValueError("Nothing in the stack")
        to_pop = self.stacks[stack_no].data
        if self.stacks[stack_no].next_node is not None:
            self.stacks[stack_no].data = self.stacks[stack_no].next_node.data
            self.stacks[stack_no].next_node = self.stacks[stack_no].next_node.next_node
        else:
            self.stacks[stack_no] = None
        return to_pop