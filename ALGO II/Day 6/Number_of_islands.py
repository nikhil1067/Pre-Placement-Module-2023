class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        m, n = len(grid), len(grid[0])
        number_of_islands = 0
        visited = set()
        queue = collections.deque()
        for row in range(0, m):
            for column in range(0, n):     
                if grid[row][column] == '1' and (row, column) not in visited:
                    number_of_islands += 1
                    queue.append((row, column))
                    while queue:
                        curr_queue_size = len(queue)
                        for i in range(0, curr_queue_size):
                            row_temp, col_temp = queue.popleft()
                            if (0 <= row_temp < m) and \
                               (0 <= col_temp < n) and \
                               grid[row_temp][col_temp] == '1' and \
                               (row_temp, col_temp) not in visited:
                                visited.add((row_temp, col_temp))
                                queue.append((row_temp + 1, col_temp))
                                queue.append((row_temp - 1, col_temp))
                                queue.append((row_temp, col_temp + 1))
                                queue.append((row_temp, col_temp - 1))
        return number_of_islands