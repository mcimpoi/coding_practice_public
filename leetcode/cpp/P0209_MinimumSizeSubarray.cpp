/* https://leetcode.com/problems/minimum-size-subarray-sum */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

class Solution {
 public:
  int minSubArrayLen(int target, const std::vector<int>& nums) {
    // Looks like good candidate for sliding window approach
    // subarray -- continuous

    // start at beginning of array; keep 2 "pointers", left and right;
    // while the current sum is less than target, keep moving right pointer
    // and add to the current sum;
    // otherwise, move the left pointer;
    // keep min distance; need to do this every time we update left, if crt_sum
    // >= target.

    int arr_size_plus_one = static_cast<int>(nums.size()) + 1;
    int min_size = static_cast<int>(nums.size()) + 1;

    int left = 0;
    int right = 0;

    int crt_sum = 0;
    while (right < nums.size()) {
      while (right < nums.size() && crt_sum < target) {
        crt_sum += nums[right];
        ++right;
      }
      if (crt_sum >= target) {
        min_size = std::min(min_size, right - left);
      }

      while (left < right && crt_sum >= target) {
        crt_sum -= nums[left];
        ++left;
        if (crt_sum >= target) {
          min_size = std::min(min_size, right - left);
        }
      }
    }

    return min_size % arr_size_plus_one;
  }
};

std::string vec2str(const std::vector<int>& vec) {
  std::string res = "[";
  for (int x : vec) {
    res += std::to_string(x) + ", ";
  }
  res += "]";
  return res;
}

int main(int argc, char** argv) {
  const std::vector<std::vector<int>> testcase_arrays(
      {{2, 3, 1, 2, 4, 3}, {1, 4, 4}, {1, 1, 1, 1, 1, 1, 1, 1}});
  const std::vector<int> testcase_targets({7, 4, 11});
  const std::vector<int> testcase_results({2, 1, 0});

  Solution s;

  for (size_t test = 0; test < testcase_arrays.size(); ++test) {
    int actual =
        s.minSubArrayLen(testcase_targets[test], testcase_arrays[test]);
    std::cout << "Test case " << test << " with target "
              << testcase_targets[test] << " and array "
              << vec2str(testcase_arrays[test]) << "\nResult: " << actual
              << " Expected: " << testcase_results[test] << "\n--\n";
  }
  return 0;
};