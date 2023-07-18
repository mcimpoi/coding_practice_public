#include <stack>

/**
 * Definition for singly-linked list.
 */
struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

// Note: different approach from Python version.
// This one uses stacks to store list elements in reversed order.
// Time: O(n); Space: O(n)
class Solution {
 public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    std::stack<int> st1;
    std::stack<int> st2;

    ListNode* h1 = l1;
    while (h1) {
      st1.push(h1->val);
      h1 = h1->next;
    }

    ListNode* h2 = l2;
    while (h2) {
      st2.push(h2->val);
      h2 = h2->next;
    }

    int max_elems = std::max(st1.size(), st2.size());
    ListNode* result_head = nullptr;
    int carry = 0;
    for (int ii = 0; ii < max_elems; ++ii) {
      int el1 = 0;
      if (!st1.empty()) {
        el1 = st1.top();
        st1.pop();
      }

      int el2 = 0;
      if (!st2.empty()) {
        el2 = st2.top();
        st2.pop();
      }

      int crt = el1 + el2 + carry;
      carry = crt / 10;
      crt %= 10;

      ListNode* newhead = new ListNode(crt);
      newhead->next = result_head;
      result_head = newhead;
    }

    if (carry == 1) {
      ListNode* newhead = new ListNode(1);
      newhead->next = result_head;
      result_head = newhead;
    }

    return result_head;
  }
};