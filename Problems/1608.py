from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def is_special(nums: List[int], x: int, valid_count: int):
            nums_for_next = []

            if x == 0:
                return -1

            for num in nums:
                if num >= x:
                    valid_count += 1
                else:
                    nums_for_next.append(num)

            if valid_count == x:
                return x

            return is_special(nums_for_next, x - 1, valid_count)

        return is_special(nums, len(nums), 0)


print(f"{Solution().specialArray(nums = [3,5])}\nExpected: 2")

print(f"{Solution().specialArray(nums = [0,0])}\nExpected: -1")

print(f"{Solution().specialArray(nums = [0,4,3,0,4])}\nExpected: 3")

print(f"{Solution().specialArray(nums = [3,6,7,7,0])}\nExpected: -1")
