class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        temp = set()
        for l in range(len(s)-9):
            substr = s[l:l+10]
            if substr in temp:
                res.add(substr)
            temp.add(substr)
            l += 1
        return list(res)