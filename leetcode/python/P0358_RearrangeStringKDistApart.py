# https://leetcode.com/problems/rearrange-string-k-distance-apart/

from collections import Counter
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # keep a priority queue, ordered by frequency;
        # if the current character can't be inserted, keep it in a buffer.
        # mark if can add the current character to the result, if not,
        # return empty string;
        # otherwise, add the character back to the queue, with updated
        # frequency, if we still have occurences.

        # from editorial - the buffer could be repalced by a queue.
        # Time complexity: O(n * k log(k)), where n is the length of s.
        # since k is 26 --> O(n)
        # building heap -- k log k, where k is the number of unique characters.
        # for each character in the string, we run heappop / heappush;
        # worst case, pop all elements of heap and add them back.
        freq = Counter(s)
        unique_chars = freq.keys()

        heap = []

        for ch, frequency in freq.items():
            heapq.heappush(heap, (-frequency, ch))

        result = ""
        prev_idx = {ch: -k for ch in unique_chars}
        count, ch = -1, "*"

        for crt_idx in range(len(s)):
            buffer = []
            ok = False
            while len(heap) > 0:
                count, ch = heapq.heappop(heap)
                if crt_idx - prev_idx[ch] >= k:
                    result += ch
                    prev_idx[ch] = crt_idx
                    count += 1
                    ok = True
                    break
                else:
                    # TODO: use deque here.
                    buffer.append((count, ch))

            if not ok:
                return ""

            if count < 0:
                heapq.heappush(heap, (count, ch))
            for x in buffer:
                heapq.heappush(heap, x)

        return result


if __name__ == "__main__":
    # NOTE: solution might not be unique.
    for testcase, expected in (
        (("aabbcc", 3), "abcabc"),
        (("aaabc", 2), "abaca"),
        (("aaabc", 3), ""),
        (("aaadbbcc", 2), "abacabcd"),
    ):
        actual = Solution().rearrangeString(*testcase)
        print(f"Testcase: {testcase}. Expected: {expected}. Actual: {actual}")
