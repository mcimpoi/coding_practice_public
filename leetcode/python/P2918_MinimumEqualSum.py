# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)

        nzero1 = sum([1 for num in nums1 if num == 0])
        nzero2 = sum([1 for num in nums2 if num == 0])

        if nzero1 == 0 and nzero2 == 0:
            return sum1 if sum1 == sum2 else -1
        if nzero1 == 0 and nzero2 != 0:
            return sum1 if sum1 - sum2 >= nzero2 else -1
        if nzero2 == 0 and nzero1 != 0:
            return sum2 if sum2 - sum1 >= nzero1 else -1

        return max(sum1 + nzero1, sum2 + nzero2)
