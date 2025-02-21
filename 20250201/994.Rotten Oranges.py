from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        queue = deque()
        visited = [[False] * m for _ in range(n)]

        # Step 1: Enqueue all rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True

        count = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: BFS to rot fresh oranges
        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                row, col = queue.popleft()

                for dx, dy in directions:
                    nx, ny = row + dx, col + dy
                    if (
                        0 <= nx < n and 0 <= ny < m and
                        not visited[nx][ny] and grid[nx][ny] == 1
                    ):
                        visited[nx][ny] = True
                        grid[nx][ny] = 2  # Rot the fresh orange
                        queue.append((nx, ny))

        # Step 3: Check for remaining fresh oranges
        for row in grid:
            if 1 in row:
                return -1  # Fresh orange remains

        return 0 if count == -1 else count  # Return time or 0 if no fresh oranges
        
        