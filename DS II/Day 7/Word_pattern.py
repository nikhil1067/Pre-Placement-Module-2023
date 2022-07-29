class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr={}
        s=s.split()
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in arr:
                if arr[pattern[i]]!=s[i]:
                    return False
            if pattern[i] not in arr and s[i] in arr.values():
                return False
            else:
                arr[pattern[i]]=s[i]
        return True