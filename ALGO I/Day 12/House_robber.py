class Solution:
    def rob(self, nums: List[int]) -> int:
        res=0
        temp1=0
        for i in nums:
            temp2=max(i+temp1, res)
            temp1=res
            res=temp2
        return res