from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0

        for item in nums:
            if unique_count == 0:
                unique_count += 1
                continue

            if item > nums[unique_count - 1]:
                nums[unique_count] = item
                unique_count += 1

        return unique_count

print(Solution().removeDuplicates(nums=[0]))
print("Expected: 1, nums = []\n")

print(Solution().removeDuplicates(nums=[]))
print("Expected: 0, nums = [0]\n")

print(Solution().removeDuplicates(nums=[1, 2]))
print("Expected: 2, nums = [1,2]\n")

print(Solution().removeDuplicates(nums=[-3, -3, -2]))
print("Expected: 2, nums = [-3,-2]\n")

print(Solution().removeDuplicates(nums=[1, 1, 2]))
print("Expected: 2, nums = [1,2,_]\n")

print(Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print("Expected: 5, nums = [0,1,2,3,4,_,_,_,_,_]\n")
