class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if len(stack) != 0 and char in mappings:
                if stack[-1] == mappings[char]:
                    stack.pop()
                    continue

                return False

            stack.append(char)

        return len(stack) == 0


print(Solution().isValid(s="]"))
print("Expected: false\n")

print(Solution().isValid(s = "({[]})"))
print("Expected: true\n")

print(Solution().isValid(s = "()"))
print("Expected: true\n")

print(Solution().isValid(s = "()[]{}"))
print("Expected: true\n")

print(Solution().isValid(s = "(]"))
print("Expected: false\n")
