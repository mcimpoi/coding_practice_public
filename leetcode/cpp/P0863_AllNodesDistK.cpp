// Definition for a binary tree node.
#include <array>
#include <iostream>
#include <queue>
#include <vector>

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
 public:
  std::vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
    // get adjacency list

    std::vector<int> result;
    if (root == nullptr || target == nullptr) {
      return result;
    }

    // convert to graph
    std::vector<std::vector<int>> adj(512, std::vector<int>());
    std::queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
      TreeNode* crt = q.front();
      q.pop();
      if (crt->left != nullptr) {
        adj[crt->left->val].push_back(crt->val);
        adj[crt->val].push_back(crt->left->val);
        q.push(crt->left);
      }
      if (crt->right != nullptr) {
        adj[crt->right->val].push_back(crt->val);
        adj[crt->val].push_back(crt->right->val);
        q.push(crt->right);
      }
    }

    std::array<int, 512> visited;
    visited.fill(0);

    std::queue<std::pair<int, int>> q2;
    q2.push(std::make_pair(target->val, 0));
    visited[target->val] = 1;

    while (!q2.empty()) {
      auto crt = q2.front();
      q2.pop();
      if (crt.second == k) {
        result.push_back(crt.first);
      } else {
        for (int neighbor : adj[crt.first]) {
          if (!visited[neighbor]) {
            q2.push(std::make_pair(neighbor, crt.second + 1));

            visited[neighbor] = 1;
          }
        }
      }
    }

    return result;
  }
};

TreeNode* build_testcase1() {
  TreeNode* root = new TreeNode(3);
  root->left = new TreeNode(5);
  root->right = new TreeNode(1);
  root->left->left = new TreeNode(6);
  root->left->right = new TreeNode(2);
  root->right->left = new TreeNode(0);
  root->right->right = new TreeNode(8);
  root->left->right->left = new TreeNode(7);
  root->left->right->right = new TreeNode(4);

  return root;
}

TreeNode* build_testcase2() {
  TreeNode* root = new TreeNode(0);
  root->left = new TreeNode(1);
  root->left->right = new TreeNode(2);
  root->left->right->right = new TreeNode(3);
  root->left->right->right->right = new TreeNode(4);
  return root;
}

void print_vec(const std::vector<int>& vec) {
  for (int i : vec) {
    std::cout << i << " ";
  }
  std::cout << std::endl;
}

int main(int argc, char** argv) {
  TreeNode* root = build_testcase1();
  Solution s;
  std::vector<int> test_output_1 = s.distanceK(root, root->left, 2);

  std::cout << "Test 1: Expected: 7 4 1, Actual: ";
  print_vec(test_output_1);

  TreeNode* root2 = build_testcase2();
  std::vector<int> test_output_2 =
      s.distanceK(root2, root2->left->right->right, 0);
  std::cout << "Test 2: Expected: 3, Actual: ";
  print_vec(test_output_2);

  return 0;
}