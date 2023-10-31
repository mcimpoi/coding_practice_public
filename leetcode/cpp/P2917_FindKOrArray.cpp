// https://leetcode.com/problems/find-the-k-or-of-an-array
#include <vector>

class Solution {
 public:
  int findKOr(std::vector<int>& nums, int k) {
    int res = 0;
    for (int ii = 0; ii < 32; ++ii) {
      int mask = 1 << ii;
      int cnt = 0;
      for (int num : nums) {
        if (num & mask) {
          ++cnt;
        }
      }
      if (cnt >= k) {
        res |= mask;
      }
    }
    return res;
  }
};