class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr={}
        for num in nums:
            if num in arr:
                arr[num]+=1
            else:
                arr[num]=1
        for num in arr:
            if arr[num]>len(nums)/2:
                return num