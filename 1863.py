from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def func(indices_to_remove: List[int]):
            total_sum = 0

            # remove indices and get XOR
            for index, num in enumerate(nums):
                if index not in indices_to_remove:
                    total_sum = total_sum ^ num

            for index in range(indices_to_remove[-1] + 1, len(nums)):
                indices_to_remove_new = indices_to_remove.copy()
                indices_to_remove_new.append(index)
                total_sum += func(indices_to_remove_new)

            return total_sum

        return func([-1])

# bit masking approach
# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         total_sum = 0
#         # Iterate through all possible subsets
#         for i in range(1 << n):
#             print(f"\ni -> {i} {bin(i)}")
#             subset_xor = 0
#             for j in range(n):
#                 print(f"j -> {j} {bin(1 << j)}")
#                 # Check if the j-th element is in the i-th subset
#                 if i & (1 << j):
#                     print("matched")
#                     subset_xor ^= nums[j]
#             total_sum += subset_xor
#         return total_sum


print(f"{Solution().subsetXORSum(nums = [5,1,6])}\nExpected: 28")

print(f"{Solution().subsetXORSum(nums = [1,3])}\nExpected: 6")
