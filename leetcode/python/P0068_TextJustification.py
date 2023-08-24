# https://leetcode.com/problems/text-justification/

from typing import List
import copy


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # split the words into lines
        # e.g. if crt_len + len(word) + 1 < maxWidth -> add to line;
        # go line by line and justify
        # handle last line and lines with one word as left justify

        def left_justify(words: List[str], maxWidth: int) -> str:
            return " ".join(words).ljust(maxWidth)

        def full_justify(words: List[str], maxWidth: int) -> str:
            n_words = len(words)
            remaining_space = maxWidth - sum([len(wd) for wd in words])
            avg_space = remaining_space // (n_words - 1)
            extra = remaining_space % (n_words - 1)

            res = ""
            for idx, word in enumerate(words):
                res += word
                if idx < extra:
                    res += "".ljust(avg_space + 1)
                else:
                    res += "".ljust(avg_space)

            return res[:maxWidth]

        crt_len = 0
        crt_line = []
        lines = []
        for wd in words:
            if crt_len == 0:
                crt_len += len(wd) + 1
                crt_line.append(wd)
            else:
                if crt_len + len(wd) <= maxWidth:
                    crt_len += len(wd) + 1
                    crt_line.append(wd)
                else:
                    lines.append(copy.deepcopy(crt_line))
                    crt_line.clear()
                    crt_len = len(wd) + 1
                    crt_line = [wd]
        if len(crt_line) > 0:
            lines.append(crt_line)

        result = []
        for idx, line in enumerate(lines):
            if idx == len(lines) - 1 or len(line) == 1:
                result.append(left_justify(line, maxWidth))
            else:
                result.append(full_justify(line, maxWidth))

        return result


if __name__ == "__main__":
    s = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(f"Text: {words}. Justified: {s.fullJustify(words, maxWidth=16)}")
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    print(f"The text: {words}. Justified: {s.fullJustify(words, maxWidth=16)}")
    words = [
        "Science",
        "is",
        "what",
        "we",
        "understand",
        "well",
        "enough",
        "to",
        "explain",
        "to",
        "a",
        "computer.",
        "Art",
        "is",
        "everything",
        "else",
        "we",
        "do",
    ]
    print(f"The text: {words}. Justified: {s.fullJustify(words, maxWidth=20)}")
