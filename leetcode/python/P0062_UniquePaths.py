# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(128)] for _ in range(128)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c]

        return dp[m - 1][n - 1]
