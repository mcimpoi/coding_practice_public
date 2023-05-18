# https://leetcode.com/problems/add-two-numbers

from typing import Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution(object):
    def _add_to_result(
        self, result: Optional[ListNode], node: Optional[ListNode], carry: int
    ) -> Tuple[Optional[ListNode], int]:
        while node is not None and result is not None:
            current_val = node.val + carry
            carry = current_val // 10
            current_val %= 10
            result.next = ListNode(current_val)
            node = node.next
            result = result.next
        return result, carry

    def addTwoNumbers(
        self, first_list: Optional[ListNode], second_list: Optional[ListNode]
    ) -> Optional[ListNode]:
        if first_list is None or second_list is None:
            return None
        current_val = first_list.val + second_list.val
        carry = current_val // 10
        current_val %= 10
        head = ListNode(current_val)
        first_list = first_list.next
        second_list = second_list.next
        result = head
        while first_list is not None and second_list is not None:
            current_val = first_list.val + second_list.val + carry
            carry = current_val // 10
            current_val %= 10
            result.next = ListNode(current_val)
            first_list = first_list.next
            second_list = second_list.next
            result = result.next
        result, carry = self._add_to_result(result, first_list, carry)
        result, carry = self._add_to_result(result, second_list, carry)
        if carry > 0 and result is not None:
            result.next = ListNode(carry)
        return head


if __name__ == "__main__":
    first_list = ListNode(2)
    second_list = ListNode(5)

    l1_ptr = first_list
    for ii in [4, 3]:
        l1_ptr.next = ListNode(ii)
        l1_ptr = l1_ptr.next

    l2_ptr = second_list
    for ii in [6]:
        l2_ptr.next = ListNode(ii)
        l2_ptr = l2_ptr.next

    s = Solution()
    result = s.addTwoNumbers(first_list, second_list)
    digits = []
    while result is not None:
        digits.append(result.val)
        result = result.next
    print(digits)
