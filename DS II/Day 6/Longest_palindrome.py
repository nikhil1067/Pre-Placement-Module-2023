class Solution:
    def longestPalindrome(self, s: str) -> int:
        arr={}
        for char in s:
            if char in arr:
                arr[char]+=1
            else:
                arr[char]=1
        max_odd=0
        for char in arr:
            if arr[char]%2!=0:
                if arr[char]>max_odd:
                    max_odd=arr[char]
                    max_odd_char=char
        res=0
        for char in arr:
            if arr[char]%2!=0:
                if char==max_odd_char:
                    res+=arr[char]
                else:
                    res+=(arr[char]-1)
            else:
                res+=arr[char]
        return res
                