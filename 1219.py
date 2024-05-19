from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # print(grid)
        directions = [1, 2, 3, 4]
        grid_size = (len(grid), len(grid[0]))
        highest_total = 0

        def go_to_next_cell(visited_cells, total, cell_cords, collected_total):
            # print(f"{cell_cords} {grid[cell_cords[0]][cell_cords[1]]} {visited_cells}")

            if grid[cell_cords[0]][cell_cords[1]] == 0:
                # print(f"total before return: {total}")
                return total

            # find the values of each direction
            for direction in directions:
                # print(f"{cell_cords} {grid[cell_cords[0]][cell_cords[1]]} {direction} {total}")
                next_val = 0
                next_cords = None

                # up
                if direction == 1:
                    next_cords = (cell_cords[0] - 1, cell_cords[1])
                # right
                if direction == 2:
                    next_cords = (cell_cords[0], cell_cords[1] + 1)
                # down
                if direction == 3:
                    next_cords = (cell_cords[0] + 1, cell_cords[1])
                # left
                if direction == 4:
                    next_cords = (cell_cords[0], cell_cords[1] - 1)

                # print(f"next cord: {next_cords}")

                if (next_cords[0] < 0 or next_cords[0] == grid_size[0]) or (next_cords[1] < 0 or next_cords[1] == grid_size[1]):
                    # local_highest = max(local_highest, total)
                    continue

                next_val = grid[next_cords[0]][next_cords[1]]

                # print(f"next cord: {next_cords} next val: {next_val}")

                if next_val == 0 or (next_cords in visited_cells):
                    # local_highest = max(local_highest, total)
                    continue

                # total += next_val
                visited_cells.append(next_cords)
                received = go_to_next_cell(visited_cells, total + next_val, next_cords, collected_total)
                # print(f"received value: {received}")
                total = max(total, received)

            collected_total.append(total)
            # print(f"** path is over: {visited_cells} total: {total}")
            ended_cell = visited_cells.pop()
            # print(f"** path is over: new visited: {visited_cells}")
            total = total - grid[ended_cell[0]][ended_cell[1]]

            # print(collected_total)

            return total

        for row_index, columns in enumerate(grid):
            for column_index, value in enumerate(columns):
                # print()
                collected_total = [value]
                total = go_to_next_cell(
                    [(row_index, column_index)],
                    value,
                    (row_index, column_index),
                    collected_total,
                )
                # print(f"received total: {total}")
                # print(f"collected totals: {collected_total}")
                highest_total = max(highest_total, max(collected_total))
                # print(f"\ncurrent highest: {highest_total}")

        # go_to_next_cell([], 0, (0,0))

        return highest_total

print(f"{Solution().getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]])}\nExpected: {24}")
print(
    f"{Solution().getMaximumGold(grid=[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])}\nExpected: {28}"
)
