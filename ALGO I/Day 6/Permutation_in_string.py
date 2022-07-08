class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s=sorted(s1)
        temp=s2[:len(s1)]
        j=len(s1)-1
        while j<len(s2):
            if sorted(temp)==s:
                return True
            else:
                if j==len(s2)-1:
                    return False
                temp=temp[1:]+s2[j+1]
                j+=1
        return False
            