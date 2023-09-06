# https://leetcode.com/problems/split-linked-list-in-parts/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val}, {self.next})"


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        # we have to split a linked list in k consecutive linked list parts
        # balanced lengths;
        # e.g. initial list: length n --> parts will have lengths
        #  (n // k) and (n // k + 1) for the first n % k parts
        def get_list_length(head: Optional[ListNode]) -> int:
            crt = head
            list_len = 0
            while crt is not None:
                crt = crt.next
                list_len += 1
            return list_len

        list_length = get_list_length(head)

        result = []
        frag_length = list_length // k

        crt = head
        for i in range(k):
            keep_head = crt
            prev = crt
            crt_len = 0
            while crt is not None and crt_len < frag_length + (
                1 if i < list_length % k else 0
            ):
                prev = crt
                crt = crt.next
                crt_len += 1
            if prev is not None:
                prev.next = None
            result.append(keep_head)

        return result


if __name__ == "__main__":
    s = Solution()
    head = ListNode(
        1,
        ListNode(
            2,
            ListNode(3, next=ListNode(4, ListNode(5, ListNode(6)))),
        ),
    )
    k = 3
    print(s.splitListToParts(head, k))
