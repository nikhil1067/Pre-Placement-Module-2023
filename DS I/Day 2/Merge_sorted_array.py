class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1=nums1[:m]
        nums1.clear()
        nums1.extend(temp1)
        temp2=nums2[:n]
        nums2.clear()
        nums2.extend(temp2)
        nums1.extend(nums2)
        nums1.sort()