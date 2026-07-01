class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        need to use bfs:
        in bfs, maintain curr_area and iterate through surrounding nodes
        mark visited nodes with 0, pass the curr_area to surrounding nodes
        when queue empty, return the curr_area
        Time comp: O(m*n)
        Space comp: O(min(m, n))

        iterate through grid with m*n, start bfs at elements = 1
        '''
        # need to check if element in range or not
        def in_bounds(x, y):
            if x < 0 or x >= len(grid):
                return False
            if y < 0 or y >= len(grid[0]):
                return False
            return True
        
        def bfs(x, y):
            q = [(x, y)]
            curr_area = 0
            while q:
                x, y = q.pop(0)
                if in_bounds(x, y):
                    if grid[x][y] == 1:
                        curr_area += 1
                        # mark as visited (0)
                        grid[x][y] = 0
                        # append 4 directions to queue
                        # only continue appending if element is 1
                        q.append((x+1, y))
                        q.append((x-1, y))
                        q.append((x, y+1))
                        q.append((x, y-1))
            
            return curr_area
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area





        
            
        