# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def makeNodeValid(node: TreeNode):
            if node is None:
                return 0, 0

            left_moves, left_diff = makeNodeValid(node.left)
            right_moves, right_diff = makeNodeValid(node.right)

            # value which should add or subtract to the parent node
            total_diff = node.val + (left_diff + right_diff) - 1
            total_moves = (left_moves + right_moves) + abs(total_diff)

            return total_moves, total_diff

        return makeNodeValid(root)[0]

# print(
#     f"{Solution().distributeCoins(root=TreeNode(3, TreeNode(0, None, None), TreeNode(0, None, None)))}\nExpected: {2}"
# )
# print(
#     f"{Solution().distributeCoins(root=TreeNode(0, TreeNode(3, None, None), TreeNode(0, None, None)))}\nExpected: {3}"
# )
print(
    f"{Solution().distributeCoins(root=TreeNode(4, TreeNode(0, None, TreeNode(0, None, TreeNode(0, None, None))), None))}\nExpected: {6}"
)
