#include <vector>

class Solution {
 public:
  int singleNumber(std::vector<int>& nums) {
    // one number appears only once
    // think of the xor trick; however, all the other numbers
    // appear 3 times, so we can't use the xor trick;
    // we are expected to use linear time and constant memory
    //
    // we can't use baseline solution, i.e.
    //  1. count frequency of numbers (O(n) time; O(n) memory)
    //  2. for each number, try to find it in array: (O(n^2) time, O(1) mem)

    // we can count bits... i.e. if a number appears 3 times --> it's bits
    // are set a multiple of 3 times.
    // for the number that appears only once, the bits are set M3 + 1 times.

    int res = 0;
    for (int bit = 0; bit < 32; ++bit) {
      int counts = 0;
      int mask = 1 << bit;
      for (int num : nums) {
        if (mask == (num & mask)) {
          ++counts;
        }
      }
      if (counts % 3 == 1) {
        res |= mask;
      }
    }
    return res;
  }
};