# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def _add_to_result(self, result, l, carry):
        while l is not None:
            current_val = l.val + carry
            carry = current_val // 10
            current_val %= 10
            result.next = ListNode(current_val)
            l = l.next
            result = result.next
        return result, carry

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current_val = l1.val + l2.val
        carry = current_val // 10
        current_val %= 10
        head = ListNode(current_val)
        l1 = l1.next
        l2 = l2.next
        result = head
        while l1 is not None and l2 is not None:
            current_val = l1.val + l2.val + carry
            carry = current_val // 10
            current_val %= 10
            result.next = ListNode(current_val)
            l1 = l1.next
            l2 = l2.next
            result = result.next
        result, carry = self._add_to_result(result, l1, carry)
        result, carry = self._add_to_result(result, l2, carry)
        if carry > 0:
            result.next = ListNode(carry)
        return head

if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(5)

    l1_ptr = l1
    for ii in [4, 3]:
        l1_ptr.next = ListNode(ii)
        l1_ptr = l1_ptr.next

    l2_ptr = l2
    for ii in [6]:
        l2_ptr.next = ListNode(ii)
        l2_ptr = l2_ptr.next
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    digits = []
    while result is not None:
        digits.append(result.val)
        result = result.next
    print(digits)
