class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        res1=-1
        res2=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                res1=mid
                high=mid-1
            if nums[mid]>target:
                high=mid-1
            if nums[mid]<target:
                low=mid+1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                res2=mid
                low=mid+1
            if nums[mid]>target:
                high=mid-1
            if nums[mid]<target:
                low=mid+1
        return [res1,res2]