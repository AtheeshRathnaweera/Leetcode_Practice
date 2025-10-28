from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return result


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next

        return head


# # Test 01
# # head = [1,2,6,3,4,5,6], val = 6
# # Output: [1, 2, 3, 4, 5]
list_01 = ListNode(
    1,
    ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))),
)
test_01_res = Solution().removeElements(list_01, 6)
if test_01_res is not None:
    print(test_01_res.toString())
else:
    print("None")

print("\n\n#######################\n\n")

# # Test 02
# # head = [], val = 1
# # Output: []
list_02 = ListNode(None, None)
test_02_res = Solution().removeElements(list_02, 1)
if test_02_res is not None:
    print(test_02_res.toString())
else:
    print("None")

print("\n\n#######################\n\n")

# # Test 03
# # head = [7,7,7,7], val = 7
# # Output: []
list_03 = ListNode(
    7,
    ListNode(
        7,
        ListNode(
            7,
        ),
    ),
)
test_03_res = Solution().removeElements(list_02, 1)
if test_02_res is not None:
    print(test_02_res.toString())
else:
    print("None")

print("\n\n#######################\n\n")

# Test 04
# head = [1,2,2,1], val = 2
# Output: [1,1]
list_04 = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
test_04_res = Solution().removeElements(list_04, 2)
if test_04_res is not None:
    print(test_04_res.toString())
else:
    print("None")
