class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        for index in range(len(haystack) - needle_len + 1):
            if haystack[index : index + needle_len] == needle:
                return index

        return -1

print(Solution().strStr(haystack="sadbutsad", needle="sad"))
print("Expected: 0\n")

print(Solution().strStr(haystack="leetcode", needle="leeto"))
print("Expected: -1\n")
