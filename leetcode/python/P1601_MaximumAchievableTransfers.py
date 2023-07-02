# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/
from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # there are only up to 16 requests; can use a binary mask, i.e.
        # loop up to 2^16 and validate if each building has a net 0;
        # update the maximum number of transfers.

        # alternative: backtracking;

        def bitmask() -> int:
            result = 0

            for mask in range(2 ** len(requests)):
                binmask = f"{mask:0b}".zfill(len(requests))

                building_deltas = [0 for _ in range(n)]
                for idx, val in enumerate(binmask):
                    if val == "1":
                        from_, to_ = requests[idx]
                        building_deltas[from_] -= 1
                        building_deltas[to_] += 1

                ok = True
                for delta in building_deltas:
                    if delta != 0:
                        ok = False
                        break

                if ok:
                    # print(binmask, building_deltas)
                    result = max(result, sum(int(x) for x in binmask))

            return result

        building_deltas = [0 for _ in range(n)]
        result = 0
        approved = 0

        def backtracking(idx: int) -> None:
            nonlocal result  # could be param
            nonlocal building_deltas
            nonlocal approved

            if idx == len(requests):
                ok = True
                for item in building_deltas:
                    if item != 0:
                        ok = False
                        break
                if ok:
                    result = max(result, approved)
                return

            for approve in (True, False):
                if approve:
                    from_, to_ = requests[idx]
                    building_deltas[from_] -= 1
                    building_deltas[to_] += 1
                    approved += 1

                    backtracking(idx + 1)

                    approved -= 1
                    building_deltas[from_] += 1
                    building_deltas[to_] -= 1
                else:
                    backtracking(idx + 1)

        backtracking(0)
        return result
