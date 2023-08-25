/*
DCP 1498; LC 0289: Game of Life

Conway's Game of Life takes place on an infinite two-dimensional board of square
cells. Each cell is either dead or alive, and at each tick, the following rules
apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally
adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a
starting list of live cell coordinates and the number of steps it should run
for. Once initialized, it should print out the board state at each step. Since
it's an infinite board, print out only the relevant coordinates, i.e. from the
top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot
(.).

LC Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
*/

#include <iostream>
#include <vector>

class Solution {
 public:
  // This solved the LeetCode version, i.e. grid is finite.
  void gameOfLife(std::vector<std::vector<int>>& board) {
    int nRows = static_cast<int>(board.size());
    int nCols = static_cast<int>(board[0].size());

    int dy[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dx[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int rr = 0; rr < nRows; ++rr) {
      for (int cc = 0; cc < nCols; ++cc) {
        int neighbors = 0;
        // size of dx and dy is 8.
        for (int jj = 0; jj < 8; ++jj) {
          if (inRange(rr + dy[jj], cc + dx[jj], nRows, nCols)) {
            neighbors += (board[rr + dy[jj]][cc + dx[jj]] % 2);
          }
        }

        int newval = ((board[rr][cc] % 2) == 1)
                         ? (neighbors == 2 || neighbors == 3)
                         : (neighbors == 3);
        board[rr][cc] += newval * 2;
      }
    }

    for (int rr = 0; rr < nRows; ++rr) {
      for (int cc = 0; cc < nCols; ++cc) {
        board[rr][cc] /= 2;
      }
    }
  }

  inline bool inRange(int row, int col, int nRows, int nCols) {
    bool ret_val = (0 <= row) && (row < nRows) && (0 <= col) && (col < nCols);
    return ret_val;
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::vector<std::vector<int>> board = {
      {0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
  s.gameOfLife(board);
  for (auto& row : board) {
    for (auto& val : row) {
      std::cout << val << " ";
    }
    std::cout << "\n";
  }
  return 0;
}
