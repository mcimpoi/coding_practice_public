from typing import List


class Solution:
    # number of cookie bags - n = len(cookies) is small --> can do brute-force
    # each bag -- k possibilities --> search space is k^n -- max 8^8

    # probably can be done by balancing -- pick pairs and swap, until convergence
    # not clear how, not trivial to implement

    # possibly binary search for solution -- e.g. between 1 and all cookies; order
    # of children does not matter; assign to child until <= amount (?) -- not clear how
    # to prove correctness.

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        max_unfairness = sum(cookies)
        totals = [0 for _ in range(k)]

        # TODO: access local variables without self (?)
        def backtrack(idx: int) -> None:
            nonlocal max_unfairness
            nonlocal totals

            # when we assigned all bags, compute unfairness, update minimum
            if idx == len(cookies):
                max_unfairness = min(max_unfairness, max(totals))
                return

            for child in range(k):
                totals[child] += cookies[idx]
                # This is important! if unfairness is already higher than current min
                # there is no point in continuing on this path
                if totals[child] < max_unfairness:
                    backtrack(idx + 1)
                totals[child] -= cookies[idx]

        backtrack(0)
        return max_unfairness


if __name__ == "__main__":
    solution = Solution()
    for testcase, expected in (
        (([8, 15, 10, 20, 8], 2), 31),
        (([6, 1, 3, 2, 2, 4, 1, 2], 3), 7),
        (([76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609], 8), 76265),
    ):
        print(
            f"Testcase:\n{testcase}\nExpected: {expected} Actual: {solution.distributeCookies(*testcase)}\n"
        )
