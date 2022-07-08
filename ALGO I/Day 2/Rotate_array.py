class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        temp1=nums[n-k:]
        temp2=nums[:n-k]
        nums.clear()
        nums.extend(temp1)
        nums.extend(temp2)