class Node:
    data = None
    next_node = None

    def __init__(self, data, min=data, position=None):
        self.data = data
        self.min_value = min
        if(position is not None):
            self.position = position
