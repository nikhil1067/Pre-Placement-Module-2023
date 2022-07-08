class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=nums.count(0)
        while nums.count(0)!=0:
            nums.remove(0)
        nums.extend([0]*x)