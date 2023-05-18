

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ii = 0
        max_len = 1
        idx_start = 0
        idx_end = 1
        while ii < n:
            jj = ii + 1
            while jj < n and s[ii] == s[jj]:
                jj += 1
            i_prev = ii - 1
            j_next = jj
            while i_prev >= 0 and j_next < n and s[i_prev] == s[j_next]:
                i_prev -= 1
                j_next += 1
            crt_len = j_next - i_prev
            if crt_len > max_len:
                idx_start = i_prev
                idx_end = j_next
                max_len = crt_len
            ii = jj
        return s[idx_start + 1: idx_end]


if __name__ == "__main__":
    sol = Solution()
    for ss in ['', 'bananas', 'abcdef', 'aaabcd', 'cbbd', 'babad', 'babcdef', 'aaaaaa', 'zaaa', 'zaaaaaaaaaaaaaaaaaaaaa', 'zzzxxxyyy', 'abcdefghijkkjihgfedcba']:
        print(ss, ' ---> ', sol.longestPalindrome(ss))
