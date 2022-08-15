from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        isLands = 0

        def dfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, column = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, column + dc

                    if (r in range(rows) and
                        c in range(columns) and 
                        (r, c) not in visited and 
                        grid[r][c] == "1"):
                        q.append((r, c))
                        visited.add((r, c))


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    isLands += 1

        return isLands

s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","1"]
]

print(s.numIslands(grid))
