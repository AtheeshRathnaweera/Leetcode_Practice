# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest
# integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the
# nearest integer, 2 is returned.


# Brute Force
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         int_base = 1
#         while int_base * int_base <= x:
#             int_base = int_base + 1
#         return int_base - 1


# Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 1, max(x // 2, 1)
        while start <= end:
            mid = start + ((end - start) // 2)
            sqr_of_mid = mid * mid
            if sqr_of_mid == x:
                return mid
            if x < sqr_of_mid:
                end = mid - 1
            if x > sqr_of_mid:
                start = mid + 1
        return end


print("\n* Result of 136 ->", Solution().mySqrt(136))
print("\n* Result of 144 ->", Solution().mySqrt(144))
print("\n* Result of 8 ->", Solution().mySqrt(8))
print("\n* Result of 1 -> ", Solution().mySqrt(1))
print("\n* Result of 2 -> ", Solution().mySqrt(2))
print("\n* Result of 5 -> ", Solution().mySqrt(5))
print("\n* Result of 0 -> ", Solution().mySqrt(0))
