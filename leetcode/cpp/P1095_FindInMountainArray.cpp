// cleaned up solution at:
// https://github.com/mcimpoi/coding_practice_public/tree/main/leetcode
/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 */

#include <iostream>
#include <unordered_map>
#include <vector>

class MountainArray {
 public:
  MountainArray(const std::vector<int>& arr) { this->arr = arr; }
  int get(int index) { return arr[index]; }
  int length() { return arr.size(); }

 private:
  std::vector<int> arr;
};

class Solution {
 public:
  int findInMountainArray(int target, MountainArray& mountainArr) {
    // arr length is up to 10^4;
    // max 100 calls to get()
    // we need smallest index
    // mountain array --> sorted ascending up to middle;
    // sorted descending from middle to end;
    // binary search to find middle;
    // binary search to find element in the left part;
    // if not found, binary search in the right part.

    // cache values we searched.

    int arr_len = mountainArr.length();
    std::unordered_map<int, int> cache;

    int idx_top = searchMountainTop(mountainArr, 0, arr_len - 1, cache);
    // TODO: possible to use the same function, depending on sign
    // of difference / comparator.
    int top_val = try_get(cache, mountainArr, idx_top);
    // std::cout << "top: " << idx_top << " value: " << top_val << "\n";
    if (top_val == target) {
      return idx_top;
    }

    int search_res = search(mountainArr, target, 0, idx_top, cache, -1);
    if (search_res == -1) {
      search_res = search(mountainArr, target, idx_top, arr_len, cache, 1);
    }
    return search_res;
  }

  int searchMountainTop(MountainArray& mountain, int idx_left, int idx_right,
                        std::unordered_map<int, int>& cache) {
    bool found = false;

    // pick one example, e.g. [0, 1, 2, 4, 2, 1]; 3
    int left = idx_left;
    int right = idx_right;

    while (left <= right) {
      int imid = (left + right) / 2;
      int mid = try_get(cache, mountain, imid);
      int before_mid = try_get(cache, mountain, imid - 1);
      if (before_mid < mid) {
        int after_mid = try_get(cache, mountain, imid + 1);
        if (mid > after_mid) {
          return imid;
        } else {
          left = imid + 1;
        }
      } else {
        right = imid;
      }
    }
    return left;  // should always return mid above
  }

  int search(MountainArray& mountain, int target, int left_idx, int right_idx,
             std::unordered_map<int, int>& cache, int direction) {
    int left = left_idx;
    int right = right_idx;

    while (left < right) {
      int imid = (left + right) / 2;
      int val = try_get(cache, mountain, imid);
      if (val == target) {
        return imid;
      }
      if (sign_different(target - val, direction)) {
        right = imid;
      } else {
        left = imid + 1;
      }
    }
    return -1;
  }

  inline bool sign_different(int x, int y) {
    return ((x < 0 && y < 0) || (x > 0 && y > 0));
  }

  int try_get(std::unordered_map<int, int>& cache, MountainArray& mountain,
              int position) {
    // return  mountain.get(position);

    if (position < 0) {
      return -1;
    }
    // std::cout << "try_get: " << position << "\n";
    if (!cache.contains(position)) {
      int val = mountain.get(position);
      cache[position] = val;
    }
    return cache[position];
  }
};

int main(int argc, char** argv) {
  Solution sol;
  std::vector<int> arr = {1, 2, 3, 4, 5, 3, 1};
  MountainArray mountain(arr);
  int target = 0;
  int res = sol.findInMountainArray(target, mountain);
  std::cout << "res: " << res << "\n";
  return 0;
}
