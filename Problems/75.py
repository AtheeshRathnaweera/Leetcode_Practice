from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current_color, start, end = -1, 0, -1

        while start < len(nums) and current_color < 3:
            current_color += 1
            end = start

            while end < len(nums):
                if nums[end] == current_color:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                end += 1

print(f"{Solution().sortColors(nums =[2,0,2,1,1,0])}\nExpected: [0,0,1,1,2,2]")
print(f"{Solution().sortColors(nums =[0, 1])}\nExpected: [0,1]")
print(f"{Solution().sortColors(nums =[0, 0, 1])}\nExpected: [0, 0, 1]")
