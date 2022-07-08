class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr={}
        res=math.inf
        for i in s:
            if i in arr:
                arr[i]+=1
            else:
                arr[i]=1
        for i in arr:
            if arr[i]==1:
                res=min(res,s.index(i))
        if res==math.inf:
            return -1
        return res