// https://leetcode.com/problems/coin-change-2/
#include <array>
#include <iostream>
// https://leetcode.com/problems/coin-change-2/
#include <vector>

class Solution {
 public:
  int change(int amount, const std::vector<int>& coins) {
    std::array<int, 5120> s;
    s.fill(0);
    s[0] = 1;

    for (int cc = 0; cc < coins.size(); ++cc) {
      for (int ii = coins[cc]; ii <= amount; ++ii) {
        s[ii] += s[ii - coins[cc]];
      }
    }

    return s[amount];
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << "Input: (5, {1, 2, 5}) Expected output: 4\n Actual: "
            << s.change(5, {1, 2, 5}) << std::endl;
  return 0;
}