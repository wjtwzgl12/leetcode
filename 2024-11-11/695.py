class Solution:
    def maxAreaOfIsland(self, grid):
        def dfs(i, j):
            # 如果越界或当前格子是水，返回面积为 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            
            # 标记当前格子为已访问
            grid[i][j] = 0
            
            # 计算当前格子的面积 + 上下左右四个方向的面积
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        
        # 初始化最大面积
        max_area = 0
        
        # 遍历网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # 遇到岛屿，启动 DFS
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
