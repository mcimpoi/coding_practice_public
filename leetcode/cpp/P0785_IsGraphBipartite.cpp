/* https://leetcode.com/problems/is-graph-bipartite/ */
/* Idea: color the ends of the edges in different colors.
  If two edges are the same color, the graph is not bipartite. */
#include <array>
#include <iostream>
#include <queue>
#include <vector>

class Solution {
 public:
  bool isBipartite(const std::vector<std::vector<int>>& graph) {
    std::array<int, 128> color;
    color.fill(-1);

    int first = 0;
    for (int ii = 0; ii < graph.size(); ++ii) {
      if (color[ii] != -1) {
        continue;
      }

      std::queue<int> q;
      q.push(ii);
      color[ii] = 1;

      while (!q.empty()) {
        int crt = q.front();
        q.pop();
        for (int jj : graph[crt]) {
          if (color[crt] == color[jj]) {
            return false;
          }
          if (color[jj] == -1) {
            color[jj] = 1 - color[crt];
            q.push(jj);
          }
        }
      }
    }

    return true;
  }
};

int main(int argc, char** argv) {
  Solution s;
  for (const std::vector<std::vector<int>>& testcase :
       std::vector<std::vector<std::vector<int>>>(
           {{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}},
            {{1, 3}, {0, 2}, {1, 3}, {0, 2}}})) {
    std::cout << (s.isBipartite(testcase) ? "" : "not ") << "bipartite\n";
  }
  return 0;
}