class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr1={}
        arr2={}
        for i in magazine:
            if i in arr1:
                arr1[i]+=1
            else:
                arr1[i]=1
        for i in ransomNote:
            if i in arr2:
                arr2[i]+=1
            else:
                arr2[i]=1
        count=0
        for i in arr2:
            if i in arr1:
                if arr1[i]>=arr2[i]:
                    count+=arr2[i]
        if count==len(ransomNote):
            return True
        else:
            return False