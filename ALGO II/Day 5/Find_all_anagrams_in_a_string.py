class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        letterDict=collections.defaultdict(int)
        for l in p:
            letterDict[l]+=1
        count=0
        i=0
        res=[]
        while i<len(s):
            if i>=len(p) and s[i-len(p)] in letterDict:
                letterDict[s[i-len(p)]]+=1
                if letterDict[s[i-len(p)]]>0:
                    count-=1
            if s[i] in letterDict:
                letterDict[s[i]]-=1
                if letterDict[s[i]]>=0:
                    count+=1
            if count==len(p):
                res.append(i-len(p)+1)
            i+=1
        return res