// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

class Solution {
 public:
  int minSpeedOnTime(const std::vector<int>& dist, double hour) {
    int n = static_cast<int>(dist.size());

    if (hour <= n - 1) {
      return -1;
    }

    int left = 1;
    int max_elem = *std::max_element(dist.begin(), dist.end());
    int right =
        1 + std::max(max_elem,
                     static_cast<int>(floor(static_cast<double>(dist.back()) /
                                            (hour - n + 1))));

    int res = -1;

    while (left <= right) {
      int mid = (left + right) / 2;
      double crt_time = 0.0;

      for (int idx = 0; idx < n - 1; ++idx) {
        crt_time += ceil(dist[idx] / static_cast<double>(mid));
      }
      crt_time += static_cast<double>(dist.back()) / mid;

      if (crt_time <= hour) {
        res = mid;
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
    return res;
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << "Input: {1, 3, 2}, 6\n Result: "
            << s.minSpeedOnTime({1, 3, 2}, 6.0) << "\n Expected : 1\n";
  return 0;
}