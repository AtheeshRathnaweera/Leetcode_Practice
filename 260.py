from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        print(nums)

        non_dup_nums = []

        for num in nums:
            if num in non_dup_nums:
                non_dup_nums.remove(num)
            else:
                non_dup_nums.append(num)

        return non_dup_nums


print(f"{Solution().singleNumber(nums = [1,2,1,3,2,5])}\nExpected: [3,5]")

print(f"{Solution().singleNumber(nums = [-1,0])}\nExpected: [-1,0]")

print(f"{Solution().singleNumber(nums = [0,1])}\nExpected: [1,0]")
