class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[""]
        for i in s:
            temp=[]
            if i.isalpha():
                for j in res:
                    temp.append(j+i.lower())
                    temp.append(j+i.upper())
            else:
                for j in res:
                    temp.append(j+i)
            res=temp
        return res