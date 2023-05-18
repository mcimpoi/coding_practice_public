/*  https://leetcode.com/problems/maximum-number-of-moves-in-a-grid */

#include <iostream>
#include <queue>
#include <utility>
#include <vector>

class Solution {
 public:
  int maxMoves(const std::vector<std::vector<int>>& grid) {
    const int nRows = static_cast<int>(grid.size());
    const int nCols = static_cast<int>(grid[0].size());

    int max_moves = 0;
    std::vector<std::vector<int>> moves(nRows, std::vector<int>(nCols, 0));

    std::queue<std::pair<int, int>> q;
    for (int row = 0; row < nRows; ++row) {
      q.push(std::make_pair(row, 0));
    }

    while (!q.empty()) {
      auto crt = q.front();
      q.pop();

      int crt_row = crt.first;
      int crt_col = crt.second;

      if (crt_col + 1 >= nCols) {
        continue;
      }
      for (int dr = -1; dr <= 1; ++dr) {
        int next_row = crt_row + dr;
        int next_col = crt_col + 1;

        if (next_row < 0 || next_row >= nRows) {
          continue;
        }
        if (grid[next_row][next_col] > grid[crt_row][crt_col] &&
            moves[crt_row][crt_col] + 1 > moves[next_row][next_col]) {
          moves[next_row][next_col] = moves[crt_row][crt_col] + 1;
          q.push(std::make_pair(next_row, next_col));
          max_moves = std::max(max_moves, moves[next_row][next_col]);
        }
      }
    }

    return max_moves;
  }
};

int main(int argc, char** argv) {
  Solution s;

  std::cout << "1. Expected: 3. Returned: "
            << s.maxMoves(
                   {{2, 4, 3, 5}, {5, 4, 9, 3}, {3, 4, 2, 11}, {10, 9, 13, 15}})
            << "\n";

  std::cout << "2. Expected: 0. Returned: "
            << s.maxMoves({{3, 2, 4}, {2, 1, 9}, {1, 1, 7}}) << "\n";
}