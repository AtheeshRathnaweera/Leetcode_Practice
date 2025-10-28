from typing import List

# Bit Manipulation - O(2^n*n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for nums_pattern in range(2 ** len(nums)):
            subset = []
            for index, num in enumerate(nums):
                if nums_pattern & (1 << index):
                    subset.append(num)
            result.append(subset)

        return result


# Recursion - O(2^n)
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         subsets = [[]]

#         def get_all_subsets(indices: List[int]):
#             local_subsets = []
#             last_index = indices[-1] if len(indices) > 0 else -1

#             for next_index in range(last_index + 1, len(nums)):
#                 new_indices = indices + [next_index]
#                 local_subsets.append([nums[i] for i in new_indices])
#                 rec_subset = get_all_subsets(new_indices)
#                 local_subsets.extend(rec_subset)

#             return local_subsets

#         subsets.extend(get_all_subsets([]))
#         return subsets


print(
    f"{Solution().subsets(nums = [1,2,3])}\nExpected: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]"
)
