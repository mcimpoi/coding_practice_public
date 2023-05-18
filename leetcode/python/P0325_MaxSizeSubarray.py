from collections import defaultdict

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        cumm_sum = [0] * (n + 1)
        idx = defaultdict(int)
        max_len = 0
        for ii in range(1, n + 1):
            cumm_sum[ii] = cumm_sum[ii - 1] + nums[ii - 1]
            if idx[cumm_sum[ii]] > 0:
                idx[cumm_sum[ii]] = min(ii, idx[cumm_sum[ii]])
            else:
                idx[cumm_sum[ii]] = ii
        for ii in range(n, 0, -1):
            jj = idx[cumm_sum[ii] - k]
            if cumm_sum[ii] == k:
                if ii > max_len:
                    max_len = ii
            if jj > 0:
                if ii - jj > max_len:
                    max_len = ii - jj
        return max_len

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArrayLen([1, -1, 5, -2, 3], 3))
    print(s.maxSubArrayLen([-2, -1, 2, 1], 1))
    print(s.maxSubArrayLen([-1, 1, 2, 3], 2))
    print(s.maxSubArrayLen([-1], -1))
