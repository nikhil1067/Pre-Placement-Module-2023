class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr=[]
        for i in matrix:
            arr.extend(i)
        if target in arr:
            return True
        return False