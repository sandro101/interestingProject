class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data
        self.discovered = False

    def __add__(self, other):
        self.children.append(other)
        other.parent = self
        return self


def build_some_tree():
    root = TreeNode('root')
    one = TreeNode('1')
    two = TreeNode('2')
    three = TreeNode('3')
    four = TreeNode('4')
    five = TreeNode('5')
    six = TreeNode('6')
    seven = TreeNode('7')
    root + (one + (four + seven))
    root + (two + five)
    root + (three + six)
    return root

