# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluate_node(node: TreeNode):
            if node.val == 2:
                return evaluate_node(node.left) or evaluate_node(node.right)

            if node.val == 3:
                return evaluate_node(node.left) and evaluate_node(node.right)

            return node.val

        return evaluate_node(root)


print(f"{Solution().evaluateTree(root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, TreeNode(0, None, None), TreeNode(1, None, None))))}\nExpected: {1}")
