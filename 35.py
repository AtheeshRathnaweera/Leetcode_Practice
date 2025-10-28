from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        indices = list(range(len(nums)))

        while len(indices) > 1:
            index = len(indices) // 2

            if nums[indices[index]] == target:
                indices = [indices[index]]
                continue

            if nums[indices[index]] > target:
                indices = indices[:index]
                continue

            if nums[indices[index]] < target:
                indices = indices[index:]

        if nums[indices[0]] == target:
            return indices[0]

        if nums[indices[0]] > target:
            return max(indices[0] - 1, 0)

        return indices[0] + 1


# print(Solution().searchInsert(nums=[1, 3, 5, 6], target=5))
# print("Expected: 2\n")

# print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
# print("Expected: 1\n")

# print(Solution().searchInsert(nums=[1, 3, 5, 6], target=4))
# print("Expected: 2\n")

# print(Solution().searchInsert(nums=[1, 3, 5, 6], target=0))
# print("Expected: 0\n")

# print(Solution().searchInsert(nums=[1, 3, 5, 6], target=7))
# print("Expected: 4\n")

# print(Solution().searchInsert(nums=[1], target=1))
# print("Expected: 0\n")

# print(Solution().searchInsert(nums=[1,3,5], target=5))
# print("Expected: 2\n")

print(Solution().searchInsert(nums=[1, 3, 5], target=4))
print("Expected: 2\n")

# print(Solution().searchInsert(nums=[0,1,2,3,5,6,7,8], target=4))
# print("Expected: 4\n")
