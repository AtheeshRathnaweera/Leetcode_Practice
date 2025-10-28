# 66. Plus One
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for index in range(len(digits) - 1, -1, -1):
            new_val = digits[index] + carry
            carry = int(new_val >= 10)
            digits[index] = new_val % 10
        if carry > 0:
            return [carry] + digits
        return digits


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for index in range(len(digits) - 1, -1, -1):
#             new_val = digits[index] + 1
#             # No carry needed: digit + 1 < 10, so we can stop here
#             if new_val < 10:
#                 digits[index] = new_val
#                 return digits

#             # Carry needed: digit was 9, so it becomes 0 and we continue
#             # to propagate the carry to the next more significant digit
#             digits[index] = 0

#             # Special case: if we've reached the most significant digit (index 0)
#             # and still have a carry, we need to add a new digit at the front
#             if index == 0:
#                 return [1] + digits

#         return digits


print(Solution().plusOne([1, 2, 3]))
print()
print(Solution().plusOne([4, 3, 2, 2]))
print()
print(Solution().plusOne([9]))
