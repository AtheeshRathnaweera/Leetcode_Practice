from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        output_binary = []
        required_operations_count = 0

        # get the min length of each binary
        highest_num = max(max(nums), k)
        min_length = len(self.get_binary_num(highest_num))

        # calculate input xor
        input_xor = None
        for num in nums:
            binary = self.get_binary_num(num)

            diff = min_length - len(binary)
            if diff != 0:
                binary.extend([0] * diff)

            if input_xor is None:
                input_xor = binary
                continue

            for index, bit in enumerate(binary):
                input_xor[index] = (input_xor[index] + bit) % 2

        # generate the binary representation of the output
        output_binary = self.get_binary_num(k)

        # normalize output binary length
        output_bits_diff = min_length - len(output_binary)
        if output_bits_diff != 0:
            output_binary.extend([0] * output_bits_diff)

        for index, output_bit in enumerate(output_binary):
            if output_bit != input_xor[index]:
                required_operations_count += 1

        return required_operations_count

    def get_binary_num(self, num: int):
        binary_num_stack = []
        temp_num = float(num)

        while temp_num not in [0.0, 1.0]:
            remainder = temp_num % 2
            binary_num_stack.append(int(remainder))

            if remainder == 1:
                temp_num = (temp_num - 1) / 2
            else:
                temp_num = temp_num / 2

        binary_num_stack.append(int(temp_num))

        return binary_num_stack

print(Solution().minOperations(nums=[2, 1, 3, 4], k=1))
print("Expected: 2\n")

print(Solution().minOperations(nums=[2, 0, 2, 0], k=0))
print("Expected: 0\n")

print(Solution().minOperations(nums=[3, 13, 9, 8, 5, 18, 11, 10], k=13))
print("Expected: 2\n")
