class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+hi# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        res=math.inf
        while low<=high:
            mid=(low+high)//2
            if isBadVersion(mid)==1:
                temp=mid
                res=min(res,temp)
                high=mid-1
            else:
                low=mid+1
        return resgh)//2
            if nums[mid]==target:
                return mid
            if target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1