from typing import List


# Time limit exceeded - O(n^2)
# class Solution:
#     def minIncrementForUnique(self, nums: List[int]) -> int:
#         # print(f"unique: {nums}")
#         # sorted_nums = sorted(nums)
#         unique_nums = set()
#         result = 0

#         for index, num in enumerate(nums):
#             # print(f"\nstarted {index} num: {num} unique nums: {unique_nums}")
#             if index == 0:
#                 unique_nums.add(num)
#                 continue

#             while nums[index] in unique_nums:
#                 nums[index] += 1
#                 result += 1
#                 # print(f"incremented: new value: {nums[index]}")
#             unique_nums.add(nums[index])

#         # print(f"unique: {unique_nums}")

#         return result

# Time complexity - O(nlogn)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # sort the nums
        sorted_nums = sorted(nums)
        last_unique = None
        result = 0

        # make the nums unique
        for item in sorted_nums:
            if last_unique is None:
                last_unique = item
                continue

            if last_unique >= item:
                last_unique += 1
                result += last_unique - item
                continue

            last_unique = item

        return result


print(f"{Solution().minIncrementForUnique(nums =[1,2,2])}\nExpected: 1")
print(f"{Solution().minIncrementForUnique(nums =[3,2,1,2,1,7])}\nExpected: 6")
