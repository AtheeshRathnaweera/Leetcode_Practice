class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        good_s = s
        selected_chars = []

        for char in s:
            if char not in selected_chars and char.isupper():
                selected_chars.append(char)
                possible_pairs = [char.lower() + char, char + char.lower()]

                for possible_pair in possible_pairs:
                    if possible_pair in good_s:
                        good_s = good_s.replace(possible_pair, '')

        if len(s) != len(good_s):
            good_s = self.makeGood(good_s)

        return good_s


print(Solution().makeGood("leEeetcode"))
print("----")
print(Solution().makeGood("abBAcC"))
print("----")
print(Solution().makeGood("mC"))
print("----")
print(Solution().makeGood("hHcOzoC"))

print("----")
print(Solution().makeGood("IcCiJhHjqrqwTIJgEeGjitWQRQLICcilJ"))
