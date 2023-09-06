// https://leetcode.com/problems/split-linked-list-in-parts/

#include <iostream>
#include <vector>

struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
 public:
  std::vector<ListNode*> splitListToParts(ListNode* head, int k) {
    ListNode* h_ = head;
    int listLen = 0;
    while (h_ != nullptr) {
      ++listLen;
      h_ = h_->next;
    }

    std::vector<ListNode*> result;

    h_ = head;
    ListNode* prev = nullptr;
    for (int kk = 0; kk < k; ++kk) {
      int segLen = (listLen / k) + (kk < (listLen % k));
      result.push_back(h_);
      for (int jj = 0; jj < segLen; ++jj) {
        if (h_ != nullptr) {
          prev = h_;
          h_ = h_->next;
        }
      }
      if (prev != nullptr) {
        h_ = prev->next;
        prev->next = nullptr;
        prev = nullptr;
      }
    }
    return result;
  }
};

int main(int argc, char** argv) {
  Solution s;
  s.splitListToParts(nullptr, 3);
  s.splitListToParts(new ListNode(1, new ListNode(2, new ListNode(3))), 5);
  return 0;
}