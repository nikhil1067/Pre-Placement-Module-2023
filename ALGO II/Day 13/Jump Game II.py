class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = {}
        
        def jump(index):
            
            if index in dp:
                return dp[index]
            
            if index==len(nums)-1:
                dp[index]=0
                return dp[index]
            elif index>=len(nums):
                return None
            else:
                result = None
                for distance in range(1,nums[index]+1):
                    r = jump(index+distance)
                    if r != None:
                        if result is None:
                            result = r
                        elif result>r:
                            result = r
                
                if result is None:
                    dp[index] = None
                else:
                    dp[index] = result+1
                return dp[index]
            
        return jump(0)