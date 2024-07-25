from typing import List

class Solution:
    def preProcessing(self, land: List[List[int]]) -> List[List[int]]:
        """
        This function identifies adjacent farmlands in each row and returns their coordinates.
        """
        adj_farms_in_row = []

        for row_index, row in enumerate(land):
            adj_groups = []
            current_group = []

            for col_index, elem in enumerate(row):
                if elem == 1:
                    current_group.append((row_index, col_index))
                    continue

                if len(current_group) > 0:
                    adj_groups.append(current_group)

                current_group = []

            if len(current_group) > 0:
                adj_groups.append(current_group)

            adj_farms_in_row.append(adj_groups)

        return adj_farms_in_row

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        This function check for the farmland groups with same column indices in each row.
        """

        adj_farms_in_row = self.preProcessing(land)
        result = []
        total_no_of_rows = len(adj_farms_in_row)

        for row_index, row_sets in enumerate(adj_farms_in_row):
            for a_set in row_sets:
                current_set = a_set
                no_of_rows = 0
                next_row_to_check = row_index

                while total_no_of_rows - 1 != next_row_to_check:
                    next_row_to_check += 1
                    # set of values to be looked for in next row
                    expected_set = [(elem[0] + 1, elem[1]) for elem in current_set]

                    # check the next row
                    if expected_set in adj_farms_in_row[next_row_to_check]:
                        no_of_rows += 1
                        adj_farms_in_row[next_row_to_check].remove(expected_set)
                        current_set = expected_set
                        continue

                    break

                result.append(
                    [a_set[0][0], a_set[0][1], a_set[-1][0] + no_of_rows, a_set[-1][1]]
                )

        return result


print(Solution().findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
print(f"Expected: [[0,0,0,0],[1,1,2,2]]\n")

# print(Solution().findFarmland([[1, 1], [1, 1]]))
# print(f"Expected: [[0,0,1,1]]\n")

# print(Solution().findFarmland([[0]]))
# print(f"Expected: []\n")

# print(Solution().findFarmland([[1]]))
# print(f"Expected: [[0,0,0,0]]\n")

# print(Solution().findFarmland([[1], [1], [1], [1], [1], [1], [1], [1]]))
# print(f"Expected: [[0,0,7,0]]\n")
