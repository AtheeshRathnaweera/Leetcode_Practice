# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # both the roots must be not null
        if root1 is not None and root2 is not None:
            if root1.val != root2.val:
                return False
            # compares the left subtree
            left_sub_equal = self.flipEquiv(root1.left, root2.left)
            # if the left subtree is equal check the right subtree as it is
            if left_sub_equal is True:
                right_sub_equal = self.flipEquiv(root1.right, root2.right)
            # if the left subtree is not equal flip the left subtree and right subtree
            else:
                left_sub_equal = self.flipEquiv(root1.right, root2.left)
                right_sub_equal = self.flipEquiv(root1.left, root2.right)

            # both the subtrees must be equal
            return left_sub_equal and right_sub_equal

        # if atleaset one root is null the comparison is False except for both Null roots
        return root1 is None and root2 is None


# Test Case 01
test_01_root_01 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6), None))
test_01_root_02 = TreeNode(1, TreeNode(3, None, TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(7))))
test_01_res = Solution().flipEquiv(test_01_root_01, test_01_root_02)
print(f"test 01: {test_01_res}")

# Test Case 02
test_02_root_01 = None
test_02_root_02 = None
test_02_res = Solution().flipEquiv(test_02_root_01, test_02_root_02)
print(f"test 02: {test_02_res}")

# Test Case 03
test_03_root_01 = None
test_03_root_02 = TreeNode(1, None, None)
test_03_res = Solution().flipEquiv(test_03_root_01, test_03_root_02)
print(f"test 03: {test_03_res}")
