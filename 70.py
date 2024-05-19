import math


class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = 1

        # get the number of 2s in n
        num_of_twos = math.floor(n / 2)

        for loop in range(1, num_of_twos + 1):
            num_of_ones = n - (2 * loop)

            ways = math.factorial(loop + num_of_ones) / (
                math.factorial(loop) * math.factorial(num_of_ones)
            )

            total_ways += int(ways)

        return total_ways

print(f"n=2 result: {Solution().climbStairs(n=2)} Expected: 2\n")
print(f"n=3 result: {Solution().climbStairs(n=3)} Expected: 3\n")
print(f"n=4 result: {Solution().climbStairs(n=4)} Expected: 5\n")
print(f"n=5 result: {Solution().climbStairs(n=5)} Expected: 8\n")
print(f"n=6 result: {Solution().climbStairs(n=6)} Expected: 13\n")
print(f"n=8 result: {Solution().climbStairs(n=8)} Expected: 34\n")
print(f"n=9 result: {Solution().climbStairs(n=9)} Expected: 55\n")
