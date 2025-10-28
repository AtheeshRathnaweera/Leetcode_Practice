from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        print(matrix)

        dimensions = self.get_dimensions(matrix)
        print(dimensions)

        adjacent_row_indices = self.get_pairs_in_rows(matrix, dimensions)
        print("\nrows and cells: ")
        for item in adjacent_row_indices:
            print(item)

        cells_with_1 = self.get_cells_with_1(adjacent_row_indices)

        # adjacent_col_indices = self.get_pairs_in_cols(matrix, dimensions)
        # for item in adjacent_col_indices:
        #     print(item)
        cells_with_1_in_same_col_counts = self.find_adjacent_cells_in_rows(
            adjacent_row_indices, dimensions, cells_with_1
        )
        print("\ncounts of each set: ")
        for item in cells_with_1_in_same_col_counts:
            print(item)

        result = self.get_highest_possible_total_for_each_set(cells_with_1_in_same_col_counts)
        print("\nmax total of each set: ")
        for item in result:
            print(item)

        print()

        if len(result) > 0:
            return max(result)
        else:
            return 0

    def get_dimensions(self, matrix: List[List[str]]) -> tuple[int, int]:
        return (len(matrix), len(matrix[0]))

    def get_pairs_in_rows(self, matrix: List[List[str]], dimensions: tuple[int, int]) -> List[List[tuple[int, int]]]:
        adjacent_row_indices = []

        # find the adjacent 1s in rows
        for row_index in range(0, dimensions[0]):
            row = matrix[row_index]
            # print(f"\nrow index: {row_index} -> {row}")

            last_column_val = None
            adjacent_pairs = []

            for column_index in range(0, dimensions[1]):
                column_val = row[column_index]
                # print(
                #     f"column index: {column_index} -> {column_val} | last col val: {last_column_val}"
                # )

                if last_column_val is None:
                    last_column_val = column_val

                if (last_column_val == "1" and column_val == "1") or column_val == "1":
                    adjacent_pairs.append((row_index, column_index))
                elif last_column_val == "1" and column_val == "0":
                    # print("last column val is not 1")
                    adjacent_row_indices.append(adjacent_pairs)
                    adjacent_pairs = []

                last_column_val = column_val
                # print(adjacent_pairs)

            # print("\n")

            if len(adjacent_pairs) > 0:
                adjacent_row_indices.append(adjacent_pairs)

        return adjacent_row_indices

    def get_cells_with_1(
        self, adjacent_row_indices: List[List[tuple[int, int]]]
    ) -> List[tuple[int, int]]:
        cell_indices = []

        for row in adjacent_row_indices:
            for cell in row:
                cell_indices.append(cell)

        return cell_indices

    def find_adjacent_cells_in_rows(
        self, adjacent_row_indices: List[List[tuple[int, int]]], dimesions, cells_with_1
    ):
        # print("\nfind_adjacent_cells_in_rows started")
        cells_with_1_in_same_col_counts = []

        for row_cells in adjacent_row_indices:
            # print()
            col_with_1_count = []

            for cell in row_cells:
                # print(cell)
                matched_cell_count = 1

                # check in downwards
                for next_row_index in range(cell[0]+1, dimesions[0]):
                    # print(next_row_index)
                    if (next_row_index, cell[1]) in cells_with_1:
                        # print("1 found in next row")
                        matched_cell_count += 1
                    else:
                        break

                # # check in upwards
                # print(f"starting row index: {cell[0]}")
                # for before_row_index in range(cell[0]-1, -1, -1):
                #     if (before_row_index, cell[1]) in cells_with_1:
                #         matched_cell_count += 1
                #     else:
                #         break

                    # print(f"before rows: {before_row_index}")

                col_with_1_count.append(matched_cell_count)

            # total_cells_in_rect_shape = self.get_rect_count(col_with_1_count)
            cells_with_1_in_same_col_counts.append(col_with_1_count)

            # max_total = max(max_total, total_cells_in_rect_shape)

            # print(f"\tmatched_col_count_for_each_cell: {col_with_1_count}")

        # find the cells in same column

        return cells_with_1_in_same_col_counts

    def get_rect_count(self, matched_col_vals):
        unique_vals = set()

        for item in matched_col_vals:
            unique_vals.add(item)

        return len(matched_col_vals) * min(unique_vals)

    def get_highest_possible_total_for_each_set(self, cells_with_1_in_same_col_counts):
        print("get_highest_possible_total_for_each_set started")
        totals = []

        for item in cells_with_1_in_same_col_counts:
            max_total = 0
            temp = item.copy()
            max_total = max(self.get_rect_count(temp), max_total)

            for round_num in range(1, len(item)):
                temp.pop()
                max_total = max(self.get_rect_count(temp), max_total)

            totals.append(max_total)

        return totals

    def get_the_set_with_highest_values(self, cells_with_1_in_same_col_counts):
        item_index = None
        highest_avg = 0

        for index, item in enumerate(cells_with_1_in_same_col_counts):
            avg = sum(item) / len(item)
            if avg > highest_avg:
                item_index = index
                highest_avg = avg

        return cells_with_1_in_same_col_counts[item_index]


print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
print(f"Expected: 6\n")

# print(Solution().maximalRectangle([["0"]]))
# print(f"Expected: 0\n")

print(Solution().maximalRectangle([["1"]]))
print(f"Expected: 1\n")

print(
    Solution().maximalRectangle(
        [
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1", "0", "0", "0"],
            ["0", "1", "1", "1", "1", "0", "0", "0"],
        ]
    )
)
print(f"Expected: 21\n")

print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "0", "1", "0"],
            ["0", "1", "1", "1", "1", "1"],
            ["1", "1", "0", "1", "1", "1"],
        ]
    )
)
print(f"Expected: 8\n")
