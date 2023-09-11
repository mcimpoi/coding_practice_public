// https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

#include <unordered_map>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> groupThePeople(std::vector<int>& groupSizes) {
    std::unordered_map<int, std::vector<int>> crt;
    std::vector<std::vector<int>> solution;

    for (int id = 0; id < groupSizes.size(); ++id) {
      int crtSize = groupSizes[id];

      if (crt[crtSize].size() < crtSize) {
        crt[crtSize].push_back(id);
      }

      if (crt[crtSize].size() == crtSize) {
        solution.push_back(crt[crtSize]);
        crt[crtSize] = std::vector<int>();
      }
    }
    return solution;
  }
};