# without memoization
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         value = 0
#         last_vals = [0, 1, 1]

#         if n < 3:
#             return last_vals[n]

#         for _ in range(3, n+1):
#             value = sum(last_vals)
#             last_vals.pop(0)
#             last_vals.append(value)

#         return value

# with caching
from functools import lru_cache

class Solution:
    def tribonacci(self, n: int) -> int:
        first_3_vals = [0, 1, 1]

        @lru_cache(maxsize=None)
        def find_n_th(n):
            if n < 3:
                return first_3_vals[n]

            return find_n_th(n - 3) + find_n_th(n - 2) + find_n_th(n - 1)

        return find_n_th(n)


print(
    Solution().tribonacci(n=1)
)
print("Expected: 1\n")

print(Solution().tribonacci(n=2))
print("Expected: 1\n")

print(Solution().tribonacci(n=3))
print("Expected: 2\n")

print(
    Solution().tribonacci(n=4)
)
print("Expected: 4\n")

print(Solution().tribonacci(n=5))
print("Expected: 7\n")

print(Solution().tribonacci(n=25))
print("Expected: 1389537\n")
