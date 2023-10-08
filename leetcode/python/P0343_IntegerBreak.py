# https://leetcode.com/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:
        # intuition: for 2 parts, max product when numbers
        # are equal or differ by 1.
        # we don't know k;
        # n is small ... k can be up to n
        # at some point the product will start decreasing
        # so we stop
        # if n was larger, we could probably do binary search
        # for values of k.

        max_prod = n // 2 * (n - n // 2)
        prev_prod = max_prod
        for k in range(2, n):
            part = n // k
            extra = n % k
            crt_prod = (part) ** (k - extra) * (part + 1) ** (extra)
            if crt_prod < prev_prod:
                break
            max_prod = max(crt_prod, max_prod)
            prev_prod = crt_prod
        return max_prod
