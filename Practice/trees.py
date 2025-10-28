# Implementation of different types of Trees
# https://www.geeksforgeeks.org/types-of-binary-tree/
# 1. Binary Tree
# 2. Full Binary Tree (Proper Binary Tree) - A full binary tree is a binary tree
# with either zero or two child nodes for each node.
# 3. Degenerate Binary Tree - Can be left aligned or right aligned or a mix of both.
# 4. Skewed Binary Tree - Where all nodes have only left children or right children.
# While all skewed binary trees are degenerate trees, not all degenerate trees are skewed
# 5. Binary Search Tree
# 6. AVL Trees
# 7. B-Trees
###################################################################################
# Binary Tree
# REPRESENTATION
class BTreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right

#       1
#     /   \
#    7     9
#   / \     \
#  2   6     9
#     / \   /
#    5  11 5

binary_tree = BTreeNode(
    1,
    BTreeNode(
        7,
        BTreeNode(2, None, None),
        BTreeNode(6, BTreeNode(5, None, None), BTreeNode(11, None, None)),
    ),
    BTreeNode(9, None, BTreeNode(9, BTreeNode(5, None, None), None)),
)

# TRAVERSAL
# In-order Traversal
# left, root, right
def in_order_traversal(node:BTreeNode):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=" ")
        in_order_traversal(node.right)

in_order_traversal(binary_tree)
# Expected: [2, 7, 5, 6, 11, 1, 9, 5, 9]

print()

# Pre-order Traversal
# root, left, right
def pre_order_traversal(node:BTreeNode):
    if node:
        print(node.val, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

pre_order_traversal(binary_tree)
# Expected: [1, 7, 2, 6, 5, 11, 9, 9, 5]

print()

# Post-order Traversal
# left, right, root
def post_order_traversal(node:BTreeNode):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.val, end=" ")

post_order_traversal(binary_tree)
# Expected: [2, 5, 11, 6, 7, 5, 9, 9, 1]

###################################################################################
# Full Binary Tree


###################################################################################
# Binary Search Tree

###################################################################################
# AVL Tree

###################################################################################
# B - Trees
