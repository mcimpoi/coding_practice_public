// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
 public:
  /*
  Use helper function, to keep track of sum and count of nodes in
  subtree;
  Traverse the tree (e.g. using queue, it does not matter)
  might not need to
  */
  int averageOfSubtree(TreeNode *root) {
    int res = 0;
    sumAndCount(root, res);
    return res;
  }

  std::pair<int, int> sumAndCount(TreeNode *root, int &res) {
    if (root == nullptr) {
      return std::make_pair(0, 0);
    }
    std::pair<int, int> left = sumAndCount(root->left, res);
    std::pair<int, int> right = sumAndCount(root->right, res);
    int crt_sum = std::get<0>(left) + std::get<0>(right) + root->val;
    int crt_count = std::get<1>(left) + std::get<1>(right) + 1;
    if (root->val == crt_sum / crt_count) {
      res += 1;
    }
    return std::make_pair(crt_sum, crt_count);
  }
};

int main() {
  Solution s;
  TreeNode *root = new TreeNode(2);
  root->left = new TreeNode(3);
  root->right = new TreeNode(1);
  root->left->left = new TreeNode(3);
  root->left->right = new TreeNode(1);
  root->right->left = new TreeNode(1);
  root->right->right = new TreeNode(3);
  int result = s.averageOfSubtree(root);
  std::cout << "Expected: 6 "
            << "Actual: " << result << std::endl;
  return 0;
}