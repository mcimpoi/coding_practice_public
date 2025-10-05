from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_idx = 0
        prev_idx = defaultdict(lambda: -1)
        counts = defaultdict(int)
        max_length = 0
        for ii, ch in enumerate(s):
            if counts[ch] == 1:
                max_length = max(max_length, ii - start_idx)
                for jj in range(start_idx, prev_idx[ch] + 1):
                    counts[s[jj]] -= 1
                start_idx = prev_idx[ch] + 1
            counts[ch] += 1
            prev_idx[ch] = ii

        max_length = max(max_length, len(s) - start_idx)
        return max_length


if __name__ == "__main__":
    s = Solution()
    for ss in [
        "abcabcbb",
        "bbbbb",
        "",
        "abc",
        "pwwkew",
        "abcdefbcdefghi",
        "ababababababababababababa",
    ]:
        print(ss, s.lengthOfLongestSubstring(ss))
