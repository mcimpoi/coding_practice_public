// https://leetcode.com/problems/combinations/

#include <iostream>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> combine(int n, int k) {
    std::vector<std::vector<int>> result;
    std::vector<int> crt_vec(k, 0);
    backtrack(n, k, 0, 1, crt_vec, result);
    return result;
  }

  void backtrack(int n, int k, int crt, int val, std::vector<int>& crt_vec,
                 std::vector<std::vector<int>>& result) {
    if (crt >= k) {
      result.push_back(crt_vec);
      return;
    }

    for (int ii = val; ii <= n; ++ii) {
      crt_vec[crt] = ii;
      backtrack(n, k, crt + 1, ii + 1, crt_vec, result);
    }
  }
};

int main(int argc, char** argv) {
  Solution solution;
  std::vector<std::vector<int>> result = solution.combine(4, 2);

  for (const auto& vec : result) {
    for (const auto& val : vec) {
      std::cout << val << " ";
    }
    std::cout << std::endl;
  }

  return 0;
}