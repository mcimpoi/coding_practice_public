from collections import defaultdict, deque

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        q = deque()
        q.append((root, 0))
        columns = defaultdict(list)
        result = []
        while (len(q) > 0):
            (crt_node, crt_val) = q.popleft()
            columns[crt_val].append(crt_node.val)

            if crt_node.left is not None:
                q.append((crt_node.left, crt_val - 1))
            if crt_node.right is not None:
                q.append((crt_node.right, crt_val + 1))

        for key in sorted(columns.keys()):
            result.append(columns[key])
        return result

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print(s.verticalOrder(root))

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)

    print(s.verticalOrder(root))

    root.left.right.right = TreeNode(2)
    root.right.left.left = TreeNode(5)

    print(s.verticalOrder(root))

    root = TreeNode(4)
    print(s.verticalOrder(root))
