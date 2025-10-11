# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/
# Difficulty: Medium
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        counts = Counter(power)
        sorted_powers = sorted(counts.keys())
        n = len(sorted_powers)

        dp = [0] * n

        dp[0] = sorted_powers[0] * counts[sorted_powers[0]]
        previous_suitable_index = 0
        for i in range(1, n):
            take_current = sorted_powers[i] * counts[sorted_powers[i]]
            while (
                previous_suitable_index < i
                and sorted_powers[i] - sorted_powers[previous_suitable_index] > 2
            ):
                previous_suitable_index += 1

            damage_from_previous = 0
            if sorted_powers[i] - sorted_powers[previous_suitable_index] > 2:
                damage_from_previous = dp[previous_suitable_index]
            elif previous_suitable_index > 0:
                damage_from_previous = dp[previous_suitable_index - 1]

            dp[i] = max(dp[i - 1], take_current + damage_from_previous)

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    for power, expected in [
        ([1, 1, 3, 4], 6),
        ([7, 1, 6, 6], 13),
        ([7, 14, 3, 19, 8, 12, 5, 16, 2, 11, 18, 4, 9, 15, 6], 65),
    ]:
        actual = s.maximumTotalDamage(power)
        print(f"maximumTotalDamage({power}) = {actual}, expected {expected}")
        assert actual == expected
