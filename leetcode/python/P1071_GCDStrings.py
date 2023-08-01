# https://leetcode.com/problems/greatest-common-divisor-of-strings/


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b) -> int:
            if a == 0 or b == 0:
                return a + b
            return gcd(max(a, b) % min(a, b), min(a, b))

        gcd_len = gcd(len(str1), len(str2))

        substr = str1[:gcd_len]
        if str1 != substr * (len(str1) // gcd_len) or str2 != substr * (
            len(str2) // gcd_len
        ):
            return ""

        return substr
