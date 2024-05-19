class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        para_stack = []
        para_indices_stack = []
        paras = ['(', ')']

        for index, char in enumerate(s):
            if char in paras:
                if len(para_stack) > 0 and para_stack[-1] == paras[0] and char == paras[1]:
                    para_stack.pop()
                    para_indices_stack.pop()
                else:
                    para_stack.append(char)
                    para_indices_stack.append(index)

        # clean the string
        for index in para_indices_stack:
            s = s[:index] + '_' + s[index+1:]

        s = s.replace('_', '')

        return s


print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
print("----")
print(Solution().minRemoveToMakeValid("a)b(c)d"))
print("----")
print(Solution().minRemoveToMakeValid("))(("))
print("----")
print(Solution().minRemoveToMakeValid("f())x)(d))hj(()"))
