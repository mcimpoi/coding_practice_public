#include <limits.h>

#include <iostream>
#include <queue>
#include <utility>
#include <vector>

class Solution {
 public:
  int shortestPathBinaryMatrix(const std::vector<std::vector<int>>& grid) {
    int nRows = grid.size();
    int nCols = grid[0].size();

    if (grid[0][0] == 1) {
      return -1;
    }
    if (grid[nRows - 1][nCols - 1] == 1) {
      return -1;
    }

    std::queue<std::pair<int, int>> q;
    std::vector<std::vector<int>> dist(128, std::vector<int>(128, INT_MAX));

    q.push(std::make_pair(0, 0));
    dist[0][0] = 1;

    while (!q.empty()) {
      std::pair<int, int> crt = q.front();
      q.pop();

      for (int dr = -1; dr <= 1; ++dr) {
        for (int dc = -1; dc <= 1; ++dc) {
          if (dc == 0 && dr == 0) {
            continue;
          }
          int nextR = crt.first + dr;
          int nextC = crt.second + dc;

          if (nextR >= 0 && nextR < nRows && nextC >= 0 && nextC < nCols &&
              grid[nextR][nextC] == 0) {
            if (dist[nextR][nextC] > dist[crt.first][crt.second] + 1) {
              dist[nextR][nextC] = dist[crt.first][crt.second] + 1;
              q.push(std::make_pair(nextR, nextC));
            }
          }
        }
      }
    }

    if (dist[nRows - 1][nCols - 1] == INT_MAX) {
      return -1;
    }
    return dist[nRows - 1][nCols - 1];
  }
};

int main(int argc, char** argv) {
  Solution s;

  std::cout << "1. Expected: 4. Returned: "
            << s.shortestPathBinaryMatrix({{0, 0, 0}, {1, 1, 0}, {1, 1, 0}})
            << "\n";

  std::cout << "2. Expected: -1. Returned: "
            << s.shortestPathBinaryMatrix({{1, 0, 0}, {1, 1, 0}, {1, 1, 0}})
            << "\n";
  return 0;
}