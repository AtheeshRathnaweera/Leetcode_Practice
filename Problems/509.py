# without memoization
class Solution:
    def fib(self, n: int) -> int:
        last_vals = [0, 1]
        value = 0

        if n < 2:
            return last_vals[n]

        for _ in range(1, n):
            value = sum(last_vals)

            last_vals.pop(0)
            last_vals.append(value)

        return value


# with caching
# from functools import lru_cache

# class Solution:
#     def fib(self, n: int) -> int:
#         first_2_vals = [0, 1]

#         @lru_cache(maxsize=None)
#         def find_n_th(n):
#             if n < 2:
#                 return first_2_vals[n]

#             return find_n_th(n - 1) + find_n_th(n - 2)

#         return find_n_th(n)

print(Solution().fib(n=1))
print("Expected: 1\n")

print(Solution().fib(n=2))
print("Expected: 1\n")

print(Solution().fib(n=3))
print("Expected: 2\n")

print(Solution().fib(n=4))
print("Expected: 3\n")
