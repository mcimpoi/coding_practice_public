# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from collections import deque, defaultdict
from typing import List, Optional


# LC Definition of TreeNode
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# (Re)Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self._val = x
        self._left = None
        self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left: Optional["TreeNode"]):
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right: Optional["TreeNode"]):
        self._right = right

    @property
    def val(self):
        return self._val


class Solution:
    def distanceK(
        self, root: Optional[TreeNode], target: Optional[TreeNode], k: int
    ) -> List[int]:
        # the graph has at most 500 nodes, with unique values;
        # we have no advantage from the fact that it is a binary tree;
        # 1) we can add a parent node -- traverse from there
        # 2) relax the definition to graph -- dfs up to length k

        if root is None or target is None:
            return []

        adj = defaultdict(list)  # this will have at most 3 elems for each entry
        adj[root.val] = []
        # convert to graph
        q = deque()
        q.append(root)

        while len(q) > 0:
            crt = q.pop()
            if crt.left is not None:
                adj[crt.val].append(crt.left.val)
                adj[crt.left.val].append(crt.val)
                q.append(crt.left)
            if crt.right is not None:
                adj[crt.val].append(crt.right.val)
                adj[crt.right.val].append(crt.val)
                q.append(crt.right)

        result = []

        max_key = max(adj.keys()) + 1 if len(adj) > 0 else 1
        visited = [False for _ in range(max_key)]

        q2 = deque()
        q2.append((target.val, 0))
        visited[target.val] = True

        while len(q2) > 0:
            crt_node, crt_dist = q2.pop()
            if crt_dist == k:
                result.append(crt_node)
            else:  # less than k
                for neighbor in adj[crt_node]:
                    if not visited[neighbor]:
                        q2.append((neighbor, crt_dist + 1))
                        visited[neighbor] = True

        return result


def build_example_tree() -> TreeNode:
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(4)
    root.left.right.left = TreeNode(7)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    return root


def build_example_tree2() -> TreeNode:
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.left.right.right.right = TreeNode(4)
    return root


if __name__ == "__main__":
    sol = Solution()
    example_tree = build_example_tree()
    result = sol.distanceK(example_tree, example_tree.left, 2)
    print(f"Expected: {sorted([1, 4, 7])} Actual: {sorted(result)}")

    example_tree2 = build_example_tree2()
    result = sol.distanceK(example_tree2, example_tree2.left.right.right, 0)
    print(f"Expected: {[3]} Actual: {sorted(result)}")
