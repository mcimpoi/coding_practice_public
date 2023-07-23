// https://leetcode.com/problems/all-possible-full-binary-trees/

#include <vector>

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode* left, TreeNode* right)
      : val(x), left(left), right(right) {}
};

class Solution {
 public:
  std::vector<TreeNode*> allPossibleFBT(int N) {
    std::vector<TreeNode*> roots;
    if (0 == N % 2) {
      return roots;
    }
    if (N == 1) {
      TreeNode* root = new TreeNode(0);
      roots.push_back(root);
      return roots;
    }

    for (int ii = 1; ii < N; ii += 2) {
      // TODO: cache these, don't need to recompute evety time.
      std::vector<TreeNode*> lefts = allPossibleFBT(ii);
      std::vector<TreeNode*> rights = allPossibleFBT(N - ii - 1);

      for (TreeNode* l : lefts) {
        for (TreeNode* r : rights) {
          TreeNode* root = new TreeNode(0);
          root->left = l;
          root->right = r;
          roots.push_back(root);
        }
      }
    }
    return roots;
  }
};