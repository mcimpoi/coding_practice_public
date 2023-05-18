class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n_a = len(a)
        n_b = len(b)

        bin_a = [int(x) for x in reversed(a)]
        bin_b = [int(x) for x in reversed(b)]

        c = [0] * (max(n_a, n_b) + 1)
        carry = 0
        for ii in range(min(n_a, n_b)):
            crt = bin_a[ii] + bin_b[ii] + carry
            carry = crt // 2
            c[ii] = crt % 2

        if n_a > n_b:
            for ii in range(n_b, n_a):
                crt = bin_a[ii] + carry
                carry = crt // 2
                c[ii] = crt % 2
        else:
            for ii in range(n_a, n_b):
                crt = bin_b[ii] + carry
                carry = crt // 2
                c[ii] = crt % 2
        if carry == 1:
            c[max(n_a, n_b)] = 1
        else:
            c = c[:-1]
        return ''.join([str(cc) for cc in reversed(c)])


if __name__ == '__main__':
    s = Solution()
    for aa, bb in zip(['0', '0', '1', '11', '10', '111'], ['0', '1', '1', '1', '1', '1101']):
        print(aa, bb, s.addBinary(aa, bb))
