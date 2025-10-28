inputs = [2, 6, 5, 1, 7, 3, 0]


def merge_sort(nums_range: tuple[int, int], nums: list[int]) -> list[int]:
    start, end = nums_range

    # handle single elements or empty ranges
    if end - start == 1:
        return nums[start:end]

    # divide to two parts
    first_part_size = (end - start) // 2
    first_part_range = (start, start + first_part_size)
    second_part_range = (first_part_range[1], end)

    # sort the parts recursively
    first_part_res = merge_sort(first_part_range, nums)
    second_part_res = merge_sort(second_part_range, nums)

    sorted_nums: list[int] = []
    first_index, second_index = 0, 0

    # compare the two and sort
    while first_index < len(first_part_res) and second_index < len(second_part_res):
        if first_part_res[first_index] <= second_part_res[second_index]:
            sorted_nums.append(first_part_res[first_index])
            first_index += 1
        else:
            sorted_nums.append(second_part_res[second_index])
            second_index += 1

    if first_index < len(first_part_res):
        sorted_nums.extend(first_part_res[first_index:])

    if second_index < len(second_part_res):
        sorted_nums.extend(second_part_res[second_index:])

    return sorted_nums


sorted_res = merge_sort((0, len(inputs)), inputs)
print(f"final: {sorted_res}")
