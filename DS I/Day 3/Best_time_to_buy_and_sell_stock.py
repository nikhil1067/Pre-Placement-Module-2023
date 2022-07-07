class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        temp=prices[0]
        for i in prices:
            res=max(res,i-temp)
            temp=min(temp,i)
        return res