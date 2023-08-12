// https://leetcode.com/problems/unique-paths/

#include <array>
#include <iostream>

class Solution {
 public:
  int uniquePaths(int m, int n) {
    std::array<std::array<int, 128>, 128> dp;
    for (int row = 0; row < m; ++row) {
      dp[row].fill(1);
    }

    for (int ii = 1; ii < m; ++ii) {
      for (int jj = 1; jj < n; ++jj) {
        dp[ii][jj] = dp[ii - 1][jj] + dp[ii][jj - 1];
      }
    }
    return dp[m - 1][n - 1];
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << s.uniquePaths(3, 7) << std::endl;
  return 0;
}