# https://leetcode.com/problems/add-two-numbers-ii/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None or head.next is None:
                return head
            rest = reverseList(head.next)
            head.next.next = head

            head.next = None

            return rest

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        l1 = reverseList(l1)
        l2 = reverseList(l2)

        h1, h2 = l1, l2
        h3, h3_head = None, None

        carry = 0
        while h1 is not None or h2 is not None:
            val = carry
            if h1 is not None:
                val += h1.val
                h1 = h1.next

            if h2 is not None:
                val += h2.val
                h2 = h2.next

            node = ListNode(val % 10)
            carry = val // 10

            if h3 is None:
                h3 = node
                h3_head = node
            else:
                h3.next = node
                h3 = h3.next

        if carry == 1:
            # h3 can't be None here, having carry means we have
            # at least one element
            assert h3 is not None
            h3.next = ListNode(1)

        h3 = reverseList(h3_head)
        return h3
