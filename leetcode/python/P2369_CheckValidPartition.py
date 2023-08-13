# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # how would we solve it if array had 2 elements?
        #  --> check if the two are equal
        # if initial array had 3 e,ements:
        #  --> check if they are equal or increasing
        # for a new position, check the last 2 or 3 elements and
        # if the array up to that position is valid

        # O(n) time and memory; could probably store a shorter buffer
        #  for memory but not worth the effort.
        # (could do O(1) memory -- we need only a window of fixed size

        good = [False for _ in nums]

        if len(nums) == 1:
            return False
        if len(nums) == 0:
            return True
        if len(nums) == 2:
            return nums[0] == nums[1]

        good[1] = nums[0] == nums[1]
        good[2] = (nums[0] == nums[1] == nums[2]) or (
            nums[1] == nums[0] + 1 == nums[2] - 1
        )

        for i in range(3, len(nums)):
            good[i] = (nums[i] == nums[i - 1] and good[i - 2]) or (
                (
                    nums[i] == nums[i - 1] == nums[i - 2]
                    or nums[i - 1] == nums[i - 2] + 1 == nums[i] - 1
                )
                and good[i - 3]
            )

        return good[-1]
