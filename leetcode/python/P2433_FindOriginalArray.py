# https://leetcode.com/problems/find-the-original-array-of-prefix-xor

from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        def v1(pref: List[int]) -> List[int]:
            res = [0 for _ in pref]
            res[0] = pref[0]
            crt = 0
            # build prefix so far in crt;
            # xor with pref --> gives last element
            for i, p in enumerate(pref):
                res[i] = p ^ crt
                crt ^= res[i]
            return res

        # pref[i] = xor for all elements up to i
        # pref[i + 1] = xor for all elem up to i + 1
        # pref[i] XOR pref[i + 1] = elem[i+1], because all others cancel out
        res = []
        for p_, n_ in zip([0] + pref, pref):
            res.append(p_ ^ n_)
        return res
