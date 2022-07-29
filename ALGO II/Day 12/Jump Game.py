class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        j=0
        c=0
        if(len(nums)<=1):
            return True
        while(i<len(nums) and j<len(nums)):
            j=i+1
            k=i+nums[i]
            if(nums[i]==0):
                return False
            m=k
            v=k
            while(j<=m and j<len(nums)):
                d=j+nums[j]
                if(d>v):
                    k=j
                    v=d
                j=j+1
            i=k
        return True 