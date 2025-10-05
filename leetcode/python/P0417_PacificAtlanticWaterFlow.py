# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium

from collections import deque

# Note from Gemini code review:
# make the fill function return set of visited coordinates.
# then result is just the intersection of the two sets.
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # dfs/bfs from edges
        # mark with value 1 one ocean; 2 the other;
        # count what's labelled with 3.
        reach = [[0 for _ in row] for row in heights]

        def fill_(reach: list[list[int]], val: int, row: int, col: int) -> list[list[int]]:
            visited = [[False for _ in row] for row in heights]
            q = deque()
            n_rows, n_cols = len(heights), len(heights[0])
            # add the whole row and column
            for r in range(n_rows):
                q.append((r, col))
                visited[r][col] = True
                reach[r][col] += val
            for c in range(n_cols):
                if not visited[row][c]:
                    q.append((row, c))
                    visited[row][c] = True
                    reach[row][c] += val
            while len(q):
                crt_r, crt_c = q.pop()
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    next_r, next_c = crt_r + dr, crt_c + dc
                    if (0 <= next_r < n_rows and
                        0 <= next_c < n_cols and 
                        not visited[next_r][next_c] and
                         heights[next_r][next_c] >= heights[crt_r][crt_c]):
                        visited[next_r][next_c] = True
                        reach[next_r][next_c] += val
                        q.append((next_r, next_c))
            return reach

        def print_matrix_(mat):
            res = "\n".join(["".join([f"{x:3} " for x in row]) for row in mat])
            print(res)

        n_rows, n_cols = len(heights), len(heights[0])
        reach = fill_(reach, 1, 0, 0)
        reach = fill_(reach, 2, n_rows - 1, n_cols - 1)
        
        res = []
        for r in range(n_rows):
            for c in range(n_cols):
                if reach[r][c] == 3:
                    res.append([r, c])
        
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))  # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    print(s.pacificAtlantic([[2,1],[1,2]]))  # [[0,0],[0,1],[1,0],[1,1]]
    print(s.pacificAtlantic([[1]]))  # [[0,0]]
    print(s.pacificAtlantic([[10,10,10],[10,1,10],[10,10,10]]))  # [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
    print(s.pacificAtlantic([[3,3,3],[3,1,3],[3,3,3]]))  # [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]