from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_in_list_01 = list1
        next_in_list_02 = list2
        sorted_list = []
        result = None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        while current_in_list_01 is not None:
            current_value = current_in_list_01.val
            next_node = current_in_list_01.next

            while next_in_list_02 is not None:
                if current_value >= next_in_list_02.val:
                    sorted_list.append(next_in_list_02.val)
                else:
                    break

                next_in_list_02 = next_in_list_02.next

            sorted_list.append(current_value)
            current_in_list_01 = next_node

        if next_in_list_02 is not None:
            while next_in_list_02 is not None:
                sorted_list.append(next_in_list_02.val)
                next_in_list_02 = next_in_list_02.next

        for item in sorted_list[::-1]:
            if result is None:
                result = ListNode(item, None)
                continue

            result = ListNode(item, result)

        return result


def list_nodes_to_string(list_nodes: ListNode):
    if list_nodes is None:
        return []

    next_node = list_nodes.next
    result = [list_nodes.val]

    while next_node is not None:
        result.append(next_node.val)
        next_node = next_node.next

    return result


print(
    list_nodes_to_string(Solution().mergeTwoLists(
        list1=ListNode(1, ListNode(2, ListNode(4))),
        list2=ListNode(1, ListNode(3, ListNode(4))),
    ))
)
print("Expected: [1,1,2,3,4,4]\n")

# print(
#     list_nodes_to_string(
#         Solution().mergeTwoLists(
#             list1=ListNode(5),
#             list2=ListNode(1, ListNode(2, ListNode(4))),
#         )
#     )
# )
# print("Expected: [1,2,4,5]\n")

# print(list_nodes_to_string(Solution().mergeTwoLists(list1=None, list2=None)))
# print("Expected: []\n")

# print(list_nodes_to_string(Solution().mergeTwoLists(list1=None, list2=ListNode(0))))
# print("Expected: [0]\n")

# print(list_nodes_to_string(Solution().mergeTwoLists(list1=ListNode(1), list2=ListNode(2))))
# print("Expected: [1, 2]\n")
