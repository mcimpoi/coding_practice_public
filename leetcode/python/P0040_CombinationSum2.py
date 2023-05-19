# https://leetcode.com/problems/combination-sum-ii
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def findCombinations(combination: List[int], target_sum: int, idx: int) -> None:
            if target_sum == 0:
                result.append(combination)
                return
            if target_sum < 0:
                return

            for i in range(idx, len(candidates)):
                # sorted the candidates array, the values only increase
                if target_sum - candidates[i] < 0:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                findCombinations(
                    combination + [candidates[i]], target_sum - candidates[i], i + 1
                )

        candidates.sort()
        findCombinations([], target, 0)
        return result


if __name__ == "__main__":
    solution = Solution()

    for ii, testcase in enumerate((([10, 1, 2, 7, 6, 1, 5], 8),)):
        candidates, target = testcase
        print(f"Testcase: {ii + 1} {candidates} {target}]\n")
        print(f"Solution: {solution.combinationSum2(candidates, target)}\n")
