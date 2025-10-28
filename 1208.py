class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_len = 0
        pointers = [0, 0 + 1]
        prev_pointers = pointers.copy()
        diffs_sum = abs(ord(s[pointers[0]]) - ord(t[pointers[0]]))

        while pointers[1] <= len(s) and pointers[0] != len(s) - 1:
            if prev_pointers[1] < pointers[1]:
                diffs_sum += abs(ord(s[pointers[1] - 1]) - ord(t[pointers[1] - 1]))

            if prev_pointers[0] < pointers[0]:
                diffs_sum -= abs(ord(s[prev_pointers[0]]) - ord(t[prev_pointers[0]]))

            prev_pointers[0], prev_pointers[1] = pointers[0], pointers[1]

            if diffs_sum <= maxCost:
                max_len = max(max_len, pointers[1] - pointers[0])
                pointers[1] += 1
            else:
                pointers[0] += 1

        return max_len

print(
    f'{Solution().equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)}\n****Expected: 3\n\n'
)

print(
    f'{Solution().equalSubstring(s = "abcd", t = "cdef", maxCost = 3)}\n****Expected: 1\n\n'
)

print(
    f'{Solution().equalSubstring(s = "abcd", t = "acde", maxCost = 0)}\n****Expected: 1\n\n'
)

print(
    f'{Solution().equalSubstring(s = "abcd", t = "gcde", maxCost = 0)}\n****Expected: 0\n\n'
)

print(
    f'{Solution().equalSubstring(s = "krrgw", t = "zjxss", maxCost = 19)}\n****Expected: 2\n\n'
)

print(
    f'{Solution().equalSubstring(s = "anryddgaqpjdw", t = "zjhotgdlmadcf", maxCost = 5)}\n****Expected: 1\n\n'
)

print(
    f'{Solution().equalSubstring(s = "ujteygggjwxnfl", t = "nstsenrzttikoy", maxCost = 43)}\n****Expected: 5\n\n'
)

print(
    f'{Solution().equalSubstring(s = "krpgjbjjznpzdfy", t = "nxargkbydxmsgby", maxCost = 14)}\n****Expected: 4\n\n'
)
