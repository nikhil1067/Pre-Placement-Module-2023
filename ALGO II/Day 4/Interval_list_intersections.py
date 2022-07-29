class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        res=[]
        while i<len(firstList) and j<len(secondList):
            low=max(firstList[i][0],secondList[j][0])
            high=min(firstList[i][1],secondList[j][1])
            if low<=high:
                res.append([low,high])
            if firstList[i][1]>secondList[j][1]:
                j+=1
            else:
                i+=1
        return res