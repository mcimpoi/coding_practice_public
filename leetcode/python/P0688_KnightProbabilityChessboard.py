# https://leetcode.com/problems/knight-probability-in-chessboard/


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        return self.kprob(N, K, r, c, {})

    def isValid(self, row, col, N):
        return row >= 0 and col >= 0 and row < N and col < N

    def kprob(
        self, N: int, K: int, r: int, c: int, memo: Dict[Tuple[int, int, int], float]
    ) -> float:
        if K == 0:
            if self.isValid(r, c, N):
                return 1.0
            else:
                return 0.0

        p = (K, r, c)
        if p in memo:
            return memo[p]

        prob = 0.0
        for d_r, d_c in (
            (1, 2),
            (1, -2),
            (2, 1),
            (2, -1),
            (-1, 2),
            (-1, -2),
            (-2, 1),
            (-2, -1),
        ):
            next_row, next_col = r + d_r, c + d_c
            if self.isValid(next_row, next_col, N):
                prob += (1.0 / 8.0) * self.kprob(N, K - 1, next_row, next_col, memo)

        memo[p] = prob

        return prob
