// https://leetcode.com/problems/candy-crush/

#include <iomanip>
#include <iostream>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> candyCrush(
      const std::vector<std::vector<int>>& board) {
    /*
        - board is small less than (50 x 50)
        - one pass: find items in row / column which could be removed.
        - make them negative

        - for each column, use 2 pointers (one read, one write), to
        - simulate moving down;

        - it's easier to work on transpose of board; return transposed
        - return transpose of working matrix (O(n^2) space, but n is small)
     */

    std::vector<std::vector<int>> grid = transpose(board);

    bool dirty = true;
    int steps = 0;
    while (dirty) {
      dirty = mark_for_removal(grid);
      steps += 1;

      if (dirty) {
        compress_grid(grid);
      }
    }
    return transpose(grid);
  }

  void print_grid(const std::vector<std::vector<int>>& grid) {
    for (int r = 0; r < grid.size(); ++r) {
      for (int c = 0; c < grid[0].size(); ++c) {
        std::cout << std::setfill(' ') << std::setw(5) << grid[r][c];
      }
      std::cout << std::endl;
    }
  }

  std::vector<std::vector<int>> transpose(
      const std::vector<std::vector<int>>& grid_in) {
    // assume it has at least one row and one col;
    int n_rows = grid_in.size();
    int n_cols = grid_in[0].size();
    std::vector<std::vector<int>> res(n_cols, std::vector<int>(n_rows, 0));
    for (int r = 0; r < n_rows; ++r) {
      for (int c = 0; c < n_cols; ++c) {
        res[c][r] = grid_in[r][c];
      }
    }
    return res;
  }

  bool mark_for_removal(std::vector<std::vector<int>>& grid) {
    // we look for 3 or more consecutive items in a row or column
    // and swap these to the negative value;
    // we ignore 0s - because those are empty cells;
    // we keep comparing with abs value, because the same candy might
    // be on both row and column

    int n_rows = grid.size();
    int n_cols = grid[0].size();
    bool dirty = false;

    for (int r = 0; r < n_rows; ++r) {
      for (int c = 0; c < n_cols; ++c) {
        if (grid[r][c] == 0) {
          continue;
        }

        int next_row = r;
        while (next_row < n_rows && abs(grid[r][c]) == abs(grid[next_row][c])) {
          ++next_row;
        }
        if (next_row - r >= 3) {
          dirty = true;
          for (int r_ = r; r_ < next_row; ++r_) {
            grid[r_][c] = -abs(grid[r_][c]);
          }
        }

        int next_col = c;
        while (next_col < n_cols && abs(grid[r][c]) == abs(grid[r][next_col])) {
          ++next_col;
        }
        if (next_col - c >= 3) {
          dirty = true;
          for (int c_ = c; c_ < next_col; ++c_) {
            grid[r][c_] = -abs(grid[r][c]);
          }
        }
      }
    }
    return dirty;
  }

  void compress_grid(std::vector<std::vector<int>>& grid) {
    // use two pointers, one read, one write
    // to remove the negative values, slide the positive ones
    // and fill the rest with 0s.
    int n_rows = grid.size();
    int n_cols = grid[0].size();
    for (int r = 0; r < n_rows; ++r) {
      int write_col = n_cols - 1;
      int read_col = n_cols - 1;

      while (read_col >= 0) {
        if (grid[r][read_col] > 0) {
          grid[r][write_col] = grid[r][read_col];
          --read_col;
          --write_col;
        } else {
          --read_col;
        }
      }
      for (int c = write_col; c >= 0; --c) {
        grid[r][c] = 0;
      }
    }
  }
};

int main(int argc, char** argv) {
  Solution sol;
  const std::vector<std::vector<int>> input_grid = {
      {110, 5, 112, 113, 114}, {210, 211, 5, 213, 214}, {310, 311, 3, 313, 314},
      {410, 411, 412, 5, 414}, {5, 1, 512, 3, 3},       {610, 4, 1, 613, 614},
      {710, 1, 2, 713, 714},   {810, 1, 2, 1, 1},       {1, 1, 2, 2, 2},
      {4, 1, 4, 4, 1014}};
  const auto result = sol.candyCrush(input_grid);

  std::cout << "Input grid:\n";
  sol.print_grid(input_grid);
  std::cout << "Result grid:\n";
  sol.print_grid(result);

  return 0;
}