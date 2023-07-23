// https://leetcode.com/problems/powx-n/

class Solution {
 public:
  double myPow(double x, int n) {
    if (n == 0) {
      return 1;
    }
    if (x == 0) {
      return 0;
    }
    if (x == 1) {
      return 1;
    }

    if (x == -1) {
      return n % 2 == 0 ? 1.0 : -1.0;
    }

    long long n_ = static_cast<long long>(n);
    bool div = false;
    if (n_ < 0) {
      div = true;
      n_ = -n_;
    }

    double result = 1;

    while (n_ > 0) {
      while (n_ > 0 && 0 == n_ % 2) {
        n_ /= 2;
        x *= x;
      }

      --n_;
      result *= x;
    }

    if (div) {
      return 1. / result;
    }
    return result;
  }
};