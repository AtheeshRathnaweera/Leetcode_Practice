from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        print(nums)

print(f"{Solution().beautifulSubsets(nums = [2,4,6], k = 2)}\nExpected: 4")

print(f"{Solution().beautifulSubsets(nums = [1], k = 1)}\nExpected: 1")
