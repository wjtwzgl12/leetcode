class Solution:
    def countSubIslands(self, grid1, grid2):
        def dfs(i, j):
            if i < 0 or i >= len(grid1) or j < 0 or j >= len(grid1[0]) or grid2[i][j] == 0:
                return True
            
            if grid1[i][j] == 0:
                self.is_sub_island = False
            
            grid2[i][j] = 0
           
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        sub_islands = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1: 
                    self.is_sub_island = True
                    dfs(i, j)
                    if self.is_sub_island:  
                        sub_islands += 1
        return sub_islands
