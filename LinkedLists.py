from typing import Optional
import unittest


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, values):
        self.head = ListNode(values[-1])

        for i in reversed(range(len(values) - 1)):
            self.head = ListNode(values[i], self.head)


class Solution:

    def getValues(self, head: Optional[ListNode]) -> list:

        arr = [head.val]
        while head and head.next:
            arr.append(head.next.val)
            head = head.next

        return arr

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Remove node n places from end of list
        Trick for one pass is to have two of the same linked list, traverse through one until n, then the second will
        always lag the first by n, and can reassign last node of lagged list.
        """
        fast = slow = head
        # Traverse through list until n
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        # Traverse through both until initial ends
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Reassign last node of lagging list
        slow.next = slow.next.next
        return head


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_getValues(self):

        inp = [1, 2, 3, 4, 5]
        linked_list = LinkedList(inp)
        out = self.solution.getValues(linked_list.head)
        self.assertEqual(inp, out)

    def test_removeNthFromEnd(self):

        data = [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
                ([1], 1, []),
                ([1, 2], 1, [1])]

        i = 0
        for inp, n, out in data:
            linked_list = LinkedList(inp)
            result = self.solution.removeNthFromEnd(linked_list.head, n)

            if result is None:
                values = []
            else:
                values = self.solution.getValues(result)

            with self.subTest(i=i):
                self.assertEqual(values, out)
            i += 1

    def test_reverseList(self):

        data = [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])]

        i = 0
        for inp, out in data:
            linked_list = LinkedList(inp)
            result = self.solution.reverseList(linked_list.head)
            values = self.solution.getValues(result)
            with self.subTest(i=i):
                self.assertEqual(values, out)
            i += 1


def main():

    unittest.main()


if __name__ == "__main__":

    main()
