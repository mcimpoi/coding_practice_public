# https://leetcode.com/problems/non-overlapping-intervals/
# Difficulty: Medium

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # n = len(intervals) <= 10^5 ==> max complexity nlogn
        # sort the intervals; then, compare the current interval with the "previous"
        # one;
        #
        # choose greedily to keep the
        #
        # prev,   crt
        # [1, 2], [1, 3], [2, 3], [3, 4]
        # [1, 2]; [1, 3] --> 2 > 1 ==> overlap;
        # but 3 > 2 ==> the current interval is shorter, keep it;
        # discard intervals greedily (intuition: wider interval has
        # higher chance to overlap)

        # TODO: Read solution and proof here (from editorial):
        # https://www.cs.umd.edu/class/fall2017/cmsc451-0101/Lects/lect07-greedy-sched.pdf
        intervals.sort()
        num_remove = 0
        prev_idx = 0

        for idx in range(1, len(intervals)):
            if intervals[prev_idx][1] > intervals[idx][0]:
                # discard the
                if intervals[prev_idx][1] > intervals[idx][1]:
                    prev_idx = idx
                num_remove += 1
            else:
                prev_idx = idx
        return num_remove

if __name__ == "__main__":
    s = Solution()
    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # 1
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))  # 2
    print(s.eraseOverlapIntervals([[1,2],[2,3]]))  # 0
    print(s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))  # 2
    print(s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))  # 2