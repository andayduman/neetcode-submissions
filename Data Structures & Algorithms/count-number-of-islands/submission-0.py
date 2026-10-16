class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    rx, cx = row+dr, col+dc
                    if (rx) in range(rows) and (cx) in range(cols) and grid[rx][cx] == "1" and (rx, cx) not in visited:
                        q.append((rx, cx))
                        visited.add((rx, cx))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # we then need to perform breadth first search to find the surrounding 1s
                    bfs(r, c)
                    islands += 1
        return islands