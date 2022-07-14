class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n-1):
            a=nums[i]
            low=i+1
            high=n-1
            while low<high:
                if (nums[low]+nums[high])==(-a):
                    if [a,nums[low],nums[high]] not in res:
                        res.append([a,nums[low],nums[high]])
                    low+=1
                elif (nums[low]+nums[high])<(-a):
                    low+=1
                else:
                    high-=1
        return res