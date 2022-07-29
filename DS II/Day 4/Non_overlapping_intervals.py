class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res=0
        minimum=intervals[0][1]
        for i in range(1,len(intervals)):
            if minimum>intervals[i][0]:
                res+=1
                minimum=min(minimum,intervals[i][1])
            else:
                minimum=intervals[i][1]
        return res