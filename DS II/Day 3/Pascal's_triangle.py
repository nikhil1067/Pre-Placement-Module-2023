class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr={0:[1],1:[1,1]}
        if rowIndex<=1:
            return arr[rowIndex]
        i=2
        while i<=rowIndex:
            j=1
            temp=[1]
            while j<len(arr[i-1]):
                temp.append(arr[i-1][j-1]+arr[i-1][j])
                j+=1
            temp.append(1)
            arr[i]=temp
            i+=1
        return arr[rowIndex]