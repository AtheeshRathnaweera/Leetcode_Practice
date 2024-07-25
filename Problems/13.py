class Solution:
    def romanToInt(self, s: str) -> int:
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        value = 0
        prev_value = None

        for numeral in s[::-1]:
            current_value = mappings.get(numeral)

            if prev_value is None or (prev_value <= current_value):
                value += current_value
            else:
                value -= current_value

            prev_value = current_value

        return value

print(Solution().romanToInt(""))
print("Expected: 0\n")

print(Solution().romanToInt("III"))
print("Expected: 3\n")

print(Solution().romanToInt("LVIII"))
print("Expected: 58\n")

print(Solution().romanToInt("MCMXCIV"))
print("Expected: 1994\n")

print(Solution().romanToInt("MCMLXXV"))
print("Expected: 1975\n")
