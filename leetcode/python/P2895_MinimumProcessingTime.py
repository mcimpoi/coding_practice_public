# https://leetcode.com/problems/minimum-processing-time

from typing import List


class Solution:
    def minProcessingTime(
        self, processorTime: List[int], tasks: List[int]
    ) -> int:
        # n processors, 4 cores each, 4n tasks
        # each processor has a time when it becomes available;
        # max_{idx}(processorTime[i] + task[idx]) --> time when processor i
        # finishes assigned tasks.
        # n processors <= 25.000 --> nlogn is good enough.
        # => sort procTime (asc) and tasks (desc)
        # we only need the longest task - processor finishes when the longest
        # task is completed.
        processorTime.sort()
        tasks.sort(reverse=True)
        res = None
        for idx, pt in enumerate(processorTime):
            res = (
                pt + tasks[4 * idx]
                if res is None
                else max(res, pt + tasks[4 * idx])
            )
        return res or -1
