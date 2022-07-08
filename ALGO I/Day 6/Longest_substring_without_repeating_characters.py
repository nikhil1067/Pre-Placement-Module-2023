class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=""
        max_len=0
        for i in range(len(s)):
            if s[i] not in res:
                res+=s[i]
            else:
                while s[i] in res:
                    res=res[1:]
                res+=s[i]
            max_len=max(max_len,len(res))
        return max_len