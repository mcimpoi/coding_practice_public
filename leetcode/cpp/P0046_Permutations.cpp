// https://leetcode.com/problems/permutations/

#include <iostream>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> permute(const std::vector<int>& nums) {
    std::vector<std::vector<int>> result;
    std::vector<int> buffer;
    backtrack(0, nums, buffer, result);
    return result;
  }

  void backtrack(int crt_idx, const std::vector<int>& nums,
                 std::vector<int>& buffer,
                 std::vector<std::vector<int>>& result) {
    if (crt_idx == nums.size()) {
      if (buffer.size() == nums.size()) {
        std::vector<int> solution;
        for (int idx : buffer) {
          solution.push_back(nums[idx]);
        }
        result.push_back(solution);
      }
    }
    for (int idx = 0; idx < nums.size(); ++idx) {
      bool found = false;
      for (int j : buffer) {
        if (j == idx) {
          found = true;
          break;
        }
      }
      if (found) {
        continue;
      }
      buffer.push_back(idx);
      backtrack(crt_idx + 1, nums, buffer, result);
      buffer.pop_back();
    }
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << "Test 1: " << std::endl;
  std::vector<int> nums1 = {1, 2, 3};
  std::vector<std::vector<int>> result1 = s.permute(nums1);

  for (const auto& vec : result1) {
    for (const auto& val : vec) {
      std::cout << val << " ";
    }
    std::cout << std::endl;
  }
  return 0;
}