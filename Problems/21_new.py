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
        merged = None

        # traversing parallerly
        while list1 or list2:
            list1_val = list1.val
            list2_val = list2.val

            print(f"list1 elem: {list1.val}")
            print(f"list2 elem: {list2.val}")

            if list1_val <= list2_val:
                list1.val = list2_val
                list1.next = list1.next

                list1 = list1.next
                list2 = list2.next

            list1 = list1.next
            list2 = list2.next

        return merged


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
