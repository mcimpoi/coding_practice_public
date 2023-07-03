#include <string>
#include <unordered_map>
#include <vector>

class Solution {
 public:
  bool buddyStrings(const std::string &A, const std::string &B) {
    if (A.length() != B.length()) {
      return false;
    }

    std::vector<int> distinct;

    for (int ii = 0; ii < A.length(); ++ii) {
      if (A[ii] != B[ii]) {
        distinct.push_back(ii);
        if (distinct.size() >= 3) {
          return false;
        }
      }
    }

    if (distinct.size() == 1) {
      return false;
    }

    if (distinct.size() == 0) {
      std::unordered_map<char, int> freq;
      for (char x : A) {
        ++freq[x];
        if (freq[x] >= 2) {
          return true;
        }
      }
      return false;
    }

    if (distinct.size() == 2) {
      return (A[distinct[0]] == B[distinct[1]] &&
              A[distinct[1]] == B[distinct[0]]);
    }

    return false;
  }
};

// TODO : Add main + basic test cases.
