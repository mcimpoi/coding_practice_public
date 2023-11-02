// https://leetcode.com/problems/find-mode-in-binary-search-tree/

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode* left, TreeNode* right)
      : val(x), left(left), right(right) {}
};

#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
 public:
  std::vector<int> findMode(TreeNode* root) {
    // keep a map for values, freq;
    // keep a counter of number of nodes in tree
    // can have 1 or 2 modes;
    std::vector<int> result;
    std::unordered_map<int, int> freq;
    int total_nodes = 0;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
      TreeNode* crt = q.front();
      q.pop();
      ++freq[crt->val];
      ++total_nodes;
      if (crt->left != nullptr) {
        q.push(crt->left);
      }
      if (crt->right != nullptr) {
        q.push(crt->right);
      }
    }
    auto max_el = std::max_element(
        freq.begin(), freq.end(),
        [](const auto& a, const auto& b) { return a.second < b.second; });

    for (const auto& x : freq) {
      if (x.second == max_el->second) {
        result.push_back(x.first);
      }
    }
    return result;
  }
};

int main(int argc, char** argv) {
  Solution s;
  TreeNode* root = new TreeNode(1);
  root->right = new TreeNode(2);
  root->right->left = new TreeNode(2);
  auto result = s.findMode(root);
  for (auto& x : result) {
    std::cout << x << " ";
  }
  std::cout << "Expected: 2" << std::endl;
}