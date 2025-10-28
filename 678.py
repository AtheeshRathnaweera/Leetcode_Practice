class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opening_para = []
        closing_para = []
        stars = []

        # match opening and closing parenthesis
        for index, char in enumerate(s):
            if char == "(":
                opening_para.append(index)
            elif char == ")":
                if len(opening_para) > 0 and index > opening_para[-1]:
                    opening_para.pop()
                else:
                    closing_para.append(index)
            elif char == "*":
                stars.append(index)

        # check if stars are available for remaining parenthesis
        if (len(opening_para) > 0 or len(closing_para) > 0) and len(stars) == 0:
            return False

        # find relevant closing paranethesis for remaing opening parenthesis
        for para_index in opening_para.copy():
            star_index = self.check_if_star_exist_for_para("(", para_index, stars)

            if star_index is not None:
                stars.remove(star_index)
                opening_para.pop(0)
            else:
                return False

        # find relevant opening paranethesis for remaing closing parenthesis
        for para_index in closing_para.copy():
            star_index = self.check_if_star_exist_for_para(")", para_index, stars)

            if star_index is not None:
                stars.remove(star_index)
                closing_para.pop(0)
            else:
                return False

        return len(opening_para) == 0 and len(closing_para) == 0

    def check_if_star_exist_for_para(self, para_type, para_index, stars):
        for star in stars:
            if para_type == "(":
                if star > para_index:
                    return star
            elif para_type == ")":
                if star < para_index:
                    return star

        return None


print(Solution().checkValidString("()"))
print("----------- Expected: TRUE")
print(Solution().checkValidString("(*)"))
print("----------- Expected: TRUE")
print(Solution().checkValidString("(*))"))
print("----------- Expected: TRUE")
print(Solution().checkValidString("(()*"))
print("----------- Expected: TRUE")
print(Solution().checkValidString("("))
print("----------- Expected: FALSE")
print(
    Solution().checkValidString(
        "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
    )
)
print("----------- Expected: TRUE")
