# https://leetcode.com/problems/all-possible-full-binary-trees/

from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # small n -> brute force, i.e. generate everything would work
        # all complete trees have an odd number of nodes, because each
        # node can have 0 or 2 descendants

        # keep previously generated trees in a cache
        # when we loop over j, the previous caches are all generated

        # e.g. i = 3 --> j will be 1
        # i = 5 --> j = 1, 3

        # complexity: at step i --> Sum over "O"(i) * "O"(n - i)
        #  possibly exponential
        # for n = 19 --> there's about 5k possible trees.

        cache = defaultdict(list)
        cache[1] = [TreeNode()]

        for i in range(1, n + 1):
            if i % 2 == 0:
                continue
            if len(cache[i]) == 0:
                for j in range(1, i, 2):
                    lefts = cache[j]
                    rights = cache[i - j - 1]

                    for left in lefts:
                        for right in rights:
                            root = TreeNode()
                            root.left = left
                            root.right = right
                            cache[i].append(root)
        return cache[n]
