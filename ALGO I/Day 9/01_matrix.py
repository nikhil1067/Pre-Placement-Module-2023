class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(mat)):
            result.append([None] * len(mat[0]))
            
        # add 0 cells to BFS queue
        queue = []
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                if mat[x][y] == 0:
                    result[x][y] = 0
                    queue.append((x, y))
        
        # run BFS
        while queue:
            x, y = queue.pop(0)
            to_add = []
            
            if x > 0:
                to_add.append((x-1, y))
            if x < len(result) - 1:
                to_add.append((x+1, y))
            if y > 0:
                to_add.append((x, y-1))
            if y < len(result[x]) - 1:
                to_add.append((x, y+1))
                
            for n in to_add:
                if result[n[0]][n[1]] is None:
                    result[n[0]][n[1]] = result[x][y] + 1
                    queue.append(n)
            
        return result