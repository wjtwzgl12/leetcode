# class Solution:
#     def maxAreaOfIsland(self, grid):
#         def dfs(i, j):
#             # 如果越界或当前格子是水，返回面积为 0
#             if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
#                 return 0
            
#             # 标记当前格子为已访问
#             grid[i][j] = 0
            
#             # 计算当前格子的面积 + 上下左右四个方向的面积
#             return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
#         # 初始化最大面积
#         max_area = 0
        
#         # 遍历网格
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:  # 遇到岛屿，启动 DFS
#                     max_area = max(max_area, dfs(i, j))
        
#         return max_area
    

#     from collections import deque

class Solution:
    def numEnclaves(self, grid):
        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                # 标记当前格子为访问过
                grid[x][y] = 0
                # 检查上下左右
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))

        rows, cols = len(grid), len(grid[0])
        # 从边界开始标记
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and grid[i][j] == 1:
                    bfs(i, j)

        # 统计未被标记的陆地数量
        return sum(grid[i][j] == 1 for i in range(rows) for j in range(cols))

