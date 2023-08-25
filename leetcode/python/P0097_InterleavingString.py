# https://leetcode.com/problems/interleaving-string/


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # keep one "pointer" for each of the strings;
        # if the letter in s3 corresponds to one of the 2 strings
        # advance
        # it matters from which string we advance:
        # e.g. s1 = abbc; s2 = addc; s3 addabbcc
        #   so 2 pointers would not work

        # if one of the strings is empty, pick everything from
        # the other string;

        # interleaved correctly up to "index" [i, j] if s3[i + j] == s1[i]
        # and match(i-1, j) or s3[i + j] == s2[j] and match(i, j -1)

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

        dp[0][0] = True

        # pay attention:
        for idx, ch in enumerate(s1):
            dp[0][idx + 1] = dp[0][idx] and s1[idx] == s3[idx]

        for idx, ch in enumerate(s2):
            dp[idx + 1][0] = dp[idx][0] and s2[idx] == s3[idx]

        for idx1 in range(1, len(s1) + 1):
            for idx2 in range(1, len(s2) + 1):
                dp[idx2][idx1] = (
                    dp[idx2][idx1 - 1] and s3[idx1 + idx2 - 1] == s1[idx1 - 1]
                ) or (dp[idx2 - 1][idx1] and s3[idx1 + idx2 - 1] == s2[idx2 - 1])

        print(dp)

        return dp[len(s2)][len(s1)]
