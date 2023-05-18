/* https://leetcode.com/problems/number-of-islands */

// Assume we are allowed to modify the grid.

#include <iostream>
#include <queue>
#include <string>
#include <utility>
#include <vector>

using namespace std;

class Solution {
 public:
  int numIslands(vector<vector<char>>& grid) {
    int dim_1 = grid.size();
    int dim_2;
    if (grid.size() == 0) {
      return 0;
    }
    dim_2 = grid[0].size();
    int num_islands = 0;
    for (int ii = 0; ii < dim_1; ++ii) {
      for (int jj = 0; jj < dim_2; ++jj) {
        // DFS only from visited
        if (grid[ii][jj] == '1') {
          ++num_islands;
          queue<pair<int, int>> q;
          q.push(make_pair(ii, jj));
          while (q.size() > 0) {
            pair<int, int> crt = q.front();
            q.pop();
            int x = crt.first;
            int y = crt.second;

            if (x > 0 && grid[x - 1][y] == '1') {
              q.push(make_pair(x - 1, y));
              grid[x - 1][y] = 'X';
            }
            if (y > 0 && grid[x][y - 1] == '1') {
              q.push(make_pair(x, y - 1));
              grid[x][y - 1] = 'X';
            }
            if (x < dim_1 - 1 && grid[x + 1][y] == '1') {
              q.push(make_pair(x + 1, y));
              grid[x + 1][y] = 'X';
            }
            if (y < dim_2 - 1 && grid[x][y + 1] == '1') {
              q.push(make_pair(x, y + 1));
              grid[x][y + 1] = 'X';
            }
          }
        }
      }
    }
    return num_islands;
  }
};

int main(int argc, char** argv) {
  Solution s;
  vector<vector<char>> grid;
  //  grid = {"11110","11010","11000","00000"};
  vector<string> tmpbuf;
  tmpbuf.push_back("11111011111111101011");
  tmpbuf.push_back("01111111111110111110");
  tmpbuf.push_back("10111001101111111111");
  tmpbuf.push_back("11110111111111111111");
  tmpbuf.push_back("10011111111111111111");
  tmpbuf.push_back("10111111011101110111");
  tmpbuf.push_back("01111111111101101111");
  tmpbuf.push_back("11111111111101111011");
  tmpbuf.push_back("11111111110111111111");
  for (int ii = 0; ii < tmpbuf.size(); ++ii) {
    vector<char> tmp;
    for (int jj = 0; jj < tmpbuf[ii].size(); ++jj) {
      tmp.push_back(tmpbuf[ii][jj]);
    }
    grid.push_back(tmp);
  }

  int result = s.numIslands(grid);
  cout << result << "\n";
}
