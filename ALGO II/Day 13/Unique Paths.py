class Solution:
    def check(self, r, c, m, n):
        if r >=0 and r< m and c >=0 and c<n:
            return True
        return False
    def uniquePaths(self, m: int, n: int) -> int:
        square = [[0 for _ in range(n)] for _ in range(m)]
        square[0][0] = 1
        for c in range(n):
            for r in range(m):
                if r == 0 and c == 0:
                    continue
                    
                if self.check(r,c-1,m,n): ## left
                    square[r][c] += square[r][c-1]
                if self.check(r-1,c,m,n): ## up
                    square[r][c] += square[r-1][c] 
        return square[-1][-1]