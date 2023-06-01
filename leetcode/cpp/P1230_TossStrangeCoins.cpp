/* https://leetcode.com/problems/toss-strange-coins/ */
#include <iostream>
#include <vector>

class Solution {
 public:
  double probabilityOfHeads(const std::vector<double>& prob, int target) {
    int N = static_cast<int>(prob.size());
    std::vector<std::vector<double>> dp(N + 1, std::vector<double>(N + 1, 0.0));

    dp[0][0] = 1.0;
    for (int ii = 1; ii < N + 1; ++ii) {
      dp[ii][0] = dp[ii - 1][0] * (1 - prob[ii - 1]);
    }

    for (int tt = 1; tt <= target; ++tt) {
      dp[tt][tt] = dp[tt - 1][tt - 1] * prob[tt - 1];

      for (int ii = tt + 1; ii < N + 1; ++ii) {
        dp[ii][tt] = (1 - prob[ii - 1]) * dp[ii - 1][tt] +
                     prob[ii - 1] * dp[ii - 1][tt - 1];
      }
    }
    return dp[N][target];
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << "Prob. heads for [{0.4}, 1]: " << s.probabilityOfHeads({0.4}, 1)
            << "\n";
  std::cout << "Prob. heads for [{0.5, 0.5, 0.5, 0.5, 0.5}, 0]: "
            << s.probabilityOfHeads({0.5, 0.5, 0.5, 0.5, 0.5}, 0) << "\n";
  std::cout << "Prob. heads for  [{1, 1, 1}, 3]: "
            << s.probabilityOfHeads({1.0, 1.0, 0.3}, 2) << "\n";
  return 0;
}