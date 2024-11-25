class Solution:
    def closedIsland(self, grid):
        def dfs(i, j):
            # 如果越界，说明连接到边界
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            
            # 如果是水，直接返回 True
            if grid[i][j] == 1:
                return True
            
            # 标记当前格子为已访问
            grid[i][j] = 1
            
            # 递归检查上下左右，并返回是否为封闭岛屿
            top = dfs(i - 1, j)
            bottom = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            
            return top and bottom and left and right

        # 遍历网格，计算封闭岛屿数量
        closed_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # 如果当前岛屿是封闭的，计数 +1
                    if dfs(i, j):
                        closed_islands += 1
        return closed_islands


# from collections import deque

# class Solution:
#     def closedIsland(self, grid):
#         def bfs(i, j):
#             queue = deque([(i, j)])
#             is_closed = True
            
#             while queue:
#                 x, y = queue.popleft()
                
#                 # 如果越界，说明连接到边界
#                 if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
#                     is_closed = False
#                     continue
                
#                 # 如果是水，跳过
#                 if grid[x][y] == 1:
#                     continue
                
#                 # 标记当前格子为已访问
#                 grid[x][y] = 1
                
#                 # 将上下左右加入队列
#                 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     queue.append((x + dx, y + dy))
            
#             return is_closed

#         closed_islands = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 0:
#                     if bfs(i, j):
#                         closed_islands += 1
#         return closed_islands
