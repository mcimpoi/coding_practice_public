// https://leetcode.com/problems/rearrange-string-k-distance-apart/

#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>

class Solution {
 public:
  std::string rearrangeString(std::string s, int k) {
    std::unordered_map<char, int> frequency;
    for (char ch : s) {
      frequency[ch] += 1;
    }

    std::unordered_map<char, int> prev_idx;
    std::priority_queue<std::pair<int, char>> pq;
    for (const auto& [ch, f] : frequency) {
      pq.push(std::make_pair(f, ch));
      prev_idx[ch] = -k;
    }

    std::string result = "";
    std::queue<std::pair<int, char>> buffer;
    for (int crt_idx = 0; crt_idx < s.length(); ++crt_idx) {
      bool ok = false;
      int count = -1;
      char ch = '*';
      while (pq.size() > 0) {
        std::pair<int, char> crt = pq.top();

        pq.pop();
        if (crt_idx - prev_idx[crt.second] >= k) {
          result += crt.second;
          prev_idx[crt.second] = crt_idx;
          ok = true;
          count = crt.first - 1;
          ch = crt.second;
          break;
        } else {
          buffer.push(crt);
        }
      }

      if (!ok) {
        return "";
      }

      if (count > 0) {
        pq.push(std::make_pair(count, ch));
      }
      // TODO: keep track of queue size.
      while (buffer.size() > 0) {
        pq.push(buffer.front());
        buffer.pop();
      }
    }

    return result;
  }
};

int main(int argc, char** argv) {
  // Note: solutions are not necessarily unique.
  Solution s;
  std::cout << "Example: aabbcc, 3 "
            << "Expected: "
            << "abcabc "
            << "Actual: " << s.rearrangeString("aabbcc", 3) << std::endl;
  return 0;
}