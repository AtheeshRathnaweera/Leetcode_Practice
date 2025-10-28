from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        last_index = None

        for index, actual_height in enumerate(height):
            if last_index is not None and last_index > index:
                continue

            end_data = self.find_end(actual_height, index, height)

            if end_data[0] is not None:
                last_index = end_data[0]
                total += end_data[1]
                continue

            lowered_height = actual_height - 1

            while lowered_height >= 0:
                end_data = self.find_end(lowered_height, index, height)

                if end_data[0] is not None:
                    last_index = end_data[0]
                    total += end_data[1]
                    break

                lowered_height -= 1

            if end_data[0] is None:
                last_index = end_data[0]

        return total

    def find_end(self, height: int, starting_index: int, heights: List[int]):
        sub_total = 0
        for sub_index in range(starting_index + 1, len(heights)):
            if height <= heights[sub_index]:
                return (sub_index, sub_total)

            sub_total += height - heights[sub_index]

        return (None, sub_total)


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(f"Expected: 6\n")

print()
print(Solution().trap([4, 2, 0, 3, 2, 5]))
print(f"Expected: 9")

print()
print(Solution().trap([4, 2, 3]))
print(f"Expected: 1")
