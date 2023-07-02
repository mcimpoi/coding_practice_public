# https://leetcode.com/problems/is-graph-bipartite/
from collections import deque
from typing import List, Optional


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color: List[Optional[int]] = [None for _ in graph]

        for crt_node in range(len(graph)):
            if color[crt_node] is not None:
                continue
            q = deque()
            q.append(crt_node)
            color[crt_node] = 1
            while len(q) > 0:
                crt_ = q.pop()
                for n_ in graph[crt_]:
                    if color[n_] is not None:
                        if color[n_] == color[crt_]:
                            return False
                    else:
                        color[n_] = 1 - color[crt_]
                        q.append(n_)
        return True


if __name__ == "__main__":
    solution = Solution()
    for testcase, expected in (
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
        ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    ):
        print(
            f"Testcase:\n{testcase}\nExpected: {expected}\nResult: {solution.isBipartite(testcase)}\n"
        )
