class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        n_rows = len(board)
        n_cols = len(board[0])
        
        if n_rows <= 2 or n_cols <= 2:
            return 
        
        Oset = set()
        stack = [(row, col) for row in [0, n_rows-1] for col in range(n_cols)]
        stack += [(row, col) for row in range(n_rows) for col in [0, n_cols-1]]
        
        while stack:
            row, col = stack.pop()
            if 0 <= row < n_rows and 0 <= col < n_cols:
                if board[row][col] == "O" and (row, col) not in Oset:
                    Oset.add((row, col))
                    stack += [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

        for row in range(1, n_rows-1):
            for col in range(1, n_cols-1):
                if (row, col) not in Oset:
                    board[row][col] = "X"