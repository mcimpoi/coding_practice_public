# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

from typing import List
from collections import defaultdict
from bisect import bisect_left


def lookup_version(arr: List[int], difference: int) -> int:
    # key to speed:
    # keep seq_len for number instead of index;
    # the same number can appear at different indices.

    indices = defaultdict(list)
    max_len = 1
    seq_len = {}

    for idx, num in enumerate(arr):
        indices[num].append(idx)

    n_steps = {}
    for idx, num in enumerate(arr):
        # already computed
        if seq_len.get(num, 0) != 0:
            continue
        seq_len[num] = 1
        n_steps[idx] = 1
        crt_idx = idx
        crt_num = num
        while crt_idx < len(arr):
            next_num = crt_num + difference
            if len(indices[next_num]) == 0:
                break
            next_idx = bisect_left(indices[next_num], crt_idx + 1)
            # not found
            if next_idx >= len(indices[next_num]):
                break
            next_idx = indices[next_num][next_idx]
            seq_len[next_num] = seq_len[crt_num] + 1
            max_len = max(max_len, seq_len[next_num])
            crt_idx, crt_num = next_idx, next_num
            n_steps[idx] += 1

    return max_len


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # Looks like LIS; TODO: revisit LIS
        # n = 10^5 -- O(n^2 might TLE)
        # O(n^2): for each item, look for item + difference in the rest of the array
        # not sorted, so worst case, we check all elements;

        # keep list of indices for every value; -- don't keep only minimum, because
        # the next position of item + diff depends on where item is.

        # for item at index i:
        #  while get_index(item + diff) is not None:
        #     item = item + diff;
        #     crt_index = get_index(item + diff)
        #     ? update the subseq length at index crt_index.

        # for some particular cases, e.g last - first = len * diff --> O(n) check
        # depends on the structure of array; not general.

        # complexity: time: O(n * logn) mem: O(n) -- because we store indices of values
        # one index per value + dict overhead. worst case, all keys distinct --> 2 * n

        # after reading editorial sol:
        # for a given val --> look for longest subseq ending in val - diff
        # this works because dp[val] is updated as we "visit" numbers in the array
        # if dp[val - diff] is not 0, then it means we found val-diff before current
        # val in the array.

        dp = {}
        max_len = 1
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            max_len = max(max_len, dp[num])

        return max_len


def read_long_example():
    with open("examples/P1218_example.txt", "r") as f:
        lines = f.readlines()
        arr = [int(x) for x in lines[0].split(",")]
        diff = int(lines[1])
        return arr, diff


if __name__ == "__main__":
    sol = Solution()
    arr, diff = read_long_example()
    print(len(arr))
    print(sol.longestSubsequence(arr, diff))
