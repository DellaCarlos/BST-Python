from binary_search_tree import BinarySearchTree
from plot_tree import plot_tree

bst = BinarySearchTree()
values = [40, 20, 23, 44, 32, 60, 10, 30, 50, 70, 5, 15, 1, 13, 43, 25, 35]

for v in values:
    bst.add(bst.root, v)

print("preorder: ")
bst.preorder(bst.root)

print("inorder: ")
bst.inorder(bst.root)

print("postorder: ")
bst.postorder(bst.root)

plot_tree(bst.root)
