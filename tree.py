"""
Tree DataStructure
"""


class Node:
    """Represent a tree node"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

    def add_node(self, newNode):
        if newNode < self:
            if self.left is None:
                self.left = newNode
            else:
                self.left.add_node(newNode)
        elif newNode > self:
            if self.right is None:
                self.right = newNode
            else:
                self.right.add_node(newNode)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data})'


class Tree:
    """A tree links the nodes"""

    def __init__(self, root):
        self.root = root

    def add_a_node(self, node):
        self.root.add_node(node)


if __name__ == '__main__':
    n10 = Node(10)
    n8 = Node(8)
    n12 = Node(12)
    n6 = Node(6)
    n9 = Node(9)
    n14 = Node(14)
    tree = Tree(n10)
