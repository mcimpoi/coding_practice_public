# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # approach 1: recursion:
        # combinations[digit + remaining_digits] = \
        #   letter + partial_string for letter in letters[digit] \
        #   for partial_string in combinations[remaining_digits]

        # approach 2: backtracking
        # stop if crt_idx == len(digits) and add to solution;
        # buffer initialized with random character; all combinations are valid.

        # approach 3: for loops;  not implemented; the other variants
        #  are more general.
        # since the input is at most 4 chars; we can treat all cases
        #  separately, as for loops.
        # pros: fast to code, cons: does not scale to longer sequences.

        key_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []
        buffer = ["*" for _ in digits]

        def backtrack(idx: int):
            if idx == len(digits):
                if buffer:
                    result.append("".join(buffer))
                return
            for letter in key_mapping[digits[idx]]:
                buffer[idx] = letter
                backtrack(idx + 1)

        def recursion(digits: str):
            if len(digits) == 0:
                return []
            if len(digits) == 1:
                return [x for x in key_mapping[digits[0]]]
            partial_results = recursion(digits[1:])

            return [
                letter + partial_result
                for letter in key_mapping[digits[0]]
                for partial_result in partial_results
            ]

        return recursion(digits)
        # backtrack(0)
        # return result


if __name__ == "__main__":
    s = Solution()
    print(f"Letter combinations of 23: {s.letterCombinations('23')}")
    print(f"Letter combinations of '': {s.letterCombinations('')}")
    print(f"Letter combinations of 9782: {s.letterCombinations('9782')}")
