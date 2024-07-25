from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        saved_palindrome_res = {}

        def is_palindrome(string: str):
            result = True

            if string in saved_palindrome_res:
                return saved_palindrome_res[string]

            for index, char in enumerate(string):
                corr_index = len(string) - 1 - index

                if char != string[corr_index]:
                    result = False
                    break

            saved_palindrome_res[string] = result
            return result

        def get_valid_substrings(
            initial_size: int,
            current_substrings: List[List[str]],
            main_substrings
        ):

            for size in range(1, len(s) + 1 - initial_size):
                total_size = initial_size + size

                # check for palindrome
                substring = s[initial_size:total_size]
                is_valid = is_palindrome(substring)

                if not is_valid:
                    continue

                substrings_list = current_substrings.copy()
                substrings_list.append(substring)

                if total_size < len(s):
                    get_valid_substrings(
                        total_size,
                        substrings_list,
                        main_substrings,
                    )

                if total_size == len(s):
                    main_substrings.append(substrings_list)

        substring = []
        get_valid_substrings(0, [], substring)

        return substring


# print(f'{Solution().partition(s = "aab")}\nExpected: [["a","a","b"],["aa","b"]]')

print(
    f'{Solution().partition(s = "abbab")}\nExpected: [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]'
)

# print(
#     f'{Solution().partition(s ="abbab")}\nExpected: [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]]'
# )

# print(
#     f'{Solution().partition(s ="cbbbcc")}\nExpected: [["c","b","b","b","c","c"],["c","b","b","b","cc"],["c","b","bb","c","c"],["c","b","bb","cc"],["c","bb","b","c","c"],["c","bb","b","cc"],["c","bbb","c","c"],["c","bbb","cc"],["cbbbc","c"]]'
# )
