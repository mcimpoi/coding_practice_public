# https://leetcode.com/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # typical backtracking
        # max length is 6 --> can go with n^n solution
        # i.e. not validate on every iteration

        # if crt_idx == len(nums) --> stop; if valid, add to result

        result: List[List[int]] = []

        def backtrack(crt_idx: int, buffer: List[int]):
            if crt_idx == len(nums):
                if len(set(buffer)) == len(buffer):
                    result.append([nums[idx] for idx in buffer])
                return
            for n_idx in range(len(nums)):
                # adding this and the step back below
                # increases the speed.
                if n_idx in buffer:
                    continue
                buffer[crt_idx] = n_idx
                backtrack(crt_idx + 1, buffer)
                # step back -- needed, otherwise the value will
                # stay in buffer, we generate only identity
                buffer[crt_idx] = -1

        backtrack(0, [-1 for _ in nums])
        return result


if __name__ == "__main__":
    s = Solution()
    print(f"Permutations of {[1,2,3]}: {s.permute([1, 2, 3])}")
    print(f"Permutations of {[0,1]}: {s.permute([0, 1])}")
