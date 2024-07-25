from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        print(nums)
        calculated_xor: dict[int, int] = {}

        def get_highest_possible_xor(num_01):
            stored_calculated_val = calculated_xor.get(num_01)
            if stored_calculated_val is not None:
                return stored_calculated_val

            print()

            highest_val = num_01
            calc_val = num_01 ^ k
            print(f"{num_01} -> {calc_val}")

            while calc_val != num_01 and highest_val < calc_val:
                calc_val = num_01 ^ k
                print(f"{num_01} -> {calc_val}")
                highest_val = max(highest_val, calc_val)

            return highest_val

        # nums_copy = nums.copy()

        # for index, num in enumerate(nums):
        #     nums_copy[index] = get_highest_possible_xor(num)

        # print(nums_copy)

        # return sum(nums_copy)

        def find_max_diff(
            updated_nums: List[int], edges_to_operate: List[List[int]], max_diff: int
        ):
            print(f"\nupdated nums: {updated_nums}\nedges to operate: {edges_to_operate} max diff: {max_diff}")

            for operate_edge in edges_to_operate:
                num_01_xor = updated_nums[operate_edge[0]] ^ k
                num_02_xor = updated_nums[operate_edge[1]] ^ k

                print(f"vals for {operate_edge} -> {num_01_xor}, {num_02_xor}")

                total_diff = (num_01_xor - nums[operate_edge[0]]) + (
                    num_02_xor - nums[operate_edge[1]]
                )
                print(f"total diff: {total_diff}")
                max_diff = max(max_diff, total_diff)

            if len(edges_to_operate) == 1:
                print(f"last max_diff: {max_diff}")
                return max_diff

            fixed_edge = edges_to_operate.pop(0)
            print(f"fixed edge for next: {fixed_edge}")

            updated_nums_new = updated_nums.copy()
            updated_nums_new[fixed_edge[0]] = updated_nums[fixed_edge[0]] ^ k
            updated_nums_new[fixed_edge[1]] = updated_nums[fixed_edge[1]] ^ k

            return find_max_diff(updated_nums_new, edges_to_operate, max_diff)

        max_diff = 0

        for edge in edges:
            print(f"\n--main edge: {edge}")
            temp_nums = nums.copy()
            temp_nums[edge[0]] = temp_nums[edge[0]] ^ k
            temp_nums[edge[1]] = temp_nums[edge[1]] ^ k

            temp_edges = edges.copy()
            temp_edges.remove(edge)

            diff = (temp_nums[edge[0]] - nums[edge[0]]) + (temp_nums[edge[1]] - nums[edge[1]])
            print(f"diff: {diff}")

            max_diff = max(max_diff, diff)
            max_diff = find_max_diff(temp_nums, temp_edges, max_diff)
            print(f"new max diff: {max_diff}")

        print(f"final max diff: {max_diff}")
        print(f"normal total: {sum(nums)}")

        return 1


# print(f"{Solution().maximumValueSum(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]])}\nExpected: 6")
# print(
#     f"{Solution().maximumValueSum(nums = [2,3], k = 7, edges = [[0,1]])}\nExpected: 9"
# )
# print(
#     f"{Solution().maximumValueSum(nums = [7,7,7,7,7,7], k = 3, edges = [[0,1],[0,2],[0,3],[0,4],[0,5]])}\nExpected: 42"
# )
print(
    f"{Solution().maximumValueSum(nums = [24,78,1,97,44], k = 6, edges = [[0,2],[1,2],[4,2],[3,4]])}\nExpected: 260"
)
