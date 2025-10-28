from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for index, item in enumerate(nums):
            if item != val:
                nums[index] = nums[count]
                nums[count] = item
                count += 1

        print(nums)
        return count

print(Solution().removeElement(nums=[3, 2, 2, 3], val=3))
print("Expected: 2, nums = [2,2]\n")

print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
print("Expected: 5, nums = [0,1,4,0,3,_,_,_]\n")
