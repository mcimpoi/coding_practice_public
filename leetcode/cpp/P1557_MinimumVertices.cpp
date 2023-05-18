/* https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes
 */
#include <iostream>
#include <vector>

class Solution {
 public:
  std::vector<int> findSmallestSetOfVertices(
      int n, const std::vector<std::vector<int>>& edges) {
    std::vector<int> result;
    std::vector<int> mask(n, 0);
    for (const auto& /* std::vector<int> */ edge : edges) {
      mask[edge[1]] = 1;
    }

    for (int v = 0; v < n; ++v) {
      if (mask[v] == 0) {
        result.push_back(v);
      }
    }
    return result;
  }
};

void print_vector(const std::vector<int>& vec) {
  for (int x : vec) {
    std::cout << x << " ";
  }
  std::cout << "\n";
}

int main(int argc, char** argv) {
  Solution s;

  std::cout << "1. Expected: ";
  print_vector({0, 3});

  std::cout << "   Actual: ";
  print_vector(
      s.findSmallestSetOfVertices(6, {{0, 1}, {0, 2}, {2, 5}, {3, 4}, {4, 2}}));

  std::cout << "2. Expected: ";
  print_vector({0, 2, 3});
  std::cout << "   Actual: ";
  print_vector(
      s.findSmallestSetOfVertices(5, {{0, 1}, {2, 1}, {3, 1}, {1, 4}, {2, 4}}));
}