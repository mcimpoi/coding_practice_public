# https://leetcode.com/problems/check-if-array-is-good

from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_n = max(nums)
        if len(nums) != max_n + 1:
            return False
        sorted_nums = list(range(1, max_n + 1)) + [max_n]

        return sorted(nums) == sorted_nums
