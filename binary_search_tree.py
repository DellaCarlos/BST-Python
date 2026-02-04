from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, current, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    current.left.parent = current
                else:
                    self.add(current.left, value)

            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    current.right.parent = current
                else:
                    self.add(current.right, value)
            else:
                print('Error: Value already exist.')

    def visit(self, node):
        print(node.value)

    def preorder(self, current):
        if current is None:
            return
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)

    def inorder(self, current):
        if current is None:
            return
        self.inorder(current.left)
        self.visit(current)
        self.inorder(current.right)

    def postorder(self, current):
        if current is None:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        self.visit(current)
