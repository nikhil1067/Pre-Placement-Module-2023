class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            x1=nums[i]
            x2=target-x1
            temp=nums[i+1:]
            if x2 in temp:
                res.append(i)
                res.append(temp.index(x2)+i+1)
                break
            else:
                continue
        return res