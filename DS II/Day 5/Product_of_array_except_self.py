class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)-1
        res=[1]*(n+1)
        for i in range(n):
            res[i+1]=res[i]*nums[i]
        prev=nums[n]
        for i in range(n):
            res[n-i-1]=res[n-i-1]*prev
            if i!=n:
                prev*=nums[n-i-1]
        return res