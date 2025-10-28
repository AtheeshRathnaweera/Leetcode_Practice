from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        considered_negatives = set()
        largest_positive = -1

        nums.sort()

        for item in nums:
            if item < 0:
                considered_negatives.add(item)
                continue

            if item * -1 in considered_negatives:
                largest_positive = max(item, largest_positive)

        return largest_positive


print(Solution().findMaxK(nums=[-1, 2, -3, 3]))
print("Expected: 3\n")

print(Solution().findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
print("Expected: 7\n")

print(Solution().findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
print("Expected: -1\n")
