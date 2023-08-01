// https://leetcode.com/problems/greatest-common-divisor-of-strings/

#include <algorithm>
#include <iostream>
#include <iterator>
#include <ostream>
#include <sstream>
#include <string>

class Solution {
 public:
  std::string bruteForce(const std::string& str1, const std::string& str2) {
    int candidateLength = 0;

    for (int i = 1; i <= std::min(str1.length(), str2.length()); ++i) {
      if ((str1.length() % i != 0) || (str2.length() % i != 0)) {
        continue;
      }
      std::ostringstream repeated;
      int numRepeats = (str1.length() + str2.length()) / i;
      std::fill_n(std::ostream_iterator<std::string>(repeated), numRepeats,
                  str1.substr(0, i));
      if (str1 + str2 == repeated.str()) {
        candidateLength = i;
      }
    }
    return str1.substr(0, candidateLength);
  }

  std::string gcdOfStrings(const std::string& str1, const std::string& str2) {
    if (str1 + str2 != str2 + str1) {
      return "";
    }

    int targetLen = gcd(str1.length(), str2.length());

    std::ostringstream repeated;
    int numRepeats = (str1.length() + str2.length()) / targetLen;
    std::fill_n(std::ostream_iterator<std::string>(repeated), numRepeats,
                str1.substr(0, targetLen));
    if (str1 + str2 == repeated.str()) {
      return str1.substr(0, targetLen);
    }

    return "";
  }

  int gcd(int a, int b) {
    if (a == 0 || b == 0) {
      return a + b;
    }
    return gcd(std::max(a, b) % std::min(a, b), std::min(a, b));
  }
};

int main(int argc, char** argv) {
  Solution solution;
  std::cout << "Returned: " << solution.gcdOfStrings("ABCABC", "ABC") << " "
            << " Expected: ABC" << std::endl;
  return 0;
}