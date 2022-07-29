class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [[0,5000] for i in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]-nums[i+1]!=dp[i+1][1]:
                dp[i] = [2,nums[i]-nums[i+1]]
            else:
                dp[i][0] = dp[i+1][0]+1
                dp[i][1] = dp[i+1][1]
        ans = 0
        i = 0
        while i<len(nums):
            if dp[i][0]>2:
                ans+= ((dp[i][0]-2)*(dp[i][0]-1))//2
                i+=dp[i][0]-1
            else:
                i+=1
        return ans