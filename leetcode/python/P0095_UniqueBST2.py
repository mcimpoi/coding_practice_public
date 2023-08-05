# https://leetcode.com/problems/unique-binary-search-trees-ii/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"({self.val}, L:({self.left}), R:({self.right}) )"


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # we need structurally unique BSTs.
        # if we have a single node --> there's only one way to build a BST
        # from that node.
        # if we have 2 nodes, [n1, n2] --> the largest one is root
        # smaller one is the left subtree; if the smaller one is root
        # the larger node will be right subtree;
        # assuming node k fixed, the nodes from 1 to k-1 will be in the
        # left subtree and nodes in k + 1..n --> right subtree

        # n = 8 --> just explore all trees.

        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]

            results = []
            for crt in range(start, end + 1):
                left_subs = generate(start, crt - 1)
                right_subs = generate(crt + 1, end)
                for left_root in left_subs:
                    for right_root in right_subs:
                        crt_node = TreeNode(crt, left_root, right_root)
                        results.append(crt_node)
            return results

        return generate(1, n)


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateTrees(3))
