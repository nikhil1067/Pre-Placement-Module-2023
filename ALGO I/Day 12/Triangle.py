class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)-2
        while n>=0:
            for i in range(n+1):
                triangle[n][i]+=min(triangle[n+1][i],triangle[n+1][i+1])
            n-=1
        return triangle[0][0]