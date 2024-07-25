from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        sorted_grid = []

        def get_sorted_row(row):
            sorted_vals = list(set(row))
            sorted_vals.sort()
            temp_result = [[] for _ in sorted_vals]
            result = []

            for index, item in enumerate(row):
                sorted_index = sorted_vals.index(item)
                temp_result[sorted_index].append((index, item))

            # flat the results
            for item_list in temp_result:
                result.extend(item_list)

            return result

        for row in grid:
            sorted_row = get_sorted_row(row)
            # print(sorted_row)
            sorted_grid.append(sorted_row)

        # print(sorted_grid)
        print()

        def update_path_with_lowest_in_next_row(next_row_index, current_cell):
            # print(f"\n{next_row_index} current cell: {current_cell}")

            next_row = sorted_grid[next_row_index]
            result = []
            # lowest_val = None

            # print(f"{next_row_index} next row: {next_row}")
            # print(f"{next_row_index} lowest_val: {lowest_val}")

            for item in next_row:
                # if lowest_val is not None and lowest_val < item[1]:
                #     # print(f"{next_row_index} break here")
                #     break

                if item[0] != current_cell[0] or current_cell[0] is None:
                    result.append([item])

                    if next_row_index + 1 == len(sorted_grid):
                        continue

                    next_results = update_path_with_lowest_in_next_row(next_row_index + 1, item)
                    # result.extend(next_results)

                    # print(f"{next_row_index} next_results: {next_results}")

                    # update the results
                    # temp_results = []
                    # for next_result in next_results:
                    #     temp_result = result[-1].copy()
                    #     temp_result.extend(next_result)
                    #     temp_results.append(temp_result)
                    # #     result_copy = result.copy()
                    # #     result_copy.append(next_result)

                    # #     temp_results.append(result_copy)
                    # result.pop()
                    # result.extend(temp_results)

                    # break

            return result

        possible_lowest_paths = update_path_with_lowest_in_next_row(0, (None, None))

        # print(possible_lowest_paths)
        return

        # find the lowest
        lowest_sum = None
        for poss_path in possible_lowest_paths:
            path_sum = 0
            for cell in poss_path:
                path_sum = path_sum + cell[1]

            if lowest_sum is None:
                lowest_sum = path_sum
                continue

            lowest_sum = min(lowest_sum, path_sum)

        return lowest_sum


# print(f"grid: {[[1,2,3],[4,5,6],[7,8,9]]}")
# print(
#     f"result: {Solution().minFallingPathSum(grid = [[1,2,3],[4,5,6],[7,8,9]])} Expected: 13\n"
# )

# print(f"grid: {[[1,2,1],[4,5,6],[7,8,9]]}")
# print(
#     f"result: {Solution().minFallingPathSum(grid = [[1,2,1],[4,5,6],[7,8,9]])} Expected: 13\n"
# )

# print(f"grid: {[[7]]}")
# print(
#     f"result: {Solution().minFallingPathSum(grid = [[7]])} Expected: 7\n"
# )

# print({Solution().minFallingPathSum(grid = [
#     [-37, 51, -36, 34, -22],
#     [82, 4, 30, 14, 38],
#     [-68, -52, -92, 65, -85],
#     [-49, -3, -77, 8, -19],
#     [-60, -71, -21, -62, -73],
# ])})
# print("Expected: -268\n")

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
print("Expected: -268\n")
