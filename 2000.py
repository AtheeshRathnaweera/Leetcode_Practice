class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_index = word.find(ch)
        return word[:ch_index+1][::-1] + word[ch_index+1:]

print(Solution().reversePrefix(word="abcdefd", ch="i"))
print("Expected: abcdefd\n")

print(Solution().reversePrefix(word="abcdefd", ch="d"))
print("Expected: dcbaefd\n")

print(Solution().reversePrefix(word="xyxzxe", ch="z"))
print("Expected: zxyxxe\n")

print(Solution().reversePrefix(word="abcd", ch="z"))
print("Expected: abcd\n")
