// https://leetcode.com/problems/peak-index-in-a-mountain-array/
#include <vector>

class Solution {
 public:
  int peakIndexInMountainArray(std::vector<int>& A) {
    int left = 0;
    int right = static_cast<int>(A.size());
    int middle = -1;
    while (left < right) {
      int middle = left + (right - left) / 2;
      if ((A[middle] > A[middle + 1]) && (A[middle - 1] < A[middle])) {
        return middle;
      }
      if (A[middle] < A[middle + 1]) {
        left = middle;
      } else {
        right = middle;
      }
    }
    return middle;
  }
};

// TODO: add main + tests.