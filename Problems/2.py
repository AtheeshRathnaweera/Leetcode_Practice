# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_01 = self.toReversedNumber(l1)
        num_02 = self.toReversedNumber(l2)
        total = num_01 + num_02
        res = self.toReversedLinkedList(total)

        return res

    def toReversedNumber(self, l):
        """
        :type l: ListNode
        :rtype: int
        """
        current_node = l
        number = ''

        while current_node is not None:
            number = str(current_node.val) + number
            current_node = current_node.next

        return int(number)

    def toReversedLinkedList(self, num):
        """
        :type num: int
        :rtype: ListNode
        """
        res = None

        for char in str(num):
            if res is None:
                res = ListNode(int(char), None)
            else:
                res = ListNode(int(char), res)

        return res

print(
    Solution().addTwoNumbers(
        ListNode(2, ListNode(4, ListNode(3, None))),
        ListNode(5, ListNode(6, ListNode(4, None)))
    )
)
print("----")
print(Solution().addTwoNumbers(ListNode(0, None), ListNode(0, None)))
