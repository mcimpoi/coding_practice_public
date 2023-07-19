// https://leetcode.com/problems/asteroid-collision/

#include <algorithm>
#include <cmath>
#include <stack>
#include <vector>

class Solution {
 public:
  std::vector<int> asteroidCollision(std::vector<int>& asteroids) {
    std::stack<int> st;

    for (int x : asteroids) {
      int crt = x;
      bool both_explode = false;
      while (!st.empty()) {
        int top = st.top();
        both_explode = false;
        if (top > 0 && crt == -top) {
          both_explode = true;
          st.pop();
          break;
        } else {
          if (top < 0 || crt > 0) {
            break;
          }
        }

        // collision
        if (crt < 0 && top > 0) {
          st.pop();
          if (std::abs(crt) < std::abs(top)) {
            crt = top;
          }
        }
      }
      if (!both_explode) {
        st.push(crt);
      }
    }

    std::vector<int> result;
    while (!st.empty()) {
      int crt = st.top();
      result.push_back(crt);
      st.pop();
    }
    std::reverse(result.begin(), result.end());
    return result;
  }
};