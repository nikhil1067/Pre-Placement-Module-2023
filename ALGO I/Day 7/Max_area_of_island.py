class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        res=0
        arr=set()
        def area(r,c):
            if 0<=r<n and 0<=c<m and (r,c) not in arr and grid[r][c]:
                arr.add((r,c))
            else:
                return 0
            return 1+area(r+1,c)+area(r,c+1)+area(r-1,c)+area(r,c-1)
        for i in range(n):
            for j in range(m):
                temp=area(i,j)
                res=max(res,temp)
        return res