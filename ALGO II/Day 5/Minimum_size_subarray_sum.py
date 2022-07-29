class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,res=0,len(nums)+1
        s=0 
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                res=min(res,r-l+1)
                s-=nums[l]
                l+=1
        if res==len(nums)+1:
            return 0
        return res 