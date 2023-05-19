/* https://leetcode.com/problems/combination-sum-ii */
#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> combinationSum2(
      const std::vector<int>& candidates, int target) {
    std::vector<std::vector<int>> result;
    if (candidates.size() == 0) {
      return {{}};
    }
    std::vector<int> sorted_candidates(candidates);
    std::sort(sorted_candidates.begin(), sorted_candidates.end());

    std::vector<int> mask(candidates.size(), 0);
    findCombinations(sorted_candidates, target, 0, mask, result);
    return result;
  }

  inline void findCombinations(const std::vector<int>& candidates, int target,
                               int index, std::vector<int>& mask,
                               std::vector<std::vector<int>>& results) {
    if (target < 0) {
      return;
    }
    if (target == 0) {
      std::vector<int> sol;
      for (int jj = 0; jj < candidates.size(); ++jj) {
        if (mask[jj] == 1) {
          sol.push_back(candidates[jj]);
        }
      }

      results.emplace_back(sol);
    }

    for (int ii = index; ii < candidates.size(); ++ii) {
      if (target - candidates[ii] < 0) {
        break;
      }
      if (ii > index && candidates[ii] == candidates[ii - 1]) {
        continue;
      }
      if (mask[ii] == 0) {
        mask[ii] = 1;
        findCombinations(candidates, target - candidates[ii], ii + 1, mask,
                         results);
        mask[ii] = 0;
      }
    }
  }
};

void print_vec(const std::vector<int>& vec) {
  for (int x : vec) {
    std::cout << x << " ";
  }
  std::cout << "\n";
}

int main(int argc, char** argv) {
  Solution s;
  std::vector<std::vector<int>> result =
      s.combinationSum2({10, 1, 2, 7, 6, 1, 5}, 8);
  for (const auto& vec : result) {
    print_vec(vec);
  }
}