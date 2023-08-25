// https://leetcode.com/problems/interleaving-string/

#include <iostream>
#include <string>
#include <vector>

class Solution {
 public:
  bool isInterleave(const std::string& s1, const std::string& s2,
                    const std::string& s3) {
    if (s1.length() + s2.length() != s3.length()) {
      return false;
    }

    std::vector<std::vector<int>> dp(s1.length() + 1,
                                     std::vector<int>(s2.length() + 1, 0));

    for (int ii = 0; ii <= s1.length(); ++ii) {
      for (int jj = 0; jj <= s2.length(); ++jj) {
        if (ii == 0 && jj == 0) {
          dp[ii][jj] = 1;
        } else if (ii == 0) {
          dp[ii][jj] = dp[ii][jj - 1] && s2[jj - 1] == s3[ii + jj - 1];
        } else if (jj == 0) {
          dp[ii][jj] = dp[ii - 1][jj] && s1[ii - 1] == s3[ii + jj - 1];
        } else {
          dp[ii][jj] = (dp[ii - 1][jj] && s1[ii - 1] == s3[ii + jj - 1]) ||
                       (dp[ii][jj - 1] && s2[jj - 1] == s3[ii + jj - 1]);
        }
        // cout << dp[ii][jj] << " ";
      }
      // cout << "\n";
    }
    return dp[s1.length()][s2.length()] == 1;
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::cout << s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
            << " Expected: 1.\n";
  std::cout << s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
            << " Expected: 0.\n";
  return 0;
}