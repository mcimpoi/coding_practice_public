// https://leetcode.com/problems/unique-paths-ii/
// https://leetcode.com/problems/unique-paths-ii

#include <array>
#include <iostream>
#include <vector>

class Solution {
 public:
  int uniquePathsWithObstacles(
      const std::vector<std::vector<int>>& obstacleGrid) {
    int n_rows = obstacleGrid.size();
    int n_cols = obstacleGrid[0].size();

    // can preallocate, because grid is small
    // and we don't need the overhead from vector.
    std::array<std::array<int, 128>, 128> ways;
    for (int row = 0; row < n_rows; ++row) {
      ways[row].fill(0);
    }

    for (int row = 0; row < n_rows; ++row) {
      for (int col = 0; col < n_cols; ++col) {
        if (row == 0 && col == 0) {
          ways[row][col] = 1;
        } else {
          if (col > 0) {
            ways[row][col] += ways[row][col - 1];
          }
          if (row > 0) {
            ways[row][col] += ways[row - 1][col];
          }
        }
        ways[row][col] *= (1 - obstacleGrid[row][col]);
      }
    }

    return ways[n_rows - 1][n_cols - 1];
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << s.uniquePathsWithObstacles({{0, 0, 0}, {0, 1, 0}, {0, 0, 0}})
            << std::endl;
  return 0;
}