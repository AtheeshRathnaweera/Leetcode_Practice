from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def get_mins_for_each_row(row_index, prev_row_vals: List[int]):
            row = None
            prev_row = prev_row_vals
            new_row_vals = []

            if row_index == len(grid):
                return prev_row_vals

            row = grid[row_index]

            # print(f"\n{row_index} prev: {prev_row}")

            for index, item in enumerate(row):
                new_prev_vals = prev_row[:index] + prev_row[index + 1:]
                # print(f"\n{row_index} column: {index} new prev: {new_prev_vals}")
                min_val = min(new_prev_vals)

                new_row_vals.append(item + min_val)

            if row_index + 1 == len(grid):
                return new_row_vals

            result = get_mins_for_each_row(row_index + 1, new_row_vals)
            # print(result)

            return result

        final_result = get_mins_for_each_row(1, grid[0])
        # print(f"final: {final_result}")

        return min(final_result)


print(f"grid: {[[1,2,3],[4,5,6],[7,8,9]]}")
print(
    f"result: {Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]])} Expected: 13\n"
)

print(f"grid: {[[1,2,1],[4,5,6],[7,8,9]]}")
print(
    f"result: {Solution().minFallingPathSum(grid = [[1,2,1],[4,5,6],[7,8,9]])} Expected: 13\n"
)

print(f"grid: {[[7]]}")
print(
    f"result: {Solution().minFallingPathSum(grid = [[7]])} Expected: 7\n"
)

print({Solution().minFallingPathSum(grid = [
    [-37, 51, -36, 34, -22],
    [82, 4, 30, 14, 38],
    [-68, -52, -92, 65, -85],
    [-49, -3, -77, 8, -19],
    [-60, -71, -21, -62, -73],
])})
print("Expected: -268\n")

print(
    {
        Solution().minFallingPathSum(
            grid=[
                [-2, -18, 31, -10, -71, 82, 47, 56, -14, 42],
                [-95, 3, 65, -7, 64, 75, -51, 97, -66, -28],
                [36, 3, -62, 38, 15, 51, -58, -90, -23, -63],
                [58, -26, -42, -66, 21, 99, -94, -95, -90, 89],
                [83, -66, -42, -45, 43, 85, 51, -86, 65, -39],
                [56, 9, 9, 95, -56, -77, -2, 20, 78, 17],
                [78, -13, -55, 55, -7, 43, -98, -89, 38, 90],
                [32, 44, -47, 81, -1, -55, -5, 16, -81, 17],
                [-87, 82, 2, 86, -88, -58, -91, -79, 44, -9],
                [-96, -14, -52, -8, 12, 38, 84, 77, -51, 52],
            ]
        )
    }
)
print("Expected: -879\n")