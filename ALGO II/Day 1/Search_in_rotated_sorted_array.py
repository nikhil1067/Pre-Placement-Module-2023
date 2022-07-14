class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def minimum(nums,low,high):
            if high<low:
                return -1
            mid=(low+high)//2
            if low<mid and nums[mid]<nums[mid-1]:
                return mid
            elif mid<high and nums[mid]>nums[mid+1]:
                return mid+1
            elif nums[high]>nums[mid]:
                return minimum(nums,low,mid-1)
            return minimum(nums,mid+1,high)
        
        def binary_search(nums,low,high,target):
            if high<low:
                return -1
            mid=(low+high)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                return binary_search(nums,mid+1,high,target)
            else:
                return binary_search(nums,low,mid-1,target)
        
        low=0
        high=len(nums)-1
        pivot=minimum(nums,low,high)
        if pivot==-1:
            return binary_search(nums,low,high,target)
        if nums[pivot]==target:
            return pivot
        if nums[0]<=target:
            return binary_search(nums,0,pivot-1,target)
        return binary_search(nums,pivot+1,high,target)
        