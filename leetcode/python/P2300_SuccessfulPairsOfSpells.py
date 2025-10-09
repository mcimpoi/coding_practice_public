# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Difficulty: Medium

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        # m and n are up to 10^5 -- O(mxn) solution would probably TLE
        # we need number of pairs for which spell * potion >= success
        # and we need to do this for every pair.

        # since we care only of the count --> don't need to keep order
        # we need only index where potion[idx] * spell > success
        # i.e. potion[idx] > success / spell
        # 
        potions.sort()
        res = []
        for spell in spells:
            target = (success + spell - 1) // spell
            left, right = 0, len(potions) - 1
            first_valid_index = len(potions)
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= target:
                    first_valid_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            res.append(len(potions) - first_valid_index)
        return res
    
if __name__ == "__main__":
    s = Solution()
    for spells, potions, success, expected in [
        ([5,1,3], [1,2,3,4,5], 7, [4,0,3]),
        ([3,1,2], [8,5,8], 16, [2,0,2]),
    ]:
        actual = s.successfulPairs(spells, potions, success)
        print(f"successfulPairs({spells}, {potions}, {success}) = {actual}, expected {expected}")
        assert actual == expected