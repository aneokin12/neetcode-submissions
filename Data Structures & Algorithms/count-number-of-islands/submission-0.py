class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def in_bounds(x, y):
            if x < 0 or x >= len(grid):
                return False
            if y < 0 or y >= len(grid[0]):
                return False
            return True
        

        def dfs(x, y):
            # if cell 0 or OOB, return
            if not in_bounds(x, y):
                return
            elif grid[x][y] == '0':
                return
            # otherwise, mark cell as visited (cell = 0)
            grid[x][y] = '0'
            # run dfs in all 4 directions
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # iterate over entire matrix, when we encounter cell = 1, increment counter
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)
        
        return counter



        