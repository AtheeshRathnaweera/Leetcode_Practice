# with convesion to a string
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num_str = str(x)
#         num_str_len = len(num_str)

#         for index in range(0, int(num_str_len / 2)):
#             if num_str[index] != num_str[num_str_len - 1 - index]:
#                 return False

#         return True


# without convesion to a string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = ''
        temp_num = x

        if x < 0:
            return False

        while 1:
            remainder = temp_num % 10
            reversed_num += str(remainder)
            temp_num = int((temp_num - remainder) / 10)

            if temp_num == 0:
                break

        return int(reversed_num) == x


print(Solution().isPalindrome(-121))
print("Expected: false\n")

print(Solution().isPalindrome(0))
print("Expected: true\n")

print(Solution().isPalindrome(10))
print("Expected: false\n")

# print(Solution().isPalindrome(121))
# print("Expected: true\n")

# print(Solution().isPalindrome(34566066543))
# print("Expected: true\n")

# print(Solution().isPalindrome(1))
# print("Expected: true\n")

# print(Solution().isPalindrome(13))
# print("Expected: false\n")
