# https://leetcode.com/problems/two-sum/
from collections import defaultdict


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        counts = defaultdict(int)
        idx = defaultdict(set)
        for ii, num in enumerate(nums):
            counts[num] += 1
            idx[num].add(ii)
        for num in nums:
            to_search = target - num
            if to_search == num:
                if counts[num] >= 2:
                    return [idx[num].pop(), idx[num].pop()]
            elif counts[to_search] > 0:
                return [idx[num].pop(), idx[to_search].pop()]
        return [-1, -1]

    def twoSum_On2_O1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for ii in range(0, n):
            for jj in range(ii + 1, n):
                if nums[ii] + nums[jj] == target:
                    return [ii, jj]
        return [-1, -1]
