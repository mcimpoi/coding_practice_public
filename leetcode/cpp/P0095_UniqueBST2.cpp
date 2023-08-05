// https://leetcode.com/problems/unique-binary-search-trees-ii/

#include <iostream>
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
  std::vector<TreeNode *> generateTrees(int n) { return build(1, n); }

  std::vector<TreeNode *> build(int start, int end) {
    if (start > end) {
      return {nullptr};
    }
    if (start == end) {
      return {new TreeNode(start)};
    }

    std::vector<TreeNode *> res;

    for (int ii = start; ii <= end; ++ii) {
      std::vector<TreeNode *> left = build(start, ii - 1);
      std::vector<TreeNode *> right = build(ii + 1, end);

      for (auto l : left) {
        for (auto r : right) {
          TreeNode *crt = new TreeNode(ii, l, r);
          res.push_back(crt);
        }
      }
    }
    return res;
  }
};

void print_tree(TreeNode *t) {
  if (t == nullptr) {
    return;
  }
  std::cout << t->val << " ";
  print_tree(t->left);
  print_tree(t->right);
}

int main(int argc, char **argv) {
  Solution s;
  std::vector<TreeNode *> results = s.generateTrees(3);
  for (int ii = 0; ii < results.size(); ++ii) {
    std::cout << "Tree " << ii << std::endl;
    print_tree(results[ii]);
    std::cout << "\n===\n";
  }
  return 0;
}