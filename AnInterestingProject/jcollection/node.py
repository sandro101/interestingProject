class Node:
    data = None
    next_node = None

    def __init__(self, data, min=data, position=None):
        self.data = data
        self.min_value = min
        if(position is not None):
            self.position = position

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False