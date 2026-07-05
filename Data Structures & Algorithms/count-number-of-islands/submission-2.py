class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def in_bounds(x, y):
            if x < 0 or x >= len(grid):
                return False
            # len(grid) guaranteed to be >= 1, so grid[0] will never be None
            if y < 0 or y >= len(grid[0]):
                return False
        # If not OOB, return True
            return True
        
        def dfs(x, y):
            # check OOB
            if not in_bounds(x, y):
                return
            # check grid[x][y] == 0
            if grid[x][y] == '0':
                return
            # otherwise, mark as visited, recursively DFS adjacent positions
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        # Now, iterate over matrix and run DFS on any seen land element
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)
        return counter

