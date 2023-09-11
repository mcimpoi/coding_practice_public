# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

from typing import List, Dict


class Solution:
    def groupThePeople(self, group_sizes: List[int]) -> List[List[int]]:
        # n is small (<= 500)
        # we can return any solution, so we can fill groups
        # as they occur.
        # keep a dict size: list of elements
        # when we reach the capacity for the list, append it to the
        # solution
        result: List[List[int]] = []
        buffers: Dict[int, List] = {}
        for num, group_sz in enumerate(group_sizes):
            if buffers.get(group_sz, None) is None:
                buffers[group_sz] = []
            buffers[group_sz].append(num)
            if len(buffers[group_sz]) == group_sz:
                result.append(buffers[group_sz])
                buffers[group_sz] = []

        return result
