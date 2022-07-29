class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        temp1=[]
        temp2=[]
        for char in s:
            if char=="#":
                if temp1:
                    temp1.pop()
            else:
                temp1.append(char)
        for char in t:
            if char=="#":
                if temp2:
                    temp2.pop()
            else:
                temp2.append(char)
        if temp1==temp2:
            return True
        else:
            return False