# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # keep a grid of number of ways
        # no need to pad; set 1 on all items on first row and column
        # at index (i, j) inside the dist matrix:
        #   ways[i, j] = ways[i, j-1] + ways[i - 1][j]
        # but it becomes 0 if thee is an obstacle.
        # Pay attention to obstacle at (0, 0).

        n_rows = len(obstacleGrid)
        # there is at least one element
        n_cols = len(obstacleGrid[0])

        ways = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

        for r in range(n_rows):
            for c in range(n_cols):
                ways[r][c] = 0
                if r == 0 and c == 0:
                    ways[r][c] = 1
                else:
                    if c > 0:
                        ways[r][c] += ways[r][c - 1]
                    if r > 0:
                        ways[r][c] += ways[r - 1][c]
                ways[r][c] *= 1 - obstacleGrid[r][c]

        return ways[-1][-1]
