# https://leetcode.com/problems/combinations/

from copy import copy
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(
            n: int,
            k: int,
            crt: int,
            val: int,
            crt_vec: List[int],
        ) -> None:
            if crt == k:
                result.append(copy(crt_vec))
                return

            for v in range(val, n + 1):
                crt_vec[crt] = v
                backtrack(n, k, crt + 1, v + 1, crt_vec)

        crt_vec = [0] * k
        backtrack(n, k, 0, 1, crt_vec)
        return result
