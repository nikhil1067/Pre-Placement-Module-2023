class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr=[]
        for num in nums:
            if not arr or arr[-1]<num:
                arr.append(num)
                if len(arr)==3:
                    return True
            else:
                for i in range(len(arr)):
                    if arr[i]>=num:
                        arr[i]=num
                        break
        return False