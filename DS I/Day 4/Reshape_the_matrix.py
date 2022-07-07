class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        arr=[]
        res=[]
        for i in mat:
            arr.extend(i)
        i=0
        k=0
        while i<r:
            temp=[]
            j=0
            while j<c:
                temp.append(arr[k])
                k+=1
                j+=1
            res.append(temp)
            i+=1
        return res