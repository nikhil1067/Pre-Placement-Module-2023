class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr=[]
        for i in matrix:
            arr.append(i)
        matrix.clear()
        x=0
        arr=arr[::-1]
        for i in range(len(arr[0])):
            temp=[]
            for j in range(len(arr)):
                temp.append(arr[j][i])
            matrix.append(temp)