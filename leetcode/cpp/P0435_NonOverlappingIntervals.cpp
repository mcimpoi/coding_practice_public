// https://leetcode.com/problems/non-overlapping-intervals/

#include <algorithm>
#include <vector>

class Solution {
 public:
  int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
    if (intervals.size() == 1) {
      return 0;
    }

    std::sort(intervals.begin(), intervals.end(),
              [](const std::vector<int>& lhs, const std::vector<int>& rhs) {
                if (lhs[0] == rhs[0]) {
                  return lhs[1] < rhs[1];
                }
                return lhs[0] < rhs[0];
              });

    int prev = 0;
    int count = 0;

    for (int ii = 1; ii < intervals.size(); ++ii) {
      if (intervals[prev][1] > intervals[ii][0]) {
        if (intervals[prev][1] > intervals[ii][1]) {
          prev = ii;
        }
        ++count;
      } else {
        prev = ii;
      }
    }

    return count;
  }
};
