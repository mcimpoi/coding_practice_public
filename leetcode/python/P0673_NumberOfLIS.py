# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # len(nums) <= 2000 --> O(n^2) should work.
        # keep dp[i] = length of LIS up to i, inclusive.
        # for current i, take the max of previous values.

        # use Counter to get the count of max element in dp[i]
        # or just keep track of max value, i.e. length of LIS

        dp = [1] * len(nums)
        cnt = [0] * len(nums)

        max_len = 1

        cnt[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])
            # once all lengths are updated
            # count how many sequences of length dp[i]
            # end here.
            for j in range(0, i):
                if nums[i] > nums[j] and dp[j] == dp[i] - 1:
                    cnt[i] += cnt[j]
            cnt[i] = max(cnt[i], 1)

        res = 0
        for d, c in zip(dp, cnt):
            if d == max_len:
                res += max(1, c)

        return res


# TODO testcases
# [1,3,5,4,7]
# [2,2,2,2,2]
# [1,2,4,3,5,4,7,2]
# [1,3,2]
# [1,1,1,2,2,2,3,3,3]
