import collections
import math
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        queue= collections.deque([
            [0,0]
        ])
        track = {(0,0): 1} 
        seen = set()
        while len(queue) != 0:
            currArr = queue.pop()
            
            currX, currY = currArr
            if (currX, currY) in seen:
                continue
            else:
                seen.add((currX, currY))
    
            if currX >= len(grid)-1 and currY >= len(grid) -1:
                continue

            currVal = track[(currX, currY)]
            
            box = [(currX-1, currY-1), (currX, currY-1), (currX+1, currY-1), (currX-1, currY), (currX+1, currY), (currX-1, currY+1), (currX, currY+1), (currX+1, currY+1)]
            for (itx, ity) in box:
                        
                if itx < 0 or ity < 0 or itx > len(grid)-1 or ity > len(grid)-1:
                    continue
                if grid[itx][ity] == 0:

                    if (itx, ity) in track:
                        track[(itx, ity)] = min(track[(currX, currY)]+1, track[(itx, ity)])
                    else:
                        track[(itx, ity)] = track[(currX, currY)]+1
                    queue.appendleft([itx, ity])
            
        if (len(grid)-1, len(grid)-1) not in track:
            return -1
        return track[(len(grid)-1, len(grid)-1)]