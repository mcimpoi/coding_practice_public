class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            if n == 0:
                return 1
            else:
                return 0.
        if n == 0:
            return 1
        if x == 1:
            return 1
        base = x
        result = 1
        invert = False
        if n < 0:
            invert = True
            n = -n
        while n > 0:
            while n % 2 == 0:
                base *= base
                n = n // 2
            result *= base
            n -= 1
        if invert and x != 0:
            result = 1. / result
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(0, 0))
    print(s.myPow(3, 3))
    print(s.myPow(5.3, 2))
    print(s.myPow(2, 31))
