# Recursion - O(max(len(a), len(b)))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a,len_b = len(a), len(b)
        max_length = max(len_a, len_b)

        if max_length - len_b > 0:
            b = "0" * (max_length - len_b) + b

        if max_length - len_a > 0:
            a = "0" * (max_length - len_a) + a

        def addition_on_position(position: int, carry_over: int):
            if position == -1:
                return str(carry_over) if carry_over == 1 else ""

            value = int(a[position]) + int(b[position]) + carry_over
            bit_rep = str(value % 2)
            next_bit = addition_on_position(position - 1, value // 2)
            return next_bit + bit_rep

        return addition_on_position(max_length - 1, 0)


# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         len_a,len_b = len(a), len(b)
#         max_length = max(len_a, len_b)

#         if max_length - len_b > 0:
#             b = "0" * (max_length - len_b) + b

#         if max_length - len_a > 0:
#             a = "0" * (max_length - len_a) + a

#         carry_over = 0
#         result = ""

#         for a_index in range(max_length - 1, -1, -1):
#             value = int(a[a_index]) + int(b[a_index]) + carry_over
#             result = str(value % 2) + result
#             carry_over = value // 2

#         if carry_over > 0:
#             result = "1" + result

#         return result

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]


print(f"{Solution().addBinary(a = '11', b = '1')}\nExpected: 100")
print(f"{Solution().addBinary(a = '1010', b = '1011')}\nExpected: 10101")
