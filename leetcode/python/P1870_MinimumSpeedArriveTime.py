# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

from typing import List
from math import ceil


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # hour must be >= len(dist)
        # speed is integer;
        # can be at least 1

        # computing the right bound:
        # round up to hour for each element before the last one;
        # the dist[-1] <= (hour - len(dist) + 1)
        # initialize right to be dist[-1] // (hour - len(dist) + 1)

        # binary search -- everytime we find a good current time
        #  --> update the result; mid will always be decreasing
        # for values going to left. (i.e. right = mid - 1)

        def compute_time(dist: List[int], mid: int) -> float:
            total: float = 0.0

            for d in dist[:-1]:
                total += ceil(d / mid)
            total += dist[-1] / float(mid)
            return total

        if hour == float(len(dist) - 1):
            # otherwise we get division by 0 when computing the right bound
            return -1

        left = 1
        right = 1 + max(max(dist), int(dist[-1] // (hour - len(dist) + 1)))

        res = -1

        while left <= right:
            mid = (left + right) // 2
            crt_time = compute_time(dist, mid)

            if crt_time <= hour:
                print(mid)
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
