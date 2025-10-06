# https://leetcode.com/problems/swim-in-rising-water/
# Difficulty: Hard

import heapq


class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        seen = {(0, 0)}
        min_heap = [(grid[0][0], 0, 0)]
        water_level = 0
        while min_heap:
            crt_level, crt_r, crt_c = heapq.heappop(min_heap)
            water_level = max(water_level, crt_level)
            if crt_r == crt_c == n - 1:
                return water_level
            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if (
                    0 <= crt_r + dr < n
                    and 0 <= crt_c + dc < n
                    and (crt_r + dr, crt_c + dc) not in seen
                ):
                    heapq.heappush(
                        min_heap, (grid[crt_r + dr][crt_c + dc], crt_r + dr, crt_c + dc)
                    )
                    seen.add((crt_r + dr, crt_c + dc))

        return -1


if __name__ == "__main__":
    s = Solution()
    grid1 = [[0, 2], [1, 3]]
    expected1 = 3
    actual1 = s.swimInWater(grid1)
    print(f"For grid {grid1}, expected {expected1}, got {actual1}")

    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6],
    ]
    expected2 = 16
    actual2 = s.swimInWater(grid2)
    print(f"For grid {grid2}, expected {expected2}, got {actual2}")
