class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        parent={x:x for x in range(n)}
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    parent[self.find(parent,i)]=self.find(parent,j)
        return sum([1 for key, val in parent.items() if key==val])
    def find(self,parent,node):
        if parent[node]!=node:
            return self.find(parent,parent[node])
        return parent[node]