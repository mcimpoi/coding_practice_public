# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/


class Solution:
    def countOrders(self, n: int) -> int:
        # assume we have a solution for n - 1, let's assume their number
        # is sol[n - 1].
        # then step n is equivalent to inserting an ordered pair (Pn, Dn)
        # in any of the previous solutions.
        # this means, picking 2 positions out of 2n
        # (i.e. C(2*n, 2) = 2n * (2n - 1) / 2)
        # and therefore sol[n] = sol[n - 1] * C(2n, 2).

        # complexity: O(n), both runtime and memory.

        sol = [1 for _ in range(n + 1)]
        MODULO = int(1e9 + 7)

        for i in range(2, n + 1):
            sol[i] = (i * (2 * i - 1) * sol[i - 1]) % MODULO

        return sol[n]


if __name__ == "__main__":
    for testcase, expected_result in (
        (1, 1),
        (2, 6),
        (5, 113400),
        (499, 496638171),
    ):
        print(
            f"Testcase: {testcase}. Expected: {expected_result}."
            f" Actual: {Solution().countOrders(testcase)}"
        )
