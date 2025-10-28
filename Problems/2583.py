# Problem: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/?envType=daily-question&envId=2024-10-22

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        sums: List[int] = []
        # print(f"Starting sum: {Solution.sums}")
        self.calculate_level_sum(0, root, sums)
        # print(f"final results: {Solution.sums}")
        # sort the list in descending order
        sums.sort(reverse=True)
        # print(f"sorted sums: {Solution.sums}")
        return sums[k - 1] if 0 < k <= len(sums) else -1

    def calculate_level_sum(self, level: int, node: TreeNode | None, sums: List[int]):
        if node:
            if len(sums) <= level:
                sums.append(node.val)
            else:
                sums[level] += node.val

            # print(f"{level} -> {node.val}")
            # print(f"{level} -> {node.val} | sum: {Solution.sums[level]}")
            self.calculate_level_sum(level + 1, node.left, sums)
            self.calculate_level_sum(level + 1, node.right, sums)


print("RESULTS")
# Test case 01:
# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
test_case_01_res = Solution().kthLargestLevelSum(
    TreeNode(
        5,
        TreeNode(8, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(1)),
        TreeNode(9, TreeNode(3), TreeNode(7)),
    ),
    2,
)
print(f"- Test Case 01: {test_case_01_res}")

# Test case 02:
# Input: root = [1,2,null,3], k = 1
# Output: 3
test_case_02_res = Solution().kthLargestLevelSum(
    TreeNode(1, TreeNode(2, TreeNode(3), None), None),
    1,
)
print(f"- Test Case 02: {test_case_02_res}")
