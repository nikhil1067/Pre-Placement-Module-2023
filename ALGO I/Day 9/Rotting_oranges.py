class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        minute = 0
        
        qRotten, freshCount = [], 0
        
        for i in range(m):
            for j in range(n):
                # We store rotten orange positions
                if grid[i][j] == 2:
                    qRotten.append([i,j])
                
                # We store the count of fresh oranges
                elif grid[i][j] == 1:
                    freshCount += 1
        
        if freshCount == 0:
            return 0
        
        # Define all directions (up, down, left, and right) 东西南北
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        while len(qRotten) != 0:
            minute += 1
            
            for _ in range(len(qRotten)):
                # Fill in the body here
                rottenOrange = qRotten.pop(0)

                # Search in all four directions to look for fresh oranges
                for i in range(4):
                    neighborOrange = [rottenOrange[0] + direction[i][0], rottenOrange[1] + direction[i][1]]

                    # If not an edge
                    if neighborOrange[0] >= 0 and neighborOrange[0] < m and neighborOrange[1] >= 0 and neighborOrange[1] < n:
                        
                        # If the orange is fresh
                        if grid[neighborOrange[0]][neighborOrange[1]] == 1:
                            # Turn the fresh orange into a rotten orange
                            grid[neighborOrange[0]][neighborOrange[1]] = 2
                            
                            # Remove it from the count of fresh oranges
                            freshCount -= 1
                            
                            # Add it to the queue of rotten oranges
                            qRotten.append(neighborOrange)
            
            if freshCount == 0:
                return minute
        
        return -1