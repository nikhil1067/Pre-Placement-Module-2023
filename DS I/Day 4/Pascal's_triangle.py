class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[[1],[1,1]]
        if numRows<=2:
            return arr[:numRows]
        i=2
        while i<numRows:
            j=0
            temp=[]
            while j<len(arr[-1])-1:
                temp.append(arr[-1][j]+arr[-1][j+1])
                j+=1
            temp.insert(0,1)
            temp.append(1)
            arr.append(temp)
            i+=1
        return arr