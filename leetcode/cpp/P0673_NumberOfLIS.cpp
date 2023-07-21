// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

#include <algorithm>
#include <vector>

class Solution {
 public:
  int findNumberOfLIS(std::vector<int>& nums) {
    std::vector<int> lengths(nums.size(), 0);
    std::vector<int> counts(nums.size(), 1);

    int thelength = 0;

    for (int ii = 0; ii < nums.size(); ++ii) {
      for (int jj = 0; jj < ii; ++jj) {
        if (nums[jj] < nums[ii]) {
          if (lengths[jj] >= lengths[ii]) {
            lengths[ii] = lengths[jj] + 1;
            counts[ii] = counts[jj];
          } else if (lengths[jj] + 1 == lengths[ii]) {
            counts[ii] += counts[jj];
          }
        }
      }
    }

    int maxlength = 0;
    int cnt = 0;
    for (int ii = 0; ii < nums.size(); ++ii) {
      maxlength = std::max(lengths[ii], maxlength);
    }
    // cout << maxlength << " ";
    for (int ii = 0; ii < nums.size(); ++ii) {
      if (lengths[ii] == maxlength) {
        cnt += counts[ii];
      }
    }

    return cnt;
  }
};