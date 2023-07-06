from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # following c++ implementation

        left, right, crt_sum = 0, 0, 0
        min_length = len(nums) + 1

        while right < len(nums):
            while right < len(nums) and crt_sum < target:
                crt_sum += nums[right]
                right += 1

            if crt_sum >= target:
                min_length = min(min_length, right - left)

            while left < right and crt_sum >= target:
                crt_sum -= nums[left]
                left += 1
                if crt_sum >= target:
                    min_length = min(min_length, right - left)

        return min_length % (len(nums) + 1)
