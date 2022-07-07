import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=(-math.inf)
        temp=0
        for i in nums:
            temp+=i
            res=max(res,temp)
            if temp<0:
                temp=0
        return res