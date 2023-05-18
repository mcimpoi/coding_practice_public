from collections import defaultdict
import cProfile
import pstats


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # for ii in range(len(A))
        #   for jj in range(len(B[0]))
        #       for kk in range(len(B)):
        #           C[ii][jj] += A[ii][kk] * B[kk][jj]
        #
        # A -- m x n
        # B -- n x p
        # TODO: handle empty matrices

        idx_a = defaultdict(set)
        idx_b = defaultdict(set)
        m = len(A)
        n = len(A[0])
        p = len(B[0])
        C = [[0 for _ in range(p)] for _ in range(m)]
        for ii in range(m):
            if not any(A[ii]):
                continue
            for jj in range(n):
                if A[ii][jj] != 0:
                    if not any(B[jj]):
                        continue
                    for kk in range(p):
                        C[ii][kk] += A[ii][jj] * B[jj][kk]
        return C

    def multiply_slow(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # for ii in range(len(A))
        #   for jj in range(len(B[0]))
        #       for kk in range(len(B)):
        #           C[ii][jj] += A[ii][kk] * B[kk][jj]
        #
        # A -- m x n
        # B -- n x p
        # TODO: handle empty matrices

        idx_a = defaultdict(set)
        idx_b = defaultdict(set)
        m = len(A)
        n = len(A[0])
        p = len(B[0])
        for ii in range(m):
            for jj in range(n):
                if A[ii][jj] != 0:
                    idx_a[ii].add(jj)
        for ii in range(n):
            for jj in range(p):
                if B[ii][jj] != 0:
                    idx_b[jj].add(ii)
        C = [[0 for _ in range(p)] for _ in range(m)]
        for ii in range(m):
            for jj in range(p):
                items = idx_a[ii] & idx_b[jj]
                for el in items:
                    C[ii][jj] += A[ii][el] * B[el][jj]
        return C


if __name__ == '__main__':
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    s = Solution()
    print(s.multiply(A, B))
