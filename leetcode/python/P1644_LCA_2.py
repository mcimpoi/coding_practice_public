# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

from typing import List, Tuple, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        # search for node in the tree, keep the path to node;
        # if not found --> return empty path
        # path will contain path from root to node.
        # for the two paths --> return the last node equal.

        def pathToNode(
            root: Optional[TreeNode],
            node: TreeNode,
            current_path: List[TreeNode],
        ) -> Tuple[bool, List[TreeNode]]:
            if root is None:
                return False, []
            path_to_here: List[TreeNode] = current_path + [root]
            if root == node:
                return True, path_to_here
            else:
                left_res, left_list = pathToNode(root.left, node, path_to_here)
                if left_res:
                    return True, left_list
                return pathToNode(root.right, node, path_to_here)

        has_path_p, path_to_p = pathToNode(root, p, [])
        has_path_q, path_to_q = pathToNode(root, q, [])

        if not has_path_p or not has_path_q:
            return None

        last_common = None

        for n1, n2 in zip(path_to_p, path_to_q):
            if n1 == n2:
                last_common = n1
            else:
                break
        return last_common


# TODO: add example tests
