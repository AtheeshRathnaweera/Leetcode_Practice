from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_counts = {}

        if len(hand) % groupSize != 0:
            return False

        for card in hand:
            if card in card_counts:
                card_counts[card] += 1
            else:
                card_counts[card] = 1

        # Sort the keys
        sorted_keys = sorted(card_counts.keys())
        card_counts = {key: card_counts[key] for key in sorted_keys}

        for key, item in card_counts.items():
            for _ in range(0, item):
                card_counts[key] -= 1

                for step in range(1, groupSize):
                    expected_val = key + step

                    if expected_val in card_counts:
                        if card_counts[expected_val] > 0:
                            card_counts[expected_val] -= 1
                        else:
                            return False
                    else:
                        return False

        return True


# Time Limit Exceeded O(n^2)
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         print(f"original: {hand}")

#         if len(hand) % groupSize != 0:
#             return False

#         last_value = None
#         group_size = 0

#         for main_index, main_value in enumerate(hand):
#             matching_index = None
#             lowest_index = main_index

#             for sub_index in range(main_index, len(hand)):
#                 if group_size == 0 and hand[sub_index] <= hand[lowest_index]:
#                     matching_index = sub_index
#                     lowest_index = sub_index
#                     continue

#                 if group_size != 0 and hand[sub_index] == last_value + 1:
#                     matching_index = sub_index
#                     break

#             if matching_index is None:
#                 continue

#             if matching_index != main_index:
#                 hand[main_index] = hand[matching_index]
#                 hand[matching_index] = main_value

#             last_value = hand[main_index]
#             group_size += 1

#             if group_size == groupSize:
#                 last_value = None
#                 group_size = 0

#         print(f"original: {hand}")

#         return group_size == 0


print(
    f"\t{Solution().isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3)}\n\tExpected: True"
)

print(
    f"\t{Solution().isNStraightHand(hand = [1,2,3,4,5], groupSize = 4)}\n\tExpected: False"
)

print(
    f"\t{Solution().isNStraightHand(hand = [1,1,2,2,3,3], groupSize = 2)}\n\tExpected: False"
)
