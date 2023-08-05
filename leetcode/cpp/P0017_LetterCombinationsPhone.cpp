// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
 public:
  std::vector<std::string> letterCombinations(const std::string& digits) {
    std::unordered_map<char, std::string> kbd;
    kbd['2'] = "abc";
    kbd['3'] = "def";
    kbd['4'] = "ghi";
    kbd['5'] = "jkl";
    kbd['6'] = "mno";
    kbd['7'] = "pqrs";
    kbd['8'] = "tuv";
    kbd['9'] = "wxyz";

    if (digits.length() == 0) {
      return std::vector<std::string>();
    }
    if (digits.length() == 1) {
      std::vector<std::string> results;
      for (int ii = 0; ii < kbd[digits[0]].length(); ++ii) {
        std::stringstream ss;
        ss << kbd[digits[0]][ii];
        results.push_back(ss.str());
      }
      return results;
    }

    std::vector<std::string> results;
    std::vector<std::string> prev_results =
        letterCombinations(digits.substr(1));
    results.reserve(prev_results.size() * 4);
    for (int ii = 0; ii < kbd[digits[0]].length(); ++ii) {
      for (int jj = 0; jj < prev_results.size(); ++jj) {
        std::stringstream ss;
        ss << kbd[digits[0]][ii] << prev_results[jj];
        results.push_back(ss.str());
      }
    }
    return results;
  }
};

int main(int argc, char** argv) {
  Solution s;
  std::vector<std::string> results = s.letterCombinations("23");
  for (int ii = 0; ii < results.size(); ++ii) {
    std::cout << results[ii] << std::endl;
  }
  return 0;
}