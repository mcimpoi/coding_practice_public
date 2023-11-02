# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # num1 + num2 = n(n+1) / 2 := S
        # num1 - num2 =  S - 2 * num2
        return n * (n + 1) // 2 - 2 * sum([x for x in range(n + 1) if x % m == 0])
